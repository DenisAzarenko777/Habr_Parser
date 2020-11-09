import requests
from bs4 import BeautifulSoup

KEYWORDS = ['дизайн', 'фото', 'web', 'python']
URL = 'https://habr.com/ru/all/page5/'
response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')
host = []
title_link = []
for article in soup.find_all('article', class_='post post_preview'):
    post__text_v1 = article.find_all('div',class_="post__text post__text-html post__text_v1")
    post__text_v2 = article.find_all('div',class_ = 'post__text post__text-html post__text_v2')
    for element in post__text_v1:
        for KW in KEYWORDS:
            if KW in element.text:
                title_element = article.find('a', class_='post__title_link')
                title = title_element.text
                link = title_element.attrs.get('href')
                print(f'{title} = {link}')
    for element in post__text_v2:
        for KW in KEYWORDS:
            if KW in element.text:
                title_element = article.find('a', class_='post__title_link')
                title = title_element.text
                link = title_element.attrs.get('href')
                print(f'{title} = {link}')
    host.append(post__text_v1)
    host.append(post__text_v2)
'''
for element in host:
    for elem in element:
        for KW in KEYWORDS:
            if KW in elem.text:
                print(elem.text)
                print("_________________")
'''










'''
    if  post__text_v1 != [] or post__text_v2 != []:
        print(post__text_v1)
        print(post__text_v2)
'''

