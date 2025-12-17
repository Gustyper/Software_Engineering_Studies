from __future__ import annotations
from abc import ABC, abstractmethod
import random

class DataPipeline(ABC): 
    # Com esse método evitamos que o run_pipeline fique ENORME e não dê pra reaproveitar nada
    # E qualquer coisa podemos ter mais de um pipeline reaproveitando partes que são iguais
    
    def run_pipeline(self, source: str) -> None: 
        self.load_data(source)
        self.hook_after_load()
        
        self.clean_data()
        self.hook_after_clean()
        
        self.analyse_data()
        self.report_results()
        
    # Métodos obrigatórios
    @abstractmethod
    def load_data(self, source: str) -> None: pass
    
    @abstractmethod
    def clean_data(self) -> None: pass

    @abstractmethod
    def analyse_data(self) -> None: pass

    @abstractmethod
    def report_results(self) -> None: pass

    # Métodos opcionais
    
    def hook_after_load(self): pass

    def hook_after_clean(self): pass
    
class SaleAnalysisPipeline(DataPipeline):
    
    def load_data(self, source: str) -> None:
        print(f"Carregando os dados de vendas de {source}")
        
    def clean_data(self) -> None:
        print("Limpando os dados de vendas...")
        
    def analyse_data(self) -> None: 
        print("Analisando os dados de vendas...")
        
    def report_results(self) -> None:
        print("Relatório final de vendas por categoria...")
        
    def hook_after_load(self) -> None:
        print("Pré-visualização para AED dos dados de venda...")
        
class FraudDetectionPipeline(DataPipeline):
    
    def load_data(self, source: str) -> None:
        print(f"Carregando transações de {source}")
        
    def clean_data(self) -> None:
        print("Filtrando Transações inválidas...")
        
    def analyse_data(self) -> None: 
        print("Detectando fraudes...")
        
    def report_results(self) -> None:
        print("Relatório final de transações suspeitas...")
        
    def hook_after_load(self) -> None:
        print("Gerar relatório de transações válidas...")
        

pipeline_1 = SaleAnalysisPipeline()
pipeline_1.run_pipeline("data-csv")

print("\n")

pipeline_2 = FraudDetectionPipeline()
pipeline_2.run_pipeline("transactions.csv")



###############################################################################


class Handler(ABC):
    def __init__(self, sucessor = None):
        """lindo"""
        self._sucessor = sucessor
        
    @abstractmethod
    def handle(self, request: str) -> str: pass


class LowerCaseHandler(Handler):
    def handle(self, request: str) -> str:
        if request.islower():
            return f"LowerCaseHandler tratou \"{request}\""
        elif self._sucessor:
            return self._sucessor.handle(request)
        else:
            return f"LowerCaseHandler não conseguiu tratar \"{request}\""
        
class UpperCaseHandler(Handler):
    def handle(self, request: str) -> str:
        if request.isupper():
            return f"UpperCaseHandler tratou \"{request}\""
        elif self._sucessor:
            return self._sucessor.handle(request)
        else:
            return f"UpperCaseHandler não conseguiu tratar \"{request}\""
        
class DefaultCaseHandler(Handler):
    def handle(self, request: str) -> str:
        return f"Nenhuma regra conseguiu tratar \"{request}\""
    
handler_chain = LowerCaseHandler(UpperCaseHandler(DefaultCaseHandler()))

test_inputs = ["abc", "XYZ", "123", "EMAp"]
for item in test_inputs:
    print(handler_chain.handle(item))
    
    
