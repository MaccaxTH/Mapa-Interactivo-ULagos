# Transiciones

define custom_dissolve = Dissolve(0.5)

# PAPU INICIO

screen pantallainicio():

    add "PantallaDeInicio.png"

    imagebutton:
        xpos 1355
        ypos 360
        idle "PantallaDeInicioCreditos.png"
        hover "PantallaDeInicioCreditos2.png"
        action [With(custom_dissolve), Jump("creditos1")]
        activate_sound "audio/click.mp3"

    imagebutton:
        xpos 1302
        ypos 455
        idle "PantallaDeInicioMapa.png"
        hover "PantallaDeInicioMapa2.png"
        action [With(custom_dissolve), Jump("mapabase")]
        activate_sound "audio/click.mp3"

    imagebutton:
        xpos 1355
        ypos 605
        idle "PantallaDeInicioImagenes.png"
        hover "PantallaDeInicioImagenes2.png"
        action [With(custom_dissolve), Jump("imagenes1")]
        activate_sound "audio/click.mp3"

    imagebutton:
        xpos 1355
        ypos 850
        idle "PantallaDeInicioSalir.png"
        hover "PantallaDeInicioSalir2.png"
        action [With(fade), Quit(confirm=False)]
        activate_sound "audio/click.mp3"
screen mapabase():
    imagemap:
        ground "Mapa.png"
        hotspot(922, 384, 38, 36) action Jump("edificiobiblioteca1"):
            activate_sound "audio/click.mp3"
        hotspot(806, 411, 35, 35) action Jump("vicerrectoria1"):
            activate_sound "audio/click.mp3"
        hotspot(349, 350, 40, 41) action Jump("gimnasios1"):
            activate_sound "audio/click.mp3"
        hotspot(550, 305, 37, 36)action Jump("laboratorios1"):
            activate_sound "audio/click.mp3"
        hotspot(509, 222, 39, 40)action Jump("edificiosalud1"):
            activate_sound "audio/click.mp3"
        hotspot(343, 185, 38, 35)action Jump("centroacondicionamientofisico1"):
            activate_sound "audio/click.mp3"
        hotspot(560, 406, 39, 31)action Jump("edificioadministrativo1"):
            activate_sound "audio/click.mp3"
        hotspot(211, 689, 39, 36)action Jump("tallermultidisciplinario1"):
            activate_sound "audio/click.mp3"
        hotspot(162, 360, 38, 39)action Jump("salondefisica1"):
            activate_sound "audio/click.mp3"
        hotspot(998, 875, 42, 41)action Jump("centroimar1"):
            activate_sound "audio/click.mp3"
        hotspot(442, 1002, 280, 74)action [Hide("mapabase"), With(dissolve)]:
            activate_sound "audio/click.mp3"
        hotspot(821, 294, 38, 38)action Jump("edificioprincipal1"):
            activate_sound "audio/click.mp3"
        imagebutton:
            xanchor 0.9
            yanchor 0.1
            xpos 0.37
            ypos 0.92
            idle "Inicio.png"
            hover"Iniciopapu.png"
            action [Hide("mapabase"), With(dissolve)]
            activate_sound "audio/click.mp3"
screen vicerrectoria():
    imagemap:
        ground "Edificio Vicerrectoría.png"
    imagebutton:
        xanchor 0.9
        yanchor 0.1
        xpos 0.988
        ypos 0.009
        idle "flecha1.png"
        hover"flecha2.png"
        action [Hide("vicerrectoria"), With(dissolve)]
        activate_sound "audio/click.mp3"
screen centroimar():
    imagemap:
        ground "Centro I-Mar.png"
    imagebutton:
        xanchor 0.9
        yanchor 0.1
        xpos 0.988
        ypos 0.009
        idle "flecha1.png"
        hover"flecha2.png"
        action [Hide("centroimar"), With(dissolve)]
        activate_sound "audio/click.mp3"
screen edificiosalud():
    imagemap:
        ground "Edificio de Salud.png"
    imagebutton:
        xanchor 0.9
        yanchor 0.1
        xpos 0.988
        ypos 0.009
        idle "flecha1.png"
        hover"flecha2.png"
        action [Hide("edificiosalud"), With(dissolve)]
        activate_sound "audio/click.mp3"
screen tallermultidisciplinario():
    imagemap:
        ground "Edificio Taller Multidisciplinario.png"
    imagebutton:
        xanchor 0.9
        yanchor 0.1
        xpos 0.988
        ypos 0.009
        idle "flecha1.png"
        hover"flecha2.png"
        action [Hide("tallermultidisciplinario"), With(dissolve)]
        activate_sound "audio/click.mp3"
transform panel_entra: # Esto es para definir la animacion, es un paneo desde la izquierda
    xpos -1456 ypos 0
    linear 0.5 xpos 0

screen centroacondicionamientofisico():
    imagemap:  
        ground "Centro de Acondicionamiento Físico.png"
    
    frame at panel_entra:
        background None
        xsize 1456
        ysize 816
        xpos 0
        ypos 0
        add "Centro de Acondicionamiento Físico(1).png"  # Aquí es la imagen que se anima
    
    imagebutton:
        idle Solid("#0000")
        hover Solid("#FFFFFF33")  
        xpos 0.04
        ypos 0.25
        xsize 180
        ysize 120
        action OpenURL("https://www.instagram.com/p/C-vAUSoOXvp/?hl=es-la")
        activate_sound "audio/click.mp3"
    
    imagebutton:
        xanchor 0.9
        yanchor 0.1
        xpos 0.988
        ypos 0.009
        idle "flecha1.png"
        hover "flecha2.png"
        action [Hide("centroacondicionamientofisico"), With(dissolve)]
        activate_sound "audio/click.mp3"
