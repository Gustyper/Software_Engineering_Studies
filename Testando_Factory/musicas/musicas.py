from abc import ABC, abstractmethod
from typing import Type, Any, Dict, Optional

class Musica(ABC):
    @abstractmethod
    def ouvir(self) -> None: ...

class Anuncio(ABC):
    @abstractmethod
    def pular(self) -> None: ...

class MusicaSpotify(Musica):
    def __init__(self, nome: str):
        self._nome : str = nome
        self._artistas : Type[Dict[str, Any]]

    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    def ouvir(self):
        print(f"Ouvindo {self._nome} no Spotify")

class MusicaYoutube(Musica):
    def __init__(self, nome: str):
        self._nome : str = nome
        self._artistas : Type[Dict[str, Any]]

    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    def ouvir(self):
        print(f"Ouvindo {self._nome} no Youtube")

class AnuncioSpotify(Anuncio):
    def __init__(self, duracao: int):
        self._duracao: int = duracao
        self._pulavel : Optional[bool]

    def pular(self):
        if self._pulavel: print(f"Pulando anuncio no Spotify")
        else: print("Impulavel")

class AnuncioYoutube(Anuncio):
    def __init__(self, duracao: int):
        self._duracao: int = duracao
        self._pulavel : Optional[bool]

    def pular(self):
        if self._pulavel: print(f"Pulando anuncio no Youtube")
        else: print("Impulavel")