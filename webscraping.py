from bs4 import BeautifulSoup as bs
import requests



class Web_Scraping:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    def world_wide_scraping(self):
        url = 'https://www.timeanddate.com/weather/?sort=1'
        response = requests.get(url, headers=self.headers).text
        soup = bs(response, 'lxml')
        raw_data = soup.find('table')
        contries = []
        temp = []
        for i in raw_data:
            try:
                contries.append((i.find('td', class_="").text).strip('*'))
            except:
                pass
            try:
                temp.append((i.find('td', class_="rbi").text.replace(u'\xa0', '')).strip())
            except:
                pass

        return contries, temp



