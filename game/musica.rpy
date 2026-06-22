# Variable para saber si la música está sonando o no
default musica_activada = False

init python:
    def toggle_musica():
        global musica_activada
        if musica_activada:
            renpy.music.stop(channel="music", fadeout=0.5)
            musica_activada = False
        else:
            renpy.music.play("menu.mp3", channel="music", loop=True, fadein=0.5)
            musica_activada = True

screen musica_listener():
    key "m" action Function(toggle_musica)

init python:
    config.overlay_screens.append("musica_listener")