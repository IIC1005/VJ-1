if __name__ == "__main__": # Solo para que no ejecutes este archivo
    import sys
    print(
        "\033[38;2;255;0;0mESTE MODULO NO DEBE EJECUTARSE. EJECUTAR main.py\033[0m\n"
        * 3
    )
    sys.exit()

import pygame

from pygame.locals import (K_ESCAPE, KEYDOWN, QUIT)

from elements.player import Player

from elements.enemy import Enemy


"""
Este es el modulo game_scene, aqui se encuentra 
la escena en donde ocurre nuestro juego
"""


def gameloop(screen):
    ''' Definimos el fondo de nuestra escena'''
    # POR HACER (2.4): añadir fondo del display

    ''' Preparamos el gameloop '''
    # POR HACER (2.8): Crear el reloj del juego
    clock = None

    # POR HACER (2.7): Generador de enemigos
    ADDENEMY = None

    # POR HACER (2.6): Creamos la instancia de jugador
    player = None

    # POR HACER (2.6): Creamos los grupos de sprites
    enemies = None
    all_sprites = None

    ''' hora de hacer el gameloop '''
    # variable booleana para manejar el loop
    running = True

    # GAME LOOP: loop principal del juego
    while running:
        # POR HACER (2.4): Dibujar la imagen en la ventana

        # iteramos sobre cada evento en la cola
        for event in pygame.event.get():
            # se presiono una tecla?
            if event.type == KEYDOWN:
                # era la tecla de escape? -> entonces terminamos
                if event.key == K_ESCAPE:
                    running = False

            # fue un click al cierre de la ventana? -> entonces terminamos
            elif event.type == QUIT:
                running = False

            # POR HACER (2.7): Generar enemigos


        # POR HACER (2.6): Actualizar los sprites

        # POR HACER (2.6): Dibujar los sprites

        # POR HACER (2.9): Colisiones

        # POR HACER (2.4): Actualizar la ventana con lo dibujado

        # POR HACER (2.8): Controlar la velocidad de fotogramas