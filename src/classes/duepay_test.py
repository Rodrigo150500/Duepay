from src.classes.duepay import Duepay
from pandas import DataFrame

def test_duepay():

    duepay = Duepay()
    response = duepay.extract_total()

    assert isinstance(response, DataFrame)
