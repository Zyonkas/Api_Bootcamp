from curses.ascii import isalpha
import requests
from config import apikey



crypto = input("Introduce a cryptocurrency: ")

while crypto != "":
    if crypto.isalpha():
        r = requests.get('https://rest.coinapi.io/v1/exchangerate/{}/USD?apikey={}'.format(crypto, apikey))

        resultado = r.json()
        if r.status_code == 200:
            print("{:.2f} $".format(resultado["rate"]))
        else:
            resultado = r.json(["error"])
    
    crypto = input("Introduce a cryptocurrency: ")