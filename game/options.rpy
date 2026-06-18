'''
Todo este codigo es el codigo base para el funcionamiento normal del motor de Ren'py, no afecta la funcionalidad ni
el aspecto del mapa interactivo, pero son necesarios de mantener para que Ren'py pueda funcionar y no crashee, aunque
particularmente acá sí hay codigo que se usó para el mapa interactivo en sí, los "##" indican estos.
'''


## Nombre del programa en forma legible. 

define config.name = _("Mapa Interactivo ULagos")


## Determina si el título dado más arriba se muestra en el menú principal.

define gui.show_name = True


## Versión

define config.version = "1.0"

define gui.about = _p("""
""")


## Nombre breve del programa para ejecutables y directorios en la distribución.

define build.name = "MapaInteractivoULagos"


define config.has_sound = True
define config.has_music = True
define config.has_voice = True




define config.enter_transition = dissolve
define config.exit_transition = dissolve


define config.intra_transition = dissolve



define config.after_load_transition = None


define config.end_game_transition = None


define config.window = "auto"



define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


default preferences.text_cps = 0


default preferences.afm_time = 15



define config.save_directory = "MapaInteractivoULagos-1778603884"

## El icono mostrado en la barra de tareas.

define config.window_icon = "gui/window_icon.png"


init python:

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    build.documentation('*.html')
    build.documentation('*.txt')

define config.keymap = {k: v for k, v in config.keymap.items() if k != 'game_menu'}

#icono del programa

define config.window_icon = "iconopapu.png"