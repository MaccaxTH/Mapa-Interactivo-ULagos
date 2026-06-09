# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define e = Character("Eileen")

# Transiciones 

define custom_fade = Fade(0.1, 0.2, 0.1) # Lo que tarda en llegar a negro / Lo que se mantiene / Volver a normal

define custom_dissolve = Dissolve(0.5)

# El juego comienza aquí.
label main_menu:
    return
    $ _skipping = False 
label start:
    show screen pantallainicio with fade
    $ renpy.pause (hard=True)
    $ _skipping = False
label mapabase:
    show screen mapabase with custom_dissolve
    $ renpy.pause (hard=True)
    $ _skipping = False
label vicerrectoria1:
    show screen vicerrectoria with custom_dissolve
    $ renpy.pause (hard=True)
    $ _skipping = False
label edificiobiblioteca1:
    show screen edificiobiblioteca with custom_dissolve
    $ renpy.pause (hard=True)
    $ _skipping = False
label gimnasios1:
    show screen gimnasios with custom_dissolve
    $ renpy.pause (hard=True)
    $ _skipping = False
label laboratorios1:
    show screen laboratorios with custom_dissolve
    $ renpy.pause (hard=True)
    $ _skipping = False
label edificiosalud1:
    show screen edificiosalud with custom_dissolve
    $ renpy.pause (hard=True)
    $ _skipping = False
label centroacondicionamientofisico1:
    show screen centroacondicionamientofisico with custom_dissolve
    $ renpy.pause (hard=True)
    $ _skipping = False
label edificioadministrativo1:
    show screen edificioadministrativo with custom_dissolve
    $ renpy.pause (hard=True)
    $ _skipping = False
label tallermultidisciplinario1:
    show screen tallermultidisciplinario with custom_dissolve
    $ renpy.pause (hard=True)
    $ _skipping = False
label salondefisica1:
    show screen salondefisica with custom_dissolve
    $ renpy.pause (hard=True)
    $ _skipping = False
label centroimar1:
    show screen centroimar with custom_dissolve
    $ renpy.pause (hard=True)
    $ _skipping = False
label creditos1:
    show screen creditos with custom_dissolve
    $ renpy.pause (hard=True)
    $ _skipping = False
label edificioprincipal1:
    show screen edificioprincipal with custom_dissolve
    $ renpy.pause (hard=True)
    $ _skipping = False
label casino1:
    show screen casino with custom_dissolve
    $ renpy.pause (hard=True)
    $ _skipping = False
label superior1:
    show screen superior with custom_dissolve
    $ renpy.pause (hard=True)
    $ _skipping = False
label estarII1:
    show screen estarII with custom_dissolve
    $ renpy.pause (hard=True)
    $ _skipping = False
label pasillo1:
    show screen pasillo with custom_dissolve
    $ renpy.pause (hard=True)
    $ _skipping = False
label imagenes1:
    show screen imagenes
    $ renpy.pause (hard=True)
    $ _skipping = False


