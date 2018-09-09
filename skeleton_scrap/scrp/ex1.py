import requests
from bs4 import BeautifulSoup

souce = requests.get(input("enter link here/> "))

soup = BeautifulSoup(souce.text, 'html.parser')
print(type(soup))
c = soup.get_text()
#print(type(soup.get_text()))
#print(soup.prettify().encode("utf-8"))



with open(input('name/> '), 'wb') as f:
    f.write(soup.get_text().encode("utf-8"))
