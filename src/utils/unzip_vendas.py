from os import path, listdir
import zipfile
from src.utils.path_finder import path_finder
from src.utils.clean_zip_file import clean_zip_file
from src.utils.loading import loading

def unzip_file(origin: str) -> None:

  loading()
  

  #Encontrando a pasta do arquivo zip
  path_folder_origin = path_finder(f"../{origin}")


  #Capturando apenas o nome do arquivo
  zipFileName = listdir(path_folder_origin)[0]

  #Juntando o diretório da pasta + nome do arquivo
  zipFilePath = path.join(path_folder_origin, zipFileName)

  if path.isdir(path_folder_origin) and path.exists(zipFilePath):
      
    with zipfile.ZipFile(zipFilePath, "r") as zip_ref:
      zip_ref.extractall(path=path_folder_origin)

      loading(descompacting=True)
      

    clean_zip_file(path_folder_origin)

    loading(descompacting=True, cleaning = True)
    

  else:
     print("Caminho não encontrado ou localização errada")