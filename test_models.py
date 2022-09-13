import pytest

#15913 de 16132 (219)

from cryptoexchange.models import coin
from config import apikey

def test_coin():
    all = coin()
    assert isinstance(all, coin)
    all.trae(apikey)
    assert len(all.crypto) == 15193
    assert len(all.not_crypto) == 219