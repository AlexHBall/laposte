import urllib3
import json
from os import environ



class Request():
    def __init__(self):
        self.key = environ.get('WEATHER_API_KEY')
        self.url = environ.get('WEATHR_API_ADRESS')
        self.http = urllib3.PoolManager()

    def get_letter_details(self, tracking_number):
        r = self.http.request('GET', f'https://api.laposte.fr/suivi/v2/idships/{tracking_number}',
                              headers={
                                  'Accept': 'application/json',
                                  'X-Okapi-Key': environ.get('LA_POSTE_API_KEY'),
                              }
                              )
        try:
            rsp = json.loads(r.data.decode('utf-8'))
            return rsp
        except json.decoder.JSONDecodeError:
            return None

    def get_weather_city_name(self, city_name):
        r = self.http.request('GET', f'{self.url}?q={city_name}&appid={self.key}',
                              )
        try:
            rsp = json.loads(r.data.decode('utf-8'))
            print(rsp)
            return rsp
        except json.decoder.JSONDecodeError:
            return None

    def get_latest_event_code(self,response):
        if response:
            try:
                if response['returnCode'] == 200:
                    latest_event_code = response['shipment']['event'][-1]['code']
                    return latest_event_code if latest_event_code else None
            except KeyError:
                return None
