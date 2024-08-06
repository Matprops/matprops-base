from abc import ABC, abstractmethod

class DataModal(ABC):
    @abstractmethod
    def numpy_handler(self):
        """ To override """
        pass

    @abstractmethod
    def list_handler(self):
        """ To override """
        pass

    @abstractmethod
    def dict_handler(self):
        """ To override """
        pass

    @abstractmethod
    def dataframe_handler(self):
        """ To override """
        pass

    @abstractmethod
    def series_handler(self):
        """ To override """
        pass