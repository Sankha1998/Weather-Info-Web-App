from bs4 import BeautifulSoup as bs
import requests



class Web_Scraping:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    def city_times(self,soup):
        """Local Time Scraping"""
        times = []
        for i in soup.find_all('tr'):
            try:
                x = (i.find('th').text).replace(u'\xa0', '')
                if x != 'Time':
                    i =x[:5]
                    if float(i)>=12:
                        times.append(i + 'PM')
                    else:
                        times.append(i + 'AM')
                else:
                    pass
            except:
                pass

        return times

    def city_feel_temp(self,soup):
        """Feel Temperature scraping """
        feel_temp = []
        for i in soup.find_all('tr'):
            try:
                feel_temp.append(int(i.find('td', class_='sep').text.strip('°C').replace(u'\xa0', ''))) # feels like
            except:
                pass
        return feel_temp

    def city_weather(self,soup):
        """ weather condition scraping"""
        weather = []
        for i in soup.find_all('tr'):
            try:
                weather.append((i.find('td', class_='small')).text.strip('.'))
            except:
                pass
        return weather

    def city_rain(self,soup):
        """ precipitation scraping"""
        precipitation = []
        p = []
        for i in soup.find_all('td', class_="sep"):
            p.append(i.text.strip())
        l = len(p)
        for i in range(1, l, 2):
            precipitation.append(p[i])
        return precipitation



    def city_scraping(self, city):
        url = "https://www.timeanddate.com/weather/india/{}/hourly".format(city)
        response = requests.get(url, headers=self.headers).text
        soup = bs(response, 'lxml')
        time = self.city_times(soup=soup)
        feel_temp = self.city_feel_temp(soup=soup)
        weather = self.city_weather(soup=soup)
        precipitation = self.city_rain(soup=soup)

        return time, feel_temp, weather, precipitation



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



