import pytest

#15913 de 16132 (219)

from cryptoexchange.models import coin, exchange
from config import apikey

def test_coin():
    all = coin()
    assert isinstance(all, coin)
    all.trae(apikey)
    assert len(all.crypto) == 15913
    assert len(all.not_crypto) == 220

def test_exchange_OK():
    BtcUsd = exchange("BTC")
    assert BtcUsd.rate is None
    assert BtcUsd.time is None
    BtcUsd.refresh(apikey)
    assert BtcUsd.rate > 0
    assert isinstance(BtcUsd.time, str)

def test_exchange_no_OK():
    noOK = exchange("KKTUA")    
    assert noOK.rate is None
    assert noOK.time is None
    
    #noOK.actualiza(apikey)

    