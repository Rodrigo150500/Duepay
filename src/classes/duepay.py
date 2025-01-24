import os
import pandas as pd
from src.utils.path_finder import path_finder

class Duepay:

    def extract_total(self):
        folder_path = path_finder(f"../input")

        file_in_folder = os.listdir(folder_path)

        file_path = os.path.join(folder_path, file_in_folder[0])
        
        duepay_excel = pd.read_csv(file_path)

        print()
        print(duepay_excel)

        



