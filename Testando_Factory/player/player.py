from abc import abstractmethod, ABC
from typing import Type, Any, Dict, Optional
from functools import wraps
from musicas import MusicaSpotify, MusicaYoutube, AnuncioSpotify, AnuncioYoutube, Musica, Anuncio

def singleton(func):
    _instance = None
    @wraps(func)
    def decorator(*args, **kwargs):
        nonlocal _instance
        if _instance == None:
            _instance = func(*args, **kwargs)
            print("Criou uma vez")
        else:
            print("Já foi criado")
        
        return _instance
    return decorator

class Player(ABC):
    @abstractmethod
    def novaMusica(self, nome: str) -> Musica: ...

    @abstractmethod
    def novoAnuncio(self, duracao: int) -> Anuncio: ...

class SpotifyPlayer(Player):
    _instance = None

    def __new__(cls):
        if cls._instance == None:
            print("Criando um SpotifyPlayer")
            cls._instance = super().__new__(cls)
        else:
            print("Já tem um player")
            
        return cls._instance

    def __init__(self):
        self.lista_musicas = []

    def novaMusica(self, nome):
        return MusicaSpotify(nome)
    
    def novoAnuncio(self, duracao):
        return AnuncioSpotify(duracao)
    
class YoutubePlayer(Player):
    _instance = None

    def __new__(cls):
        if cls._instance == None:
            print("Criando um YoutubePlayer")
            cls._instance = super().__new__(cls)
        else:
            print("Já tem um player")
            
        return cls._instance

    def __init__(self):
        self.lista_musicas = []

    def novaMusica(self, nome):
        return MusicaYoutube(nome)
    
    def novoAnuncio(self, duracao):
        return AnuncioYoutube(duracao)
    

class Application(ABC):
    def new_player(self, nome: str) -> Player:
        if nome == "Spotify": return SpotifyPlayer()
        elif nome == "Youtube": return YoutubePlayer()
        else: 
            print("Deu Ruim")
            raise ValueError()