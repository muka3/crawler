import requests
import bs4

res = resquests.get('')

soup = bs4.BeautifulSoup(res.text, 'lxml')
