from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import csv

CSV = 'output.csv'
URL = 'https://xn--90acagbhgpca7c8c7f.xn--p1ai/news/'
TEXT_CLASS = 'article__content-title'
IMG_CLASS = 'article__content-img-container'
DATE_CLASS = 'article__content-date'
LINK_CLASS = 'news-card'
FULL_TEXT_CLASS = "//div[@class='article__content-body-content ck-content']"


def get_driver(url):
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    driver.implicitly_wait(5)
    print('ПАРСЕР АКТИВИРОВАН!!!')
    return driver


def page_info(driver):
    page = driver.find_elements(By.CLASS_NAME, LINK_CLASS)
    url = page[0].get_attribute('href')
    news_id = re.search(r'news/(\d+)', url).group(1)
    return news_id


def get_news(driver):
    news = driver.find_elements(By.CLASS_NAME, TEXT_CLASS)
    return news


def get_full_txt(driver):
    full_txt = driver.find_elements(By.XPATH, FULL_TEXT_CLASS)
    return full_txt


def get_img(driver):
    img = driver.find_elements(By.CLASS_NAME, IMG_CLASS)
    return img


def get_date(driver):
    date = driver.find_elements(By.CLASS_NAME, DATE_CLASS)
    return date


def get_link(driver):
    link = driver.find_elements(By.CLASS_NAME, LINK_CLASS)
    return link


def save_doc(items, path):
    with open(path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Описание', 'Дата', 'Изображение', 'Ссылка', 'Полный текст'])
        for item in items:
            writer.writerow([item['title'], item['date'], item['image'], item['link'], item['full_txt']])


def get_content(news, img, date, full_txt, url):
    cards = []
    cards.append(
        {
            'title': news[0].text,
            'image': img[0].find_element(By.TAG_NAME, 'img').get_attribute('src'),
            'date': date[0].text,
            'full_txt': full_txt[0].text.replace('\n\n', '\n').replace('\n\n', '\n').strip(),
            'link': url
        }
    )
    return cards


def parser():
    card = []
    with get_driver(URL) as driver:
        for page_num in range(int(page_info(driver)), 14, -1):
            url = f"{URL}{page_num}"
            driver.get(url)
            driver.implicitly_wait(2)
            try:
                error = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CLASS_NAME, TEXT_CLASS)))
            except:
                print('Страница не найдена!', url)
                continue
            else:
                print('Парсаться страница:', url)
                card.extend(get_content(get_news(driver), get_img(driver), get_date(driver), get_full_txt(driver), url))
    save_doc(card, CSV)


if __name__ == '__main__':
    parser()