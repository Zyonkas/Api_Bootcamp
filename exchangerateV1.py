from curses.ascii import isalpha
import requests
apikey = "B380CFA0-4540-4CE3-B855-2C8C48D3A572"

r = requests.get("https://rest.coinapi.io/v1/assets?apikey={}".format(apikey))
if r.status_code != 200:
    raise Exception("Error assets cannot be find: {}".format(r.status_code))

id_list = r.json()
final_list = []
for id in id_list:
    if id["type_is_crypto"] == 1:
        final_list.append(id['asset_id'])

crypto = input("Introduce a cryptocurrency: ").upper()

while crypto != "":
    if crypto in final_list:
        r = requests.get('https://rest.coinapi.io/v1/exchangerate/{}/USD?apikey={}'.format(crypto, apikey))

        resultado = r.json()
        if r.status_code == 200:
            print("{:.2f} $".format(resultado["rate"]))
        else:
            print(resultado = r.json["error"])
    
    crypto = input("Introduce a cryptocurrency: ").upper()