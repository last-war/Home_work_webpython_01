import pickle
from collections import UserDict
from abc import ABC, abstractmethod

class AbcDict(ABC):
    @abstractmethod
    def save(self):
        ...

    @abstractmethod
    def load(self):
        ...

class MainBookRecord(ABC):
    @abstractmethod
    def change_field(self, field_name, old_value, new_value):
        pass

    @abstractmethod
    def __str__(self):
        pass


class MainBook(AbcDict, UserDict):
    """Parent class for notebook and contact book"""

    def save(self, fh):
        """Saving data to file"""
        with open(fh, 'wb') as file:
            pickle.dump(self.data, file)

    def load(self, fh):
        """Load data from file"""
        try:
            with open(fh, 'rb') as file:
                self.data = pickle.load(file)

        except FileNotFoundError:
            pass

