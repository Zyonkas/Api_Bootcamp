from cryptoexchange.views import ShowError, ViewChange, pideCrypto
from cryptoexchange.models import exchange, coin, ModelError
from config import apikey

todas = coin()
todas.trae(apikey)

print("{} de {}".format(len(todas.cryptos), len(todas.cryptos) + len (todas.no_cryptos)))

crypto = pideCrypto()

while crypto != "" :
    if crypto in todas.cryptos:
        tipoCambio = exchange(crypto)
        try:
            tipoCambio.actualiza(apikey)
            ViewChange(tipoCambio.tasa)

            print("{:.2f} €".format(tipoCambio.tasa))
        except ModelError as variable:
            ShowError(variable)

    crypto = pideCrypto()
