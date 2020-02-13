import requests
from bs4 import BeautifulSoup

#this code scrapes the headlines from WSJ
print("From WSJ", "\n")
r = requests.get("http://www.wsj.com", headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
c = r.content
soup = BeautifulSoup(c, "html.parser")
all = soup.find_all("div", {"class" : "WSJTheme--headline--3qd-ycaT"})

for item in all:
    print(item.find_all("h3")[0].text)
print("\n")

#this code scrapes the headlines from FT
print("From the FT", "\n")
r = requests.get("http://www.ft.com", headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
c = r.content
soup = BeautifulSoup(c, "html.parser")
all = soup.find_all("div", {"class" : "o-teaser__heading"})

for item in all:
    print(item.find_all("a")[0].text)
print("\n")

#this code scrapes the headlines from Estadao
print("From Estadao", "\n")
r = requests.get("http://www.estadao.com.br", headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
c = r.content
soup = BeautifulSoup(c, "html.parser")
all = soup.find_all("div", {"class" : "intro"})

for item in all:
    print(item.find_all("h3")[0].text)
print("\n")
