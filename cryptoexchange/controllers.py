from cryptoexchange.views import ShowError, ViewChange, pideCrypto
from cryptoexchange.models import exchange, coin, ModelError
from config import apikey

class app:
    def exe(self):
        todas = coin()
        todas.trae(apikey)

        crypto = pideCrypto()

        while crypto != "" :
            if crypto in todas.crypto:
                tipoCambio = exchange(crypto)
                try:
                    tipoCambio.refresh(apikey)
                    ViewChange(tipoCambio.rate)

                    print("{:.2f} €".format(tipoCambio.rate))
                except ModelError as variable:
                    ShowError(variable)

            crypto = pideCrypto()