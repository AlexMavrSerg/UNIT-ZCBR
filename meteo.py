import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

ya_df = pd.read_html("https://yandex.ru/pogoda/details/10-day-weather?lat=44.556975&lon=33.526404&via=ms")

#ya_df = 
ya_new=pd.concat([ya_df[0],ya_df[1],ya_df[2],ya_df[3],ya_df[4],ya_df[5],ya_df[6],ya_df[7],ya_df[8],ya_df[9]],ignore_index=True)
