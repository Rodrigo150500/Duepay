import os
from xml.etree import ElementTree as ET
from src.utils.path_finder import path_finder
from pandas import DataFrame

class Vendas:

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
                "NFe": []
        }
        for xml in files_xml_path:
            
            tree = ET.parse(xml)
            root = tree.getroot()

            cpf_reference = root.find(".//CPF")

            if cpf_reference is not None:

                cpf = cpf_reference.text.strip()            

                nfe_reference = root.find(".//infCFe")

                id_value = nfe_reference.get("Id")

                nfe = self.__process_infCFe(id_value)

                data["CPF"].append(cpf)
                data["NFe"].append(nfe)
        
        return data

                



            

    def __process_infCFe(self, nfc_value: str) -> str:

        return nfc_value[3:]


