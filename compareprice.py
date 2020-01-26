import urllib.request as req
from bs4 import BeautifulSoup as bs

def qry_flipkart(name):
    lst = name.split()
    qry_flipkart = 'https://www.flipkart.com/search?q='
    for l in lst:
        qry_flipkart = qry_flipkart + '+' + l
    return qry_flipkart


def filter(name):
    s = str(name).lower()
    # print(s)
    index = s.find('(')
    # print(s[0:index-1])
    return s[0:index - 1]

def qry_Amazon(name):
    lst = name.split()
    qry = 'https://www.amazon.in/s?k='
    for l in lst:
        qry = qry + '+' + l
    return qry

item = input("Enter name of product to search : ")

#for flipkart
print("Flipkart Query  "+qry_flipkart(item))
data = req.urlopen(qry_flipkart(item)).read()
soup = bs(data, 'lxml')
count = 0
def has_id_no_class(tag):
    return tag.has_attr('data-id') and not tag.has_attr('class')
for dataId in soup.findAll(has_id_no_class):
    name = dataId.findChildren('div', {"class": "_3wU53n"})
    flag = True
    content = []
    for item1 in name:
        item1 = [content for content in item1.text.split('\n') if len(content) > 0]
        item1 = ' '.join(item1)
        content.append(item1)
    for i in content:
        if item.lower() in i.lower():
            print(i)
        else:
            flag = False

    price = dataId.findChildren('div', {"class": "_1vC4OE _2rQ-NK"})
    content1 = []
    for item2 in price:
        item2 = [content1 for content1 in item2.text.split('\n') if len(content1) > 0]
        item2 = ' '.join(item2)
        content1.append(item2)
    for i in content1:
        if flag:
            print(i)

    links_with_text = []
    for a in dataId.findChildren('a', {"class": "_31qSD5"}, href=True):
        if a.text:
            links_with_text.append(a['href'])
    for t in links_with_text:
        if flag:
            print("https://www.flipkart.com"+t)
    if flag:
        print("*"*90)
print()
print()


#for amazon
print("Amazon Query  "+qry_Amazon(item))
data = req.urlopen(qry_Amazon(item)).read()
soup = bs(data, 'lxml')
count = 0
def has_data_asin(tag):
    return tag.has_attr('data-asin')

for dataId in soup.findAll(has_data_asin):
    name = dataId.findChildren('span', {"class": "a-size-medium a-color-base a-text-normal"})
    flag = True
    content = []
    for item1 in name:
        item1 = [content for content in item1.text.split('\n') if len(content) > 0]
        item1 = ' '.join(item1)
        content.append(item1)
    for i in content:
        if item.lower() in i.lower():
            print(i)
        else:
            flag = False
    price_flag = False
    price = dataId.findChildren('span', {"class": "a-color-price"})
    if(price == []):
        price = dataId.findChildren('span', {"class": "a-price-whole"})
        price_flag = True

    content1 = []
    for item2 in price:
        item2 = [content1 for content1 in item2.text.split('\n') if len(content1) > 0]
        item2 = ' '.join(item2)
        content1.append(item2)
    for i in content1:
        if flag:
            #print(price)
            print(i)

    links_with_text = []
    for a in dataId.findChildren('a', {"class": "a-link-normal a-text-normal"}, href=True):
        if a.text:
            links_with_text.append(a['href'])

    for t in links_with_text:
        if flag:
            print("https://www.amazon.in"+t)

    if flag:
        print("*"*90)
print()
print()





