import flet as ft
import pygame
import random

def main(page: ft.Page):
    page.title = "Encuesta MDS"
    page.window.width = 400
    page.window.height = 300
    page.window.resizable = False

    margen_inferior = 95
    margen_lateral = 100
    movimiento_minimo = 50

    def mover_boton_no(e):
        max_top = page.height - margen_inferior
        max_left = page.width - margen_lateral
    
        top_actual = btn_no.top
        left_actual = btn_no.left
    
        nuevo_top = top_actual + random.randint(-movimiento_minimo, movimiento_minimo)
        nuevo_left = left_actual + random.randint(-movimiento_minimo, movimiento_minimo)
    
        # Asegúrate de que el botón no se salga de los límites
        if nuevo_top < 0:
            nuevo_top = 0
        elif nuevo_top > max_top:
            nuevo_top = max_top
    
        if nuevo_left < 0:
            nuevo_left = 0
        elif nuevo_left > max_left:
            nuevo_left = max_left
    
        btn_no.top = nuevo_top
        btn_no.left = nuevo_left
        page.update()

    def mostrar_respuesta(e):
        pygame.init()
        screen = pygame.display.set_mode((600, 400))
        pygame.display.set_caption("Imagen Rotando")

        imagen = pygame.image.load("C:\\Users\\Cristian\\Desktop\\xd\\xd.jpg")
        imagen = pygame.transform.scale(imagen, (400, 400)) 
        rect = imagen.get_rect(center=(300, 200))

        angulo = 0
        reloj = pygame.time.Clock()

        pygame.mixer.music.load("C:\\Users\\Cristian\\Desktop\\xd\\xd.mp3")
        pygame.mixer.music.play(-1) 

        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    return

            angulo += 1
            imagen_rotada = pygame.transform.rotate(imagen, angulo)
            rect_rotado = imagen_rotada.get_rect(center=rect.center)

            screen.fill((0, 0, 0))
            screen.blit(imagen_rotada, rect_rotado.topleft)

            pygame.display.flip()
            reloj.tick(60)

    btn_si = ft.ElevatedButton("Sí😘", on_click=mostrar_respuesta, width=100)
    btn_no = ft.ElevatedButton("No👌", width=100, on_hover=mover_boton_no)

    stack = ft.Stack(
        [
            btn_si,
            btn_no,
        ],
        width=400,
        height=300,
    )

    btn_si.top = 100
    btn_si.left = 50

    btn_no.top = 100
    btn_no.left = 200

    page.add(
        ft.Column(
            [
                ft.Text("¿Tú tienes papito ? uwu❤️❤️💕💕💕😍", 
                        size=30, 
                        weight=ft.FontWeight.BOLD),
                stack,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
        )
    )

ft.app(target=main)
