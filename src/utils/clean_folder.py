import os
from src.utils.path_finder import path_finder

def clean_folder(path: str) -> None:
    path_folder = path_finder(path)

    files = os.listdir(path_folder)

    if os.path.isdir(path_folder) and os.path.exists(path_folder):

        for file in files:
            
            file_path = os.path.join(path_folder, file)

            if os.path.isfile(file_path):
                os.remove(file_path)
        