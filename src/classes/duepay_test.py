from src.classes.duepay import Duepay

def test_duepay():

    duepay = Duepay()
    res = duepay.extract_total()
    print(res)

