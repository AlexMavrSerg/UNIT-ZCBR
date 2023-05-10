#Используемые библиотеки
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

#Соединение с сайтом
unarmy = 'https://yunarmy.ru/press-center/news/'
rddm = 'https://xn--90acagbhgpca7c8c7f.xn--p1ai/news'
u = requests.get(unarmy)
r = requests.get(rddm)
#print(r.status_code)

#print(r.text)

#Парсинг определённого контента Web-страницы
soup = bs(u.text, 'html.parser')
news = soup.find_all('li', class_='news-card')
for unarmy_news in news:
    print(unarmy_news.h3)
    print(unarmy_news.p)
    print('https://yunarmy.ru'+unarmy_news.a['href'])