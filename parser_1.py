#Используемые модули
import requests
from bs4 import BeautifulSoup as bs

#Соединение с сайтом
unarmy = 'https://yunarmy.ru/press-center/news/'
unarmy_n_award = 'https://yunarmy.ru/press-center/news/nagrazhdenie-nachalnika-shtaba-samarskoy-oblasti/'
rddm = 'https://xn--90acagbhgpca7c8c7f.xn--p1ai/news'
u = requests.get(unarmy)
una = requests.get(unarmy_n_award)
r = requests.get(rddm)
#print(r.status_code)

#print(r.text)

#Парсинг определённого контента Web-страницы
soup = bs(u.text, "html.parser")
news = soup.find_all('li', class_='news-card')
for unarmy_news in news:
    print(unarmy_news.h3)
    print(unarmy_news.p)
    print('https://yunarmy.ru'+unarmy_news.a['href'])
    
soup2 = bs(una.text, "html.parser")
news_award_t = soup2.find_all('div', class_='news-inner')
for unarmy_news_award_title in news_award_t:
    print(unarmy_news_award_title.h1)
news_award_p = soup2.find_all('div', class_='news-inner__article-top')
for unarmy_news_award_desc in news_award_p:
    print(unarmy_news_award_desc.div)
