from abc import ABC, abstractmethod
from typing import Optional, Dict, Any

class Document(ABC):
    def __init__(self, name: str):
        self._name: str = name   #Type hinting é literalmnte uma hinting. O compilador ignora : str pra rodar, mas se eu fizer
                                 # name = 123, ele vai sublinhar falando que tá estranho
        self._is_open: bool = False
        self._snapshot: Optional[Dict[str, Any]] = None       # Pode ser NOne ou um Dict com chaves str e valores quiasquer

    @property                      # assim que funciona um getter
    def name (self) -> str:
        return self._name
    @name.setter                   # assim que funciona um setter
    def name(self, new_name) -> None:
        self._name = new_name

        # no fim, ambos permitem que usemos .name ou .name = tal.
        # quanto usar? quando queremos um controle secreto pra variável. 
        # Por exmeplo, como é nome podemos ter uma lógica que não permite números ou $%#! no meio

        # o getter pode ser algum atributo que nao necessariamente existe. ele pode ser calculado n ahora

    @abstractmethod
    def _open(self): ...
    
    @abstractmethod
    def _close(self): ...
    
    @abstractmethod
    def save(self): ...
    
    @abstractmethod
    def revert(self): ...