screen edificioadministrativo():
    imagemap:
        ground "Edificio Administrativo del Campus.png"
            #activate_sound "audio/click.mp3"
    imagebutton:
        xanchor 0.9
        yanchor 0.1
        xpos 0.988
        ypos 0.009
        idle "flecha1.png"
        hover"flecha2.png"
        action [Hide("edificioadministrativo"), With(dissolve)]
        activate_sound "audio/click.mp3"
screen edificiobiblioteca():
    imagemap:
        ground "Edificio Biblioteca.png"
    imagebutton:
        xanchor 0.9
        yanchor 0.1
        xpos 0.988
        ypos 0.009
        idle "flecha1.png"
        hover"flecha2.png"
        action [Hide("edificiobiblioteca"), With(dissolve)]
        activate_sound "audio/click.mp3"
screen gimnasios():
    imagemap:
        ground "Gimnasios.png"
    imagebutton:
        xanchor 0.9
        yanchor 0.1
        xpos 0.988
        ypos 0.009
        idle "flecha1.png"
        hover"flecha2.png"
        action [Hide("gimnasios"), With(dissolve)]
        activate_sound "audio/click.mp3"
screen laboratorios():
    imagemap:
        ground "Laboratorios.png"
    imagebutton:
        xanchor 0.9
        yanchor 0.1
        xpos 0.988
        ypos 0.009
        idle "flecha1.png"
        hover"flecha2.png"
        action [Hide("laboratorios"), With(dissolve)]
        activate_sound "audio/click.mp3"
screen salondefisica():
    imagemap:
        ground "Salon de Física.png"
    imagebutton:
        xanchor 0.9
        yanchor 0.1
        xpos 0.988
        ypos 0.009
        idle "flecha1.png"
        hover"flecha2.png"
        action [Hide("salondefisica"), With(dissolve)]
        activate_sound "audio/click.mp3"
screen creditos():
    imagemap:
        ground "Creditos.png"
    imagebutton:
        xanchor 0.9
        yanchor 0.1
        xpos 0.988
        ypos 0.009
        idle "flecha1.png"
        hover"flecha2.png"
        action [Hide("creditos"), With(dissolve)]
        activate_sound "audio/click.mp3"
    imagebutton:
        xanchor 0.9
        yanchor 0.1
        xpos 1.0
        ypos 0.1
        idle "GitHubIcon.png"
        hover "GitHubIconClick.png"
        action OpenURL("https://github.com/MaccaxTH/Mapa-Interactivo-ULagos.git")
        activate_sound "audio/click.mp3"
screen edificioprincipal():
    imagemap:
        ground "Edificio Principal_ Mapa.png"
        hotspot(920, 561, 41, 41)action Jump("pasillo1")
        hotspot(725, 466, 42, 40)action Jump("casino1")
        hotspot(583, 465, 39, 41)action Jump("superior1")
        hotspot(379, 469, 40, 37)action Jump("estarII1")
        
    imagebutton:
        xanchor 0.9
        yanchor 0.1
        xpos 0.988
        ypos 0.009
        idle "flecha1.png"
        hover"flecha2.png"
        action [Hide("edificioprincipal"), With(dissolve)]
        activate_sound "audio/click.mp3"
    
screen casino():
    imagemap:
        ground "Edificio Principal_ Casino.png"
    imagebutton:
        xanchor 0.9
        yanchor 0.1
        xpos 0.988
        ypos 0.009
        idle "flecha1.png"
        hover"flecha2.png"
        action [Hide("casino"), With(dissolve)]
        activate_sound "audio/click.mp3"
screen superior():
    imagemap:
        ground "Edificio Principal_ Pisos Superiores.png"
    imagebutton:
        xanchor 0.9
        yanchor 0.1
        xpos 0.988
        ypos 0.009
        idle "flecha1.png"
        hover "flecha2.png"
        action [Hide("superior"), With(dissolve)]
        activate_sound "audio/click.mp3"
screen estarII():
    imagemap:
        ground "Edificio Principal_ Sala de Estar 2.png"
    imagebutton:
        xanchor 0.9
        yanchor 0.1
        xpos 0.988
        ypos 0.009
        idle "flecha1.png"
        hover "flecha2.png"
        action [Hide("estarII"), With(dissolve)]
        activate_sound "audio/click.mp3"
screen pasillo():
    imagemap:
        ground "Edificio Principal_ Pasillo Principal.png"
    imagebutton:
        xanchor 0.9
        yanchor 0.1
        xpos 0.988
        ypos 0.009
        idle "flecha1.png"
        hover "flecha2.png"
        action [Hide("pasillo"), With(dissolve)]
        activate_sound "audio/click.mp3"
screen imagenes1():
    imagemap:
        ground "imagenes.png"
    imagebutton:
        xanchor 0.9
        yanchor 0.1
        xpos 0.56
        ypos 0.92
        idle "Inicio.png"
        hover "InicioPapu.png" 
        action [Hide("imagenes1"), With(dissolve)]     
        activate_sound "audio/click.mp3"