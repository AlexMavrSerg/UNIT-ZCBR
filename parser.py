from bs4 import BeautifulSoup
import requests

rddm = 'https://будьвдвижении.рф/news'
unarmy = 'https://yunarmy.ru/yunarmeyskielagerya/'

page1 = requests.get(rddm)
page2 = requests.get(unarmy)

print(page1.status_code)
print(page2.status_code)

filteredNews = []
allNews = []

soup1 = BeautifulSoup(page1.text, 'html.parser')
soup2 = BeautifulSoup(page2.text, 'html.parser')

#print(soup1)
print(soup2)

allNews = soup1.findAll('div', class_='news-page__container')

for data in allNews:
    if data.find('p', class_='news-card__text') is not None:
        filteredNews.append(data.text)

for data in filteredNews:
    print(data)

print(filteredNews)
