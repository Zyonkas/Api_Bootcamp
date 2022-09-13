import requests
from config import apikey

class ModelError(Exception):
    pass


class coin:
    def __init__(self):
        self.crypto = []
        self.not_crypto = []

    def trae(self, apikey):
        r = requests.get("https://rest.coinapi.io/v1/assets?apikey={}".format(apikey))
        if r.status_code != 200:
            raise Exception("Error assets cannot be find: {}".format(r.status_code))

        id_list = r.json()
        
        for id in id_list:
            if id["type_is_crypto"] == 1:
                self.crypto.append(id['asset_id'])
            else:
                self.not_crypto.append(id["asset_id"])


class exchange:
    def __init__(self, crypto):
        self.crypto = crypto
        self.rate = None
        self.time = None

    def refresh(self, apikey):
        r = requests.get('https://rest.coinapi.io/v1/exchangerate/{}/USD?apikey={}'.format(self.crypto, apikey))
        resultado = r.json()
        if r.status_code == 200:
            self.rate = resultado["rate"]
            self.time = resultado["time"]
        else:    
            raise ModelError("{}: {}".format(r.status_code, r.error))