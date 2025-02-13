from src.utils.unzip_vendas import unzip_file
from src.classes.dataframe_merged import DataframeMerged

def main():

    try:

        unzip_file('input/vendas')

        dataframe = DataframeMerged()
        dataframe.dataframe_merged()     
    except Exception as exception:
        print(exception)
        input("")   


if __name__ == "__main__":
    main()

