from src.utils.unzip_vendas import unzip_file
from src.classes.dataframe_merged import DataframeMerged

def main():

    unzip_file('input/vendas')

    dataframe = DataframeMerged()
    dataframe.dataframe_merged()


if __name__ == "__main__":
    main()

