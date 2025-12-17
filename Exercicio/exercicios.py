# Exercício 1: Implementação de um iterador

import pandas as pd
    
class Iterator:
    def __init__(self, data):
        self._index = 0
        self.data = data
        self.len = len(data)

    def __iter__(self):
        return self
    
    def __next__(self):
        if self._index >= self.len:
            print("Acabei de iterar por tudo")
            raise StopIteration 
        item = self.data[self._index]
        self._index += 1
        return item 
    
class CSVAdapter:
    def __init__(self, path: str):
        self._df = pd.read_csv(path)
    
    def __adapter__(self):
        addapted_data = []
        for i in range(len(self._df)):
            addapted_data.append(list(self._df.iloc[i]))
        return addapted_data
    
    def __iter__(self):
        return Iterator(self.__adapter__())
        
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
    
class ObjectAdapter:
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

class Objeto():
    def __init__(self, value, next = None):
        self._value = value
        self.next = next
        
    def get_value(self):
        return self._value



df_csv = CSVAdapter("teste.csv")
df_API = APIAdapter()

df_objeto3 = Objeto("coco")
df_objeto2 = Objeto(2, df_objeto3)
df_objeto1 = Objeto(1, df_objeto2)

for i in df_objeto1:
    print(i)
