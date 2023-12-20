import requests
from bs4 import BeautifulSoup
from weasyprint import HTML
import os

class Crawler:
    def __init__(self, url):
        self.url = url
    
    def run(self):
        html = self.get_html()
        text = self.find_all_text(html)
        self.generate_pdf(text)


    def get_html(self):
        return requests.get(self.url).text
    
    def find_all_text(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        container = soup.find_all('p')
        container = container[1:]
        container = container[:-14]
        contentList = []
        for con in container:
            contentList.append(str(con))
        content = ' '.join(contentList)
        return content


    def generate_pdf(self, filtered_html):

        pdf_path = os.getcwd() + "/output.pdf"
        html_object = HTML(string=filtered_html)
        html_object.write_pdf(pdf_path)



if __name__ == '__main__':
    url = input("Please input url to article \nfor example https://yomujp.com/n4_itsumofutaride/\n")
    Crawler(url).run()