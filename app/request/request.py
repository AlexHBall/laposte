import urllib3
import json
from os import environ

from app.request.response import Response


class Request():
    def __init__(self):
        self.key = environ.get('WEATHER_API_KEY')
        self.url = environ.get('WEATHR_API_ADRESS')
        self.http = urllib3.PoolManager()

    def get_weather_city_name(self, city_name):
        r = self.http.request('GET', f'{self.url}?q={city_name}&appid={self.key}',
                              )
        try:
            data = json.loads(r.data.decode('utf-8'))
            return Response(response_json=data)
            
        except json.decoder.JSONDecodeError:
            return None