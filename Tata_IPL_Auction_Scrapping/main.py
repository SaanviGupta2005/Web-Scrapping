import lxml as lxml
import pandas as pd
import requests as requests
from bs4 import BeautifulSoup

url = "https://www.iplt20.com/auction/2022"
r = requests.get(url)
# print(r)

soup = BeautifulSoup(r.text, "lxml")

table = soup.find("table", class_="ih-td-tab auction-tbl")

title = table.find_all("th", class_="skip-filter")

header = []

for i in title:
    name = i.text
    header.append(name)

df = pd.DataFrame(columns=header)

rows = table.find_all("tr")

for i in rows[1:]:
    first_td = i.find_all("td")[0].find("div", class_="ih-pt-ic").text.strip()
    data = i.find_all("td")[1:]
    row = [tr.text for tr in data]
    row.insert(0, first_td)
    l = len(df)
    df.loc[l] = row

print(df)

df.to_csv("D:/Ipl Auction Stats.csv")