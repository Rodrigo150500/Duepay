from abc import ABC, abstractmethod
from pandas import DataFrame

class DuepayInterface(ABC):

    @abstractmethod
    def extract_total(self) -> DataFrame:
        pass
