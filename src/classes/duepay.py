import os
from src.utils.path_finder import path_finder

class Duepay:

    def extract_total(self):
        folder_path = path_finder(f"../output")
        print()
        print(folder_path)

obj = Duepay()
obj.extract_total()

