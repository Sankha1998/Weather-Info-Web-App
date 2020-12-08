from bs4 import BeautifulSoup as bs
import requests

import lxml

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
                    i = x[:5]
                    if float(i)>=12:
                        times.append(i + 'PM')     # time
                    else:
                        times.append(i + 'AM')
                else:
                    pass
            except:
                pass

        return times



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

    def city_more_info(self,soup):
        raw_data = []
        for i in soup.find_all('td', class_=""):
            a = (i.text).replace(u'\xa0', '').strip()
            a = a.strip('%')
            a = a.strip('km/h')
            a = a.strip('°C')
            if (a != '↑' and a != '-') and len(a) < 4:
                raw_data.append(a)
        """
        daily temperature, wind speed,humidity"""

        temp_d = []
        wind_speed = []
        humidity = []

        l = len(raw_data)

        for i in range(0, l, 3):
            try:
                temp_d.append(int(raw_data[i]))
            except:
                pass

        for i in range(0, len(temp_d)):
            try:
                temp_d[i] = int(temp_d[i])
            except:
                pass

        for i in range(1, l, 3):
            wind_speed.append(raw_data[i].strip() + 'km/h')

        for i in range(2, l, 3):
            humidity.append(raw_data[i].strip() + '%')
        return temp_d,wind_speed,humidity


    def city_scraping(self, city):
        url = "https://www.timeanddate.com/weather/india/{}/hourly".format(city)
        response = requests.get(url, headers=self.headers).text
        soup = bs(response, 'lxml')
        time = self.city_times(soup=soup)
        more_info = self.city_more_info(soup=soup)
        temp_d = more_info[0]
        wind_speed = more_info[1]
        humidity = more_info[2]
        precipitation = self.city_rain(soup=soup)

        return time, temp_d, wind_speed, humidity, precipitation



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


