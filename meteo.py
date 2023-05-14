import requests
from bs4 import BeautifulSoup as bs

r = requests.get('https://yandex.ru/pogoda/details/10-day-weather?lat=44.556975&lon=33.526404&via=ms', headers = {'User-Agent':'Mozilla/5.0'})
soup = bs(r.content, 'lxml')

for card in soup.select('.card:not(.adv)'):
    date = ' '.join([i.text for i in card.select('[class$=number],[class$=month]')])
    print(date)
    temps = list(zip(
                      [i.text for i in card.select('.weather-table__daypart')]
                    , [i.text for i in card.select('.weather-table__body-cell_type_feels-like .temp__value')]
                ))
    print(temps)