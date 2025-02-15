import re

def validate_total(valor: str) -> bool:
    validacao = r"^\d+(?:[\.,]\d{2})?$"
    
    return bool(re.fullmatch(validacao, valor))

def validate_cpf(valor: str) -> bool:
    padrao = r"^\d{3}\.\d{3}\.\d{3}-\d{2}$"
    return bool(re.fullmatch(padrao, valor))


def validate_input_search(msg: str) ->int | str:


    while True:
        pesquisa = str(input(msg)).strip()

    
        if validate_cpf(pesquisa) == True:

            return pesquisa
        
        elif validate_total(pesquisa) == True:

            if "," in pesquisa:
                pesquisa = pesquisa.replace(",",".")
                
                return float(pesquisa)

            return float(pesquisa)

        else:

            print("Entrada Inválida")
            print("")



