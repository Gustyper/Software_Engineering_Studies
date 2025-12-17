from adapters import CSVAdapter, APIAdapter, ObjectAdapter
from dataIterator import Iterator

class Objeto():
    def __init__(self, value, next = None):
        self._value = value
        self.next = next

    def get_value(self):
        return self._value
    
dados_csv = CSVAdapter("teste.csv").get_data()
dados_api = APIAdapter().get_data()

df_objeto3 = Objeto("coco")
df_objeto2 = Objeto(2, df_objeto3)
df_objeto1 = Objeto(1, df_objeto2)

dados_objeto = ObjectAdapter(df_objeto1).get_data()

for i in Iterator(dados_csv):
    print(i)
print("-")

for i in Iterator(dados_api):
    print(i)
print("-")

for i in Iterator(dados_objeto):
    print(i)
print("-")
