from player import *

app = Application()

Spotify = app.new_player("Spotify")

Radioactive = Spotify.novaMusica("Radioactive")
betano = Spotify.novoAnuncio(30)

Radioactive.ouvir()

Spotify = app.new_player("Spotify")

print("Ain eu quero reimportar tudo")

import importlib

importlib.reload(player)


