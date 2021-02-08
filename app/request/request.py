import urllib3
import json


class Request():
    key_sandbox = r"JMmdQzyIsb1looU+tjjlvJdtjXlE++XGyPh/r74p8rEmG02VOHDeSlcMUMRHjxuL"

    def __init__(self):

        self.http = urllib3.PoolManager()

    def get_letter_details(self, tracking_number):
        # Identifiant de l'objet recherché de 11 à 15 caractères alphanumériques
        r = self.http.request('GET', f'https://api.laposte.fr/suivi/v2/idships/{tracking_number}',
                              headers={
                                  'Accept': 'application/json',
                                  'X-Okapi-Key': self.key_sandbox,
                              }
                              )
        try:
            rsp = json.loads(r.data.decode('utf-8'))
            return rsp
        except json.decoder.JSONDecodeError:
            return None
