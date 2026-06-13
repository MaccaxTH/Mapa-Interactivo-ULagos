# Animaciones y variables

define custom_dissolve = Dissolve(0.5) # Transición de disolver

transform panel_entra: # Esto es para definir la animacion, es un paneo desde la izquierda
    xpos -1456 ypos 0
    linear 0.5 xpos 0

transform panel_derecha: # Esto es para definir la animacion, es un paneo desde la derecha
    xpos 1456 ypos 0
    linear 0.5 xpos 0

transform panel_abajo: # Esto es para definir la animacion, es un paneo desde abajo
    xpos 0 ypos 1456
    linear 0.5 ypos 0

# PAPU INICIO

screen pantallainicio():
    frame:
        modal True
        xsize 1920
        ysize 1080
        align((0.5, 0.5))
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
    frame:
        modal True
        xsize 1920
        ysize 1080
        align((0.5, 0.5))
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
    frame:
        modal True
        xsize 1920
        ysize 1080
        align((0.5, 0.5))
    imagemap:
        ground "Edificio Vicerrectoría.png"
    
    frame at panel_entra:
        background None
        xsize 1456
        ysize 816
        xpos 0
        ypos 0
        add "Edificio Vicerrectoría(1).png"  # Aquí es la imagen que se anima
    imagebutton:
        xanchor 0.9
        yanchor 0.1
        xpos 0.988
        ypos 0.009
        idle "flecha1.png"
        hover"flecha2.png"
        action Hide("vicerrectoria")
        activate_sound "audio/click.mp3"
screen centroimar():
    frame:
        modal True
        xsize 1920
        ysize 1080
        align((0.5, 0.5))
    imagemap:
        ground "Centro I-Mar.png"
    
    frame at panel_entra:
        background None
        xsize 1456
        ysize 816
        xpos 0
        ypos 0
        add "Centro I-Mar(1).png"  # Aquí es la imagen que se anima
    imagebutton:
        xanchor 0.9
        yanchor 0.1
        xpos 0.988
        ypos 0.009
        idle "flecha1.png"
        hover"flecha2.png"
        action Hide("centroimar")
        activate_sound "audio/click.mp3"
screen edificiosalud():
    frame:
        modal True
        xsize 1920
        ysize 1080
        align((0.5, 0.5))
    imagemap:
        ground "Edificio de Salud.png"
    
    frame at panel_entra:
        background None
        xsize 1456
        ysize 816
        xpos 0
        ypos 0
        add "Edificio de Salud(1).png"  # Aquí es la imagen que se anima
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
    frame:
        modal True
        xsize 1920
        ysize 1080
        align((0.5, 0.5))
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

screen centroacondicionamientofisico():
    frame:
        modal True
        xsize 1920
        ysize 1080
        align((0.5, 0.5))
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
    frame:
        modal True
        xsize 1920
        ysize 1080
        align((0.5, 0.5))
    imagemap:
        ground "Edificio Administrativo del Campus.png"
            #activate_sound "audio/click.mp3"
    
    frame at panel_entra:
        background None
        xsize 1456
        ysize 816
        xpos 0
        ypos 0
        add "Edificio Administrativo del Campus(1).png"  # Aquí es la imagen que se anima
    imagebutton:
        xanchor 0.9
        yanchor 0.1
        xpos 0.988
        ypos 0.009
        idle "flecha1.png"
        hover"flecha2.png"
        action Hide("edificioadministrativo")
        activate_sound "audio/click.mp3"
screen edificiobiblioteca():
    frame:
        modal True
        xsize 1920
        ysize 1080
        align((0.5, 0.5))
    imagemap:
        ground "Edificio Biblioteca.png"
    
    frame at panel_entra:
        background None
        xsize 1456
        ysize 816
        xpos 0
        ypos 0
        add "Edificio Biblioteca(1).png"  # Aquí es la imagen que se anima
    imagebutton:
        xanchor 0.9
        yanchor 0.1
        xpos 0.988
        ypos 0.009
        idle "flecha1.png"
        hover"flecha2.png"
        action Hide("edificiobiblioteca")
        activate_sound "audio/click.mp3"
screen gimnasios():
    frame:
        modal True
        xsize 1920
        ysize 1080
        align((0.5, 0.5))
    imagemap:
        ground "Gimnasios.png"
    
    frame at panel_entra:
        background None
        xsize 1456
        ysize 816
        xpos 0
        ypos 0
        add "Gimnasios(1).png"  # Aquí es la imagen que se anima
    imagebutton:
        xanchor 0.9
        yanchor 0.1
        xpos 0.988
        ypos 0.009
        idle "flecha1.png"
        hover"flecha2.png"
        action Hide("gimnasios")
        activate_sound "audio/click.mp3"
screen laboratorios():
    frame:
        modal True
        xsize 1920
        ysize 1080
        align((0.5, 0.5))
    imagemap:
        ground "Laboratorios.png"
    
    frame at panel_entra:
        background None
        xsize 1456
        ysize 816
        xpos 0
        ypos 0
        add "Laboratorios(1).png"  # Aquí es la imagen que se anima
    imagebutton:
        xanchor 0.9
        yanchor 0.1
        xpos 0.988
        ypos 0.009
        idle "flecha1.png"
        hover"flecha2.png"
        action Hide("laboratorios")
        activate_sound "audio/click.mp3"
screen salondefisica():
    frame:
        modal True
        xsize 1920
        ysize 1080
        align((0.5, 0.5))
    imagemap:
        ground "Salon de Física.png"
    
    frame at panel_entra:
        background None
        xsize 1456
        ysize 816
        xpos 0
        ypos 0
        add "Salon de Física(1).png"  # Aquí es la imagen que se anima
    imagebutton:
        xanchor 0.9
        yanchor 0.1
        xpos 0.988
        ypos 0.009
        idle "flecha1.png"
        hover"flecha2.png"
        action Hide("salondefisica")
        activate_sound "audio/click.mp3"
