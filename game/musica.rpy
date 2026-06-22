# Variable para saber si la música está sonando o no
default musica_activada = False

# Acción personalizada para togglear la música
init python:
    def toggle_musica():
        global musica_activada
        if musica_activada:
            renpy.stop_music(fadeout=0.5, channel="music")
            musica_activada = False
        else:
            renpy.music.play("menu.mp3", channel="music", loop=True, fadein=0.5)
            musica_activada = True

# Screen invisible que captura la tecla M en TODO el juego
screen musica_listener():
    key "m" action Function(toggle_musica)

# Esto hace que la screen esté activa siempre, en cualquier pantalla
init python:
    config.overlay_screens.append("musica_listener")