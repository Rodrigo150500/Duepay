import os
import zipfile
from src.utils.path_finder import path_finder

def unzip_file(origin: str) -> None:

    path_folder_origin = path_finder(f"../{origin}")


    zipFileName = os.listdir(path_folder_origin)[0]

    zipFilePath = os.path.join(path_folder_origin, zipFileName)

    if os.path.isdir(path_folder_origin) and os.path.exists(zipFilePath):
        
      with zipfile.ZipFile(zipFilePath, "r") as zip_ref:
        zip_ref.extract(path_folder_origin)
    else:
       print("Caminho não encontrado")



unzip_file("input/vendas")