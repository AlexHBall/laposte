import urllib3
import json


class Request():

    def __init__(self):
        self.key = r"jOPLSbA8fThnlEVU6J8U/HJ4jY20kfBEGuyBvEgQ65MeXyeAB9by8cucJZizrVJ6"
        self.http = urllib3.PoolManager()


    def get_letter_details(self, tracking_number):
        # Identifiant de l'objet recherché de 11 à 15 caractères alphanumériques
        r = self.http.request('GET', f'https://api.laposte.fr/suivi/v2/idships/{tracking_number}',
                              headers={
                                  'Accept': 'application/json',
                                  'X-Okapi-Key': self.key,
                              }
                              )
        try:
            rsp = json.loads(r.data.decode('utf-8'))
            return rsp
        except json.decoder.JSONDecodeError:
            return None

    def get_latest_event_code(self,response):
        if response:
            try:
                if response['returnCode'] == HTTP_OK:
                    latest_event_code = response['shipment']['event'][-1]['code']
                    return latest_event_code if latest_event_code else None
            except KeyError:
                return None

    def set_request_key(self,key):
        self.key = key