from bs4 import BeautifulSoup
import requests

def get_weather():
    weather_url = "http://www.nchmf.gov.vn/kttvsite/"
    weather_data_dict = {
        'title': '',
        'loc': '',
        # 'min_temp': '', 
        # 'min_temp': '',
        'temp': '',
        'detail': ''
    }

    r = requests.get(weather_url)
    soup = BeautifulSoup(r.content, 'html.parser')

    titles = soup.find_all('h3')
    locs = soup.find_all('a', class_='tt-location')
    temps = soup.find_all('span', class_='text-weather-location')
    details = soup.find_all('p', class_='text-list-weather')
    
    weather_data_dict['title'] = titles[0].text + '.'
    weather_data_dict['loc'] = locs[0].text + '.'
    weather_data_dict['temp'] = temps[0].text + '.'
    weather_data_dict['detail'] = details[0].text

    return weather_data_dict 