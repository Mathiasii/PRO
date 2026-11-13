import pytest

from telefonnummer import valider_telefonnummer

def test_telefonnummer_1():
    status, msg, phone = valider_telefonnummer("12121212") == True
    assert status == True