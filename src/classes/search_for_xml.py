import os
from src.utils.path_finder import path_finder
from xml.etree import ElementTree as ET

class SearchForXML:

    def __init__(self, value: str )-> None:
       self.__value = value
       self.__found = False


    def search(self):

        files_path = self.__find_xmls()

        self.__search_manager(files_path)

        if (self.__found == False):
            print("Valores não encontrados")
        
    

    def __find_xmls(self) -> list:
        folder_path = path_finder(f"../input/vendas")        
        
        files_in_folder = os.listdir(folder_path)

        files_path = []
        
        for file in files_in_folder:
            files_path.append(os.path.join(folder_path,file))

        return files_path
    

    
    def __search_manager(self, files_xml_path: list) -> None:
        


        for xml in files_xml_path:
            
            tree = ET.parse(xml)
            root = tree.getroot()            

            #pegando a data
            date_reference = root.find(".//dEmi") 

            date_value = date_reference.text.strip()

            date = self.__format_date(date_value)
            
            #Pegando a chave da Nota
            nfe_reference = root.find(".//infCFe")

            id_value = nfe_reference.get("Id")

            nfe = self.__format_nfe(id_value)

            #Pegando o valor total
            total_reference = root.find(".//vCFe")
            total = float(total_reference.text.strip().replace(",","."))

            cpf_reference = root.find(".//CPF")


            cpf = None
            
            if cpf_reference is not None:
                cpf_value = cpf_reference.text.strip()  
                cpf = self.__format_cpf(cpf_value)  # Agora formatado corretamente como xxx.xxx.xxx-xx

            # Verifica o tipo de entrada e realiza a comparação correta
            encontrou = False
            if isinstance(self.__value, str) and cpf == self.__value:  # Se for CPF (string)
                encontrou = True
            elif isinstance(self.__value, float) and total == self.__value:  # Se for valor total (float)
                encontrou = True

            # Se encontrar, imprime uma única vez
            if encontrou:
                self.__found = True
                print("")
                print(f"Caminho: {xml}")
                print(f"Data: {date}")
                print(f"CPF: {cpf if cpf is not None else 'Sem CPF'}")
                print(f"Total: {total:.2f}")
                print(f"Chave de Acesso: {nfe}")
                print("-" * 50)
                    
                

            
    def __format_nfe(self, nfe_value: str) -> str:

        nfe_with_no_string = nfe_value[3:]

        nfe = ""
        for i in range(0, len(nfe_with_no_string)):
            if i % 4 == 0:
                nfe += " "+nfe_with_no_string[i]
            else:
                nfe += nfe_with_no_string[i]

        return nfe
    
    def __format_cpf(self, cpf_value: str) -> str:
        #xxx.xxx.xxx-xx
        cpf = f"{cpf_value[0:3]}.{cpf_value[3:6]}.{cpf_value[6:9]}-{cpf_value[9:11]}"
        return cpf

    def __format_date(self, date: str) -> str:

        #dd/mm/aaaa
        #20250203 03/02/2025 

        dia = date[6:8]
        mes = date[4:6]
        ano = date[0:4]

        date_formated = f'{dia}/{mes}/{ano}'


        return date_formated