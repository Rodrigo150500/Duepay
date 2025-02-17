import os
import pandas as pd
from src.utils.loading import loading
from src.utils.path_finder import path_finder
from src.classes.interface.duepay_interface import DuepayInterface

class Duepay(DuepayInterface):

    def extract_total(self) -> pd.DataFrame:
        
       
        file_path = self.__find_folder()
        
        data_valor = self.__extract_data_from_xlsx(file_path)
        
        df = pd.DataFrame(data_valor)

        loading(descompacting=True, cleaning=True, extract_data_csv=True)

    
        return df

    def __find_folder(self) -> str:

        folder_path = path_finder(f"../input/duepay")

        while True:
            try:
                file_in_folder = os.listdir(folder_path)[0]

                if ".csv" in file_in_folder:
                    break
            except:
                input("Arquivo duepay .csv não encontrado. Adicione o arquivo .csv na pasta Duepay.\nTecle ENTER para continuar")

        file_path = os.path.join(folder_path, file_in_folder)

        return file_path

    def __extract_data_from_xlsx(self, file_path: str) -> dict:

        duepay_excel = pd.read_csv(file_path, delimiter=';', encoding='utf-8')

        value_list = duepay_excel['VALOR']

        value_list_processed = self.__data_formated(value_list)

        total_column = {"Valor": value_list_processed}

        return total_column

    def __data_formated(self, data_value: list) -> list:
        
        list_replaced = [float(str(value).strip().replace(",",".")) for value in data_value]

        return list_replaced