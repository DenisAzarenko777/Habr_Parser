import requests
from bs4 import BeautifulSoup


KEYWORDS = ['дизайн', 'фото', 'web', 'python']
URL = 'https://habr.com/ru/all/'


class Python_parser_habr:

    def __init__(self,KEYWORDS: list ,URL: str) -> None:
        self.URL = URL
        self.KEYWORDS = KEYWORDS
        self.Habr_list = []

    def get_hab(self):
        try:
            for i in range(0,50,1):
                self.response = requests.get(self.URL)
                self.soup = BeautifulSoup(self.response.text, 'html.parser')
                for article in self.soup.find_all('article', class_ = 'post post_preview'):
                    self.hubs = article.find_all('a', class_ = "hub-link")
                    self.post__text_v1 = article.find_all('div', class_="post__text post__text-html post__text_v1")
                    self.post__text_v2 = article.find_all('div', class_='post__text post__text-html post__text_v2')
                    self.hubs_text = list(map(lambda x: x.text.lower(), self.hubs))
                    for element in self.post__text_v1:
                        for KW in self.KEYWORDS:
                            if KW in element.text:
                                self.title_element = article.find('a', class_='post__title_link')
                                self.title = self.title_element.text
                                self.link = self.title_element.attrs.get('href')
                                self.Habr_list.append((f'{self.title} = {self.link}'))
                                print(f'{self.title} = {self.link}')
                    for element in self.post__text_v2:
                        for KW in self.KEYWORDS:
                            if KW in element.text:
                                self.title_element = article.find('a', class_='post__title_link')
                                self.title = self.title_element.text
                                self.link = self.title_element.attrs.get('href')
                                self.Habr_list.append((f'{self.title} = {self.link}'))
                                print(f'{self.title} = {self.link}')

                    for KW in self.KEYWORDS:
                        if KW in self.hubs_text:
                            self.title_element = article.find('a', class_ = 'post__title_link')
                            self.title = self.title_element.text
                            self.link = self.title_element.attrs.get('href')
                            print(f'{self.title} = {self.link}')
                            self.Habr_list.append((f'{self.title} = {self.link}'))
                self.link_next_all = self.soup.find('a', class_ = 'arrows-pagination__item-link arrows-pagination__item-link_next', id = 'next_page')
                self.link_next_text = self.link_next_all.text
                self.link_next = self.link_next_all.attrs.get('href')
                self.link_next1 = 'https://habr.com/'
                self.link_next2 = self.link_next1 + str(self.link_next)
                self.URL = self.link_next2

            return self.Habr_list
        except:
            return  self.Habr_list


if __name__ == '__main__':
    parser = Python_parser_habr(KEYWORDS,URL)
    parser.get_hab()
    MyFile = open ('output.txt','w',encoding='utf-8')
    MyList = list(map(lambda x: x + '\n',parser.get_hab()))
    MyFile.writelines(MyList)
    MyFile.close()