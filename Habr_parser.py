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
                response = requests.get(self.URL)
                soup = BeautifulSoup(response.text, 'html.parser')
                for article in soup.find_all('article', class_ = 'post post_preview'):
                    hubs = article.find_all('a', class_ = "hub-link")
                    hubs_text = list(map(lambda x: x.text.lower(), hubs))

                    for KW in self.KEYWORDS:
                        if KW in hubs_text:
                            title_element = article.find('a', class_ = 'post__title_link')
                            title = title_element.text
                            link = title_element.attrs.get('href')
                            print(f'{title} = {link}')
                            self.Habr_list.append((f'{title} = {link}'))
                link_next_all = soup.find('a', class_ = 'arrows-pagination__item-link arrows-pagination__item-link_next', id = 'next_page')
                link_next_text = link_next_all.text
                link_next = link_next_all.attrs.get('href')
                link_next1 = 'https://habr.com/'
                link_next2 = link_next1 + str(link_next)
                self.URL = link_next2
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