screen creditos():
    frame:
        modal True
        xsize 1920
        ysize 1080
        align((0.5, 0.5))
    frame:
        modal True
        xsize 1920
        ysize 1080
        align((0.5, 0.5))
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
    frame:
        modal True
        xsize 1920
        ysize 1080
        align((0.5, 0.5))
    imagemap:
        ground "Edificio Principal_ Mapa.png"
        hotspot(997, 752, 34, 32)action Jump("pasillo1")
        hotspot(812, 693, 37, 38)action Jump("casino1")
        hotspot(755, 694, 41, 34)action Jump("superior1")
        hotspot(486, 674, 45, 35)action Jump("estarII1")
        
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
    frame:
        modal True
        xsize 1920
        ysize 1080
        align((0.5, 0.5))
    imagemap:
        ground "Edificio Principal_ Casino.png"
    frame at panel_derecha:
        background None
        xsize 1456
        ysize 816
        xpos 0
        ypos 0
        add "EdificioPrincipalCasinoPanel.png"  # Aquí es la imagen que se anima
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
    frame:
        modal True
        xsize 1920
        ysize 1080
        align((0.5, 0.5))
    imagemap:
        ground "EdificioPrincipalPisosSuperiores.png"
    frame at panel_abajo:
        background None
        xsize 1456
        ysize 816
        xpos 0
        ypos 0
        add "EdificioPrincipalPisosSuperioresPanel.png"  # Aquí es la imagen que se anima
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
    frame:
        modal True
        xsize 1920
        ysize 1080
        align((0.5, 0.5))
    imagemap:
        ground "EdificioPrincipalSaladeEstar2.png"
    frame at panel_abajo:
        background None
        xsize 1456
        ysize 816
        xpos 0
        ypos 0
        add "EdificioPrincipalSaladeEstar2Panel.png"  # Aquí es la imagen que se anima
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
    frame:
        modal True
        xsize 1920
        ysize 1080
        align((0.5, 0.5))
    imagemap:
        ground "EdificioPrincipalPasillo.png"
    frame at panel_derecha:
        background None
        xsize 1456
        ysize 816
        xpos 0
        ypos 0
        add "EdificioPrincipalPasilloPanel.png"  # Aquí es la imagen que se anima
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
    frame:
        modal True
        xsize 1920
        ysize 1080
        align((0.5, 0.5))
    imagemap:
        ground "imagenes.png"
        hotspot(123, 80, 369, 271)action Jump("imagenes1w")
        hotspot(558, 80, 367, 278)action Jump("imagenes2w")
        hotspot(988, 78, 374, 278)action Jump("imagenes3w")
        hotspot(1422, 84, 371, 274)action Jump("imagenes4w")
        hotspot(122, 400, 372, 276)action Jump("imagenes5w")
        hotspot(558, 401, 368, 272)action Jump("imagenes6w")
        hotspot(991, 401, 367, 275)action Jump("imagenes7w")
        hotspot(1425, 405, 365, 266)action Jump("imagenes8w")
        hotspot(125, 718, 370, 276)action Jump("imagenes9w")
        hotspot(558, 720, 368, 274)action Jump("imagenes10w")
        hotspot(991, 718, 369, 280)action Jump("imagenes11w")
        hotspot(1423, 721, 367, 276)action Jump("imagenes12w")
        

    imagebutton:
        xanchor 0.9
        yanchor 0.1
        xpos 0.56
        ypos 0.92
        idle "Inicio.png"
        hover "InicioPapu.png" 
        action [Hide("imagenes1"), With(dissolve)]     
        activate_sound "audio/click.mp3"
screen imagenes10():
    imagemap:
        ground"Mockup Imagenes (1).png"
        hotspot(1468, 80, 84, 79)action Hide("imagenes10")
screen imagenes20():
    imagemap:
        ground"Mockup Imagenes (2).png"
        hotspot(1468, 80, 84, 79)action Hide("imagenes20")
screen imagenes30():
    imagemap:
        ground"Mockup Imagenes (3).png"
        hotspot(1468, 80, 84, 79)action Hide("imagenes30")
screen imagenes40():
    imagemap:
        ground"Mockup Imagenes (4).png"
        hotspot(1468, 80, 84, 79)action Hide("imagenes40")
screen imagenes50():
    imagemap:
        ground"Mockup Imagenes (5).png"
        hotspot(1468, 80, 84, 79)action Hide("imagenes50")
screen imagenes60():
    imagemap:
        ground"Mockup Imagenes (6).png"
        hotspot(1468, 80, 84, 79)action Hide("imagenes60")
screen imagenes70():
    imagemap:
        ground"Mockup Imagenes (7).png"
        hotspot(1468, 80, 84, 79)action Hide("imagenes70")
screen imagenes80():
    imagemap:
        ground"Mockup Imagenes (8).png"
        hotspot(1468, 80, 84, 79)action Hide("imagenes80")
screen imagenes90():
    imagemap:
        ground"Mockup Imagenes (9).png"
        hotspot(1468, 80, 84, 79)action Hide("imagenes90")
screen imagenes100():
    imagemap:
        ground"Mockup Imagenes (10).png"
        hotspot(1468, 80, 84, 79)action Hide("imagenes100")
screen imagenes110():
    imagemap:
        ground"Mockup Imagenes (11).png"
        hotspot(1468, 80, 84, 79)action Hide("imagenes110")
screen imagenes120():
    imagemap:
        ground"Mockup Imagenes (12).png"
        hotspot(1468, 80, 84, 79)action Hide("imagenes120")