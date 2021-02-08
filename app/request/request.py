import urllib3
import json


class Request():
    key = "qUaEdLNRaiAmBty5+Ey0O+yj7Si9jVpos0SuI7qejkdKxZVdMGhhB/L+DD/VhLtA"
    key_sandbox = r"+hfCR9theomaP/3rSLLGcqsM00EMx5DjlRClI5Xwnb3cnG30jBwxl/bnCcbRoItV"

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
