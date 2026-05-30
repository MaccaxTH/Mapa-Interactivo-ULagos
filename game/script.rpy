# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define e = Character("Eileen")


# El juego comienza aquí.
label main_menu:
    return
    $ _skipping = False 
label start:
    show screen pantallainicio
    $ renpy.pause (hard=True)
    $ _skipping = False
label mapabase:
    show screen mapabase
    $ renpy.pause (hard=True)
    $ _skipping = False
label vicerrectoria1:
    show screen vicerrectoria
    $ renpy.pause (hard=True)
    $ _skipping = False
label edificiobiblioteca1:
    show screen edificiobiblioteca
    $ renpy.pause (hard=True)
    $ _skipping = False
label gimnasios1:
    show screen gimnasios
    $ renpy.pause (hard=True)
    $ _skipping = False
label laboratorios1:
    show screen laboratorios
    $ renpy.pause (hard=True)
    $ _skipping = False
label edificiosalud1:
    show screen edificiosalud
    $ renpy.pause (hard=True)
    $ _skipping = False
label centroacondicionamientofisico1:
    show screen centroacondicionamientofisico
    $ renpy.pause (hard=True)
    $ _skipping = False
label edificioadministrativo1:
    show screen edificioadministrativo
    $ renpy.pause (hard=True)
    $ _skipping = False
label tallermultidisciplinario1:
    show screen tallermultidisciplinario
    $ renpy.pause (hard=True)
    $ _skipping = False
label salondefisica1:
    show screen salondefisica
    $ renpy.pause (hard=True)
    $ _skipping = False
label centroimar1:
    show screen centroimar
    $ renpy.pause (hard=True)
    $ _skipping = False



