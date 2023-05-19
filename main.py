from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv

CSV = 'output.csv'

option = Options()
option.add_argument('--headless')

url = 'https://xn--90acagbhgpca7c8c7f.xn--p1ai/news'
driver = webdriver.Chrome()
driver.get(url=url)
driver.implicitly_wait(10)
print('ПАРСЕР АКТИВИРОВАН!!!')


def page_info():
    pages = driver.find_elements(By.CLASS_NAME, 'number')
    return pages[4].text


def get_news():
    news = driver.find_elements(By.CLASS_NAME, 'news-card__text')
    return news


def get_img():
    img = driver.find_elements(By.CLASS_NAME, 'news-card__img-container')
    return img


def get_date():
    date = driver.find_elements(By.CLASS_NAME, 'news-card__date')
    return date


def get_link():
    link = driver.find_elements(By.CLASS_NAME, 'news-card')
    return link


def save_doc(items, path):
    with open(path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Описание', 'Ссылка', 'Дата', 'Изображение'])
        for item in items:
            writer.writerow([item['title'], item['link'], item['date'], item['image']])


def get_content(news, img, date, link):
    cards = []
    for item in range(len(news)):
        cards.append(
            {
                'title': news[item].text,
                'image': img[item].find_element(By.TAG_NAME, 'img').get_attribute('src'),
                'date': date[item].text,
                'link': link[item].get_attribute('href')
            }
        )
    return cards


def parser():
    card = []
    for i in range(1, int(page_info()) + 1):
        print('Парсится стицраница:', i)
        card.extend(get_content(get_news(), get_img(), get_date(), get_link()))
        if i == int(page_info()):
            driver.close()
            driver.quit()
            print('Конец работы.')
            break
        element = driver.find_element(By.CLASS_NAME, "btn-next")
        driver.execute_script("arguments[0].scrollIntoView();", element)
        driver.execute_script("arguments[0].click();", element)
        WebDriverWait(driver, 10).until(EC.staleness_of(driver.find_element(By.CLASS_NAME, "news-card__text")))
    save_doc(card, CSV)


parser()
