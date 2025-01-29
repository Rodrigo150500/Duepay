from src.classes.vendas import Vendas
from pandas import DataFrame

def test_vendas():

    vendas = Vendas()

    response = vendas.extract_data_cpf_total_chave()
    print()
    print(response)

    #assert isinstance(response, DataFrame)
    
