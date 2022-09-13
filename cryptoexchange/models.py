import requests
from config import apikey


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