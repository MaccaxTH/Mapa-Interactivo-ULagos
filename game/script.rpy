# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define e = Character("Eileen")


# El juego comienza aquí.

label start:
    show screen pantallainicio
    $ renpy.pause (hard=True)
label mapabase:
    show screen mapabase
    $ renpy.pause (hard=True)
    
label vicerrectoria:
    show screen vicerrectoria
    $ renpy.pause (hard=True)

