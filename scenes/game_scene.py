if __name__ == "__main__":  # ! Solo para que no ejecutes este archivo
    import sys

    print(
        "\033c"
        + "\033[38;2;255;0;0mESTE ARCHIVO NO DEBE EJECUTARSE. EJECUTAR main.py\033[0m\n"
        * 3
    )
    sys.exit()

import pygame
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT


def gameloop(screen):
    # * Preparamos la escena de juego, cargando los elementos que se van a usar en el loop principal

    # TODO (2.4): Añadir fondo del display
    background_image = None

    # TODO (2.6): Crear la instancia de jugador
    player = None

    # TODO (2.6): Crear los grupos de sprites
    enemies = None
    all_sprites = None

    # TODO (2.7): Crear el generador de enemigos
    ADDENEMY = None

    # TODO (2.8): Crear el reloj del juego
    clock = None

    running = True  # variable booleana para manejar el loop

    # * Loop principal del juego, todo lo que ocurre en el juego se hace dentro de este loop
    while running:
        # TODO (2.4): Dibujar la imagen de fondo en la ventana

        # Iteramos sobre cada evento en la cola
        for event in pygame.event.get():
            if event.type == KEYDOWN:  # se presiono una tecla?
                if event.key == K_ESCAPE:  # era la tecla de escape?
                    running = False  # terminamos el loop

            elif event.type == QUIT:  # fue un click al cierre de la ventana?
                running = False  # terminamos el loop

            # TODO (2.7): Generar enemigos

        # TODO (2.6): Actualizar el estado interno de los sprites (posiciones, etc)

        # TODO (2.6): Dibujar los sprites actualizados en la ventana

        # TODO (2.9): Calcular colisiones entre jugador y enemigos

        # TODO (2.4): Actualizar la ventana para reflejar todos los cambios

        # TODO (2.8): Controlar la velocidad de fotogramas
