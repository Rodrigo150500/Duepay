from src.classes.duepay import Duepay
from src.classes.vendas import Vendas
from src.utils.path_finder import path_finder
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)


def main():
    dataframe_duepay = Duepay().extract_total()

    dataframe_vendas = Vendas().extract_data_cpf_total_chave()

    dataframe_merge = dataframe_duepay.merge(dataframe_vendas, left_on="Valor", right_on="Total", how='outer')

    dataframe_merge = dataframe_merge.fillna("Verificar").infer_objects(copy=False)

    name_excel_file_path = f"{path_finder("../output")}/Duepay_Final.xlsx"

    dataframe_merge.to_excel(name_excel_file_path, index=False)



if __name__ == "__main__":
    main()

