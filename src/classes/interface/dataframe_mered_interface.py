from abc import ABC, abstractmethod

class DataframeMergedInterface(ABC):

    @abstractmethod
    def dataframe_merged(self) -> None:
        pass