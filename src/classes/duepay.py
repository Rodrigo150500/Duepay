import os
import pandas as pd
from src.utils.path_finder import path_finder
from src.classes.interface.duepay_interface import DuepayInterface

class Duepay(DuepayInterface):

    def find_folder(self) -> str:
        folder_path = path_finder(f"../input/duepay")

        file_in_folder = os.listdir(folder_path)

        file_path = os.path.join(folder_path, file_in_folder[0])
        
        return file_path

    
    def extract_total(self) -> pd.DataFrame:

        file_path = self.find_folder()

        duepay_excel = pd.read_csv(file_path, delimiter=';', encoding='utf-8')

        total_column = sorted(duepay_excel['VALOR'])
        
        df = pd.DataFrame(total_column)

        return df



