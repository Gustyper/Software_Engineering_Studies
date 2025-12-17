import pandas as pd
from dataIterator import Iterator
 
class CSVAdapter:
    """
        Adaptador Noob
        Adapta os dados noobs
        ------
        parametros: caminho do csv
    """
    def __init__(self, path: str):
        self._df = pd.read_csv(path)
    
    def __adapter__(self):
        addapted_data = []
        for i in range(len(self._df)):
            addapted_data.append(list(self._df.iloc[i]))
        return addapted_data
    
    def __iter__(self):
        return Iterator(self.__adapter__())
    
    def get_data(self):
        return self.__adapter__()
        
class APIAdapter:
    def __init__(self):
        self._dict = self.__GetDataAPI__()
        self.addapted_data = []
        self.__adapter__()
    
    def __adapter__(self):
        addapted_data = []
        for value in self._dict.values():
            addapted_data.append(value)
        return addapted_data
    
    def __iter__(self):
        return Iterator(self.__adapter__())
    
    def __GetDataAPI__(self):
        return {1:"um", 2:"dois", 3:"tres", 4:"quatro", 5:"cinco"}
    
    def get_data(self):
        return self.__adapter__()
    
class ObjectAdapter():
    def __init__(self, start):
        self._start = start
        self.__adapter__()

    def get_value(self):
        return self._value

    def __adapter__(self):
        addapted_data = []
        next = self._start
        while next != None:
            addapted_data.append(next.get_value())
            next = next.next
        return addapted_data
    
    def __iter__(self):
        return Iterator(self.__adapter__())
    
    def get_data(self):
        return self.__adapter__()
    