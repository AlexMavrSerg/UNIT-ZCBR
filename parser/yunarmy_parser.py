import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import sys
import json
import string


all_data = {}
images_dir = "images/"
"""
"link": {
    "name": "..."
    "preview-image": "url"
    "content": {
        "date": "..."
        "location": "..."
        "age": "..."
        "description": "..."
        "video": "url"
        "categories": "..."
        "specifications": [...]
        "images": [urls]
        "how-to-participate": [...]
        "content": [...]
        "results": [...]
        "partners": [...]
    }
}
"""

def __parse_link(link):
    post = {}
    r = requests.get(link)
    print(link + ':', r.status_code)
    page = bs(r.text, 'lxml')

    # getting name
    project_inner_header = page.find("div", attrs={"class": "project-inner__header"})
    post["name"] = project_inner_header.find("h1").text
    print("name:", post["name"])

    # getting preview
    img = project_inner_header.find("img")
    if img != None:
        post["preview-image"] = URL_BASE + img["src"]
    else:
        post["preview-image"] = None
    print("preview-image:", post["preview-image"])

    post["content"] = {}

    # date, location, age
    project_inner_wrapper = page.find("div", attrs={"class":"project-inner__wrapper"})
    info = project_inner_wrapper.find_all("h4")
    names = ["date", "location", "age"]
    for i in range(len(names)):
        content = info[i].find("span")
        content = content.find("span")
        cnt = content.find("b")
        if cnt is None:
            post["content"][names[i]] = content.text
        else:
            post["content"][names[i]] = cnt.text
        print(names[i] + ":", post["content"][names[i]])
    
    # description
    all_paragraphs = project_inner_wrapper.find_all("p")
    post["content"]["description"] = []
    for paragraph in all_paragraphs:
        post["content"]["description"].append(paragraph.text)
    print("description:", post["content"]["description"])
    



if __name__ == "__main__":
    URL_BASE = 'https://yunarmy.ru'
    URL = URL_BASE + '/yunarmeyskielagerya'

    r = requests.get(URL)
    if r.status_code in [404]:
        print("ERROR {}".format(r.status_code))
        sys.exit(1)

    page = bs(r.text, 'lxml')

    # Извлечение ссылок
    news = page.find("div", attrs={"class": "projects__wrap"})
    news_list = news.find("ul")
    links_html = news_list.select("ul li a")
    links = [link["href"] for link in links_html]
    #################################################################

    for link in links:
        link = URL_BASE + link
        all_data[link] = __parse_link(link)   
        print("\n")