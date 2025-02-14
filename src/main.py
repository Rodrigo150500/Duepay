from src.utils.unzip_vendas import unzip_file
from src.classes.dataframe_merged import DataframeMerged
from src.classes.search_for_xml import SearchForXML
from src.utils.validate_input_choice import validate_input_choice
from src.utils.validate_input_search import validate_input_search 

def main():

    while True:

        escolha = validate_input_choice("Deseja realizar qual procedimento: \n1 - Gerar Duepay Excel\n2 - Realizar pesquisa\n3 - sair\nOpcao:")

        if escolha == 1:
            try:

                unzip_file('input/vendas')

                dataframe = DataframeMerged()
                dataframe.dataframe_merged()     
            except Exception as exception:
                print(exception)
                input("")
        elif escolha == 2:
            try:
                pesquisa = validate_input_search("Digite o CPF ou o valor total.\nCPF: xxx.xxx.xxx-xx\nTotal: 99.99\nValor: ")

                search = SearchForXML(pesquisa)

                search.search()
                
            except Exception as exception:
                print(exception)
                input("")
        elif escolha == 3:
            break
        
        
    
if __name__ == "__main__":
    main()

