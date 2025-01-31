from abc import ABC, abstractmethod
from pandas import DataFrame


class VendasInterface(ABC):

    @abstractmethod
    def extract_data_cpf_total_chave(self) -> DataFrame:
        pass
