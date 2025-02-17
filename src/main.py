import os
from src.utils.unzip_vendas import unzip_file
from src.classes.dataframe_merged import DataframeMerged
from src.classes.search_for_xml import SearchForXML
from src.utils.validate_input_choice import validate_input_choice
from src.utils.validate_input_search import validate_input_search 


def main():

    while True:
        print()

        escolha = validate_input_choice("Deseja realizar qual procedimento: \n1 - Gerar Duepay Excel\n2 - Realizar pesquisa\n3 - Sair\nOpcao:")

        if escolha == 1:
            try:
                
                validacao = unzip_file('input/vendas')

                if validacao == True:

                    dataframe = DataframeMerged()
                    dataframe.dataframe_merged()

                else:
                    raise Exception     

            except Exception as exception:
                print(exception)
        elif escolha == 2:

            while True:

                try:
                    unzip_file('input/vendas')
                except:
                    pass


                try:
                    print()
                    pesquisa = validate_input_search("Digite o CPF ou o valor total.\nExemplo:\nCPF: xxx.xxx.xxx-xx\nTotal: xx.xx\nValor: ")                    
                    
                    search = SearchForXML(pesquisa)

                    search.search()

                    escolha = validate_input_choice("Deseja realizar outra pesquisa: \n1 - Sim\n2 - Não\n3 - Volta\nOpção:")

                    if escolha == 2 or escolha == 3:
                        break
                    
                except Exception as exception:
                    print(exception)
                    input("")
        elif escolha == 3:
            break
        
        
    
if __name__ == "__main__":
    main()

