import os
from .interface.vendas_interface import VendasInterface
from xml.etree import ElementTree as ET
from src.utils.path_finder import path_finder
from pandas import DataFrame

class Vendas(VendasInterface):

    def extract_data_cpf_total_chave(self) -> DataFrame:
        
        files_path = self.__find_xmls()

        extract_data = self.__extract_data_from_xml(files_path)

        df = DataFrame(extract_data)

        return df

        
    
    def __find_xmls(self) -> list:
        folder_path = path_finder(f"../input/vendas")
        
        files_in_folder = os.listdir(folder_path)

        files_path = []
        
        for file in files_in_folder:
            files_path.append(os.path.join(folder_path,file))

        return files_path
    
    def __extract_data_from_xml(self, files_xml_path: list) -> dict:
        data = {
                "CPF": [],
                "Total":[],
                "NFe": []
        }
        for xml in files_xml_path:
            
            tree = ET.parse(xml)
            root = tree.getroot()
            

            cpf_reference = root.find(".//CPF")

            if cpf_reference is not None:
                
                #Pegando CPF
                cpf_value = cpf_reference.text.strip()  

                cpf = self.__format_cpf(cpf_value)

                
                #Pegando a chave da Nota
                nfe_reference = root.find(".//infCFe")

                id_value = nfe_reference.get("Id")

                nfe = self.__format_nfe(id_value)


                #Pegando o valor total
                total_reference = root.find(".//vCFe")
                total = float(total_reference.text.strip().replace(",","."))

                data["CPF"].append(cpf)
                data["NFe"].append(nfe)
                data["Total"].append(total)
        
        return data

                
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
