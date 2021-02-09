import urllib3
import json


class Request():
    key = r"7NoU4nqjV5ndr+pVDYf8EZaTZgCG85QZbWb71Evjwl0wJKeqplIdXM/QAf+ssSXg"
    def __init__(self):
        self.http = urllib3.PoolManager()

    def get_letter_details(self, tracking_number):
        # Identifiant de l'objet recherché de 11 à 15 caractères alphanumériques
        r = self.http.request('GET', f'https://api.laposte.fr/suivi/v2/idships/{tracking_number}',
                              headers={
                                  'Accept': 'application/json',
                                  'X-Okapi-Key': r"dBb/NahoRmC+bnXZIQf+XPpxXXjMeuHhgft9U6o2ZFefwyo/+CgU8FuWnFMFFlsi",
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
                if response['returnCode'] == 200:
                    latest_event_code = response['shipment']['event'][-1]['code']
                    return latest_event_code if latest_event_code else None
            except KeyError:
                return None
