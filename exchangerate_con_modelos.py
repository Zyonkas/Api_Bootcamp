from cryptoexchange.models import exchange, coin, ModelError
from config import apikey

todas = coin()
todas.trae(apikey)

print("{} de {}".format(len(todas.criptos), len(todas.criptos) + len (todas.no_criptos)))

crypto = input("introduzca una cripto conocida: ").upper()
while crypto != "" :
    if crypto in todas.criptos:
        tipoCambio = exchange(crypto)
        try:
            tipoCambio.actualiza(apikey)

            print("{:.2f} €".format(tipoCambio.tasa))
        except ModelError as variable:
            print("se ha producido el error {}".format(variable))

    crypto = input("introduzca una cripto conocida: ").upper()