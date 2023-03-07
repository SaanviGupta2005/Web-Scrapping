import lxml as lxml
import pandas as pandas
import pandas as pd
import requests
from bs4 import BeautifulSoup

product_name = []
prices = []
description = []
reviews = []

for i in range(2,12):
    url = "https://www.flipkart.com/search?q=mobiles%20under%2050000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page"+str(i)

    r = requests.get(url)
    # print(r)

    soup = BeautifulSoup(r.text, "lxml")
    box = soup.find("div", class_="_1YokD2 _3Mn1Gg")

    names = box.find_all("div", class_="_4rR01T")
    for i in names:
        name = i.text
        product_name.append(name)
    # print(product_name)
    # print(len(product_name))

    pricing = box.find_all("div", class_="_30jeq3 _1_WHN1")
    for i in pricing:
        price = i.text
        prices.append(price)
    # print(prices)
    # print(len(prices))

    desc = box.find_all("ul", class_="_1xgFaf")
    for i in desc:
        des = i.text
        description.append(des)
    # print(description)
    # print(len(description))

    review = box.find_all("div", class_="_3LWZlK")
    for i in review:
        rev = i.text
        reviews.append(rev)
    # print(reviews)
    # print(len(reviews))

df = pd.DataFrame({"Product Name": product_name, "Prices": prices, "Description": description, "Reviews": reviews})
# print(df)
df.to_csv("D:/flipkart_mobiles_under_50000.csv")

# print(soup)


# np = soup.find("a", class_="_1LKTO3").get("href")
# cnp = "https://www.flipkart.com" + np
# print(cnp)

# url = cnp
# r = requests.get(url)
# soup = BeautifulSoup(r.text, "lxml")
