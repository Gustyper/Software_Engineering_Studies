from abc import ABC, abstractmethod
from typing import Optional, Dict, List


class strategy(ABC):
    @abstractmethod
    def exec(self, input): ...

class estrategia_exemplo1(strategy):
    def exec(self, input):
        print(f"Executando {self.__class__.__name__} com o input {input}")

class estrategia_exemplo2(strategy):
    def exec(self, input):
        print(f"Executando {self.__class__.__name__} com o input {input}")


class template(ABC):
    def run_template(self):
        self.exec_1()
        self.exec_2()
        self.exec_3()
        self.exec_optional()

    @abstractmethod
    def exec_1(self): ...

    @abstractmethod
    def exec_2(self): ...

    @abstractmethod
    def exec_3(self): ...

    def exec_optional(self): 
        print("Esse é opcional")

class template_concreto(template):
    def __init__(self, strategy: strategy):
        self._strategy = strategy

    def set_strategy(self, strategy: strategy):
        self._strategy = strategy

    def exec_1(self): 
        print("Parte 1 do Pipeline")

    def exec_2(self): 
        print("Parte 2 do pipeline")
        self._strategy.exec(self.__class__.__name__)

    def exec_3(self): 
        print("Parte 3 do pipeline")


strat1 = estrategia_exemplo1()
strat2 = estrategia_exemplo2()

pipeline = template_concreto(strat1)

pipeline.run_template()


print("\n\n")
###############################################3


class handler(ABC):
    def __init__(self, sucessor = None):
        self._sucessor: Optional[handler] = sucessor

    @abstractmethod
    def handle(self, objeto) -> None: ...

class handler_texto_lower(handler):
    def handle(self, texto: str):
        if texto.islower():
            print("handler lower tratou")

        if self._sucessor:
            self._sucessor.handle(texto) 

class handler_texto_upper(handler):
    def handle(self, texto: str):
        if texto.isupper():
            print("handler upper tratou")
            # Eu poderia retornar depois de cada handler. Daí seria "o primeiro handler que deu match já resolve"

        if self._sucessor:
            self._sucessor.handle(texto) 

class handler_texto_final(handler):
    def handle(self, texto: str):
        print("handler final tratou")

        if self._sucessor:
            self._sucessor.handle(texto) 

chain = handler_texto_lower(handler_texto_upper(handler_texto_final()))

palavra = "TESTE"

chain.handle(palavra)

print("\n\n")
###############################################3

class EditorDeTexto():
    def __init__(self, texto: str):
        self._texto = texto

    def input(self, input):
        self._texto += input

    def apagar(self, apagar):
        self._texto = self._texto.replace(apagar, "")

class command(ABC):
    @abstractmethod
    def exec(self): ...

    @abstractmethod
    def undo(self): ...

class InputCommand(command):
    def __init__(self, editordetexto: EditorDeTexto, texto: str) -> None:
        self._texto = texto
        self._editor = editordetexto

    def exec(self):
        self._editor.input(self._texto)

    def undo(self):
        self._editor.apagar(self._texto)

class ApagarCommand(command):
    def __init__(self, editordetexto: EditorDeTexto, texto: str) -> None:
        self._texto = texto
        self._editor = editordetexto

    def exec(self):
        self._editor.apagar(self._texto)

    def undo(self):
        self._editor.input(self._texto)

class MacroCommand(command):
    def __init__(self, editordetexto: EditorDeTexto, commandos: List[command]) -> None:
        self._commands = commandos

    def exec(self):
        for cmd in self._commands:
            cmd.exec()

    def undo(self):
       for cmd in reversed(self._commands):
            cmd.undo()

class commandInvoker():
    def __init__(self): 
        self._history: List[command] = []
        self._redo_stack: List[command] = []

    def execute_command(self, command: command) -> None:
        command.exec()
        self._history.append(command)
        self._redo_stack.clear()
        
    def undo(self) -> None:
        if not self._history:
            print("Data a desfazer")
            return
        last_command = self._history.pop()
        last_command.undo()
        self._redo_stack.append(last_command)
        
    def redo(self) -> None:
        if not self._redo_stack:
            print("Nada a refazer")
            return
        command = self._redo_stack.pop()
        command.exec()
        self._history.append(command)
        
    def show_history(self) -> None:
        for i, cmd in enumerate(self._history, start = 1):
            print(f"{i}: {cmd.__class__.__name__}")


editor = EditorDeTexto("Texto inicial ")

comando_1 = InputCommand(editor, " outro texto")
comando_2 = ApagarCommand(editor, "Texto ")

envocador = commandInvoker()

envocador.execute_command(comando_1)

print(editor._texto)
