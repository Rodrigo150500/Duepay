from .interface.dataframe_mered_interface import DataframeMergedInterface
from src.classes.duepay import Duepay
from src.classes.vendas import Vendas
from src.utils.path_finder import path_finder
from pandas import DataFrame
from src.utils.loading import loading


class DataframeMerged(DataframeMergedInterface):


    def dataframe_merged(self) -> None:

        dataframe_duepay = Duepay().extract_total()

        dataframe_vendas = Vendas().extract_data_cpf_total_chave()

        dataframe_merge = self.__dataframe_merge(dataframe_vendas, dataframe_duepay)

        self.__export_dataframe(dataframe_merge)

        loading(descompacting=True, cleaning=True, extract_data_csv= True, extract_data_xml= True, export_to_excel=True)


    def __dataframe_merge(self, dataframe_vendas: DataFrame, dataframe_duepay: DataFrame) -> DataFrame:

        dataframe_merge = dataframe_duepay.merge(dataframe_vendas, left_on="Valor", right_on="Total", how='outer')

        dataframe_merge_filled = dataframe_merge.fillna("Verificar").infer_objects(copy=False)

        return dataframe_merge_filled
    
    def __export_dataframe(self, dataframe: DataFrame) -> None:
        
        name_excel_file_path = f"{path_finder("../output")}/Duepay_Final.xlsx"

        dataframe.to_excel(name_excel_file_path, index=False)
        