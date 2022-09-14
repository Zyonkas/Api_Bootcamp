def pideCrypto():
    crypto = input("Introduzca una crypto conocida: ").upper()
    return crypto

def ViewChange(rate):
    print("{:.2f} €".format(rate))

def ShowError(error):
    print("se ha producido el error {}".format(error))
