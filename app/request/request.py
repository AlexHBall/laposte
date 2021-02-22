import urllib3
import json
from os import environ



class Request():
    def __init__(self):
        self.key = environ.get('WEATHER_API_KEY')
        self.url = environ.get('WEATHR_API_ADRESS')
        self.http = urllib3.PoolManager()

    def get_weather_city_name(self, city_name):
        r = self.http.request('GET', f'{self.url}?q={city_name}&appid={self.key}',
                              )
        try:
            rsp = json.loads(r.data.decode('utf-8'))
            return rsp
        except json.decoder.JSONDecodeError:
            return None