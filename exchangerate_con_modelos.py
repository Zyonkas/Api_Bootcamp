from cryptoexchange.models import exchange, coin, ModelError
from config import apikey

todas = coin()
todas.trae(apikey)

print("{} de {}".format(len(todas.crypto), len(todas.crypto) + len (todas.not_crypto)))

crypto = input("introduzca una cripto conocida: ").upper()
while crypto != "" :
    if crypto in todas.cryptos:
        tipoCambio = exchange(crypto)
        try:
            tipoCambio.actualiza(apikey)

            print("{:.2f} €".format(tipoCambio.tasa))
        except ModelError as variable:
            print("se ha producido el error {}".format(variable))

    crypto = input("introduzca una cripto conocida: ").upper()