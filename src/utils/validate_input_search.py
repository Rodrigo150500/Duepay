def validate_input_search(msg: str) ->int | str:

    pesquisa = str(input(msg)).strip()

    if pesquisa[3] == "." and pesquisa[7] == "." and pesquisa[11] == "-":
        
        return str(pesquisa)

    else:
        if "," in pesquisa:
            pesquisa = pesquisa.replace(",",".").strip()
            
            return float(pesquisa)
        else:

            return float(pesquisa)