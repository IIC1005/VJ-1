import random

import pygame

BUGpng = pygame.image.load("assets/bug.png")
BUGpng_scaled = pygame.transform.scale(BUGpng, (64, 64))


class Enemy(pygame.sprite.Sprite):
    def __init__(self, screen, *groups):

        # ? super().__init__() llama al constructor de la clase padre (Sprite) para inicializar el objeto correctamente
        # ? Aprovechamos de pasarle los grupos a los que pertenece para que pygame lo maneje automáticamente
        super().__init__(*groups)

        self.image = BUGpng_scaled
        self.rect = self.image.get_rect(
            center=(
                # La coordenada [x] (posición horizontal) esta a la derecha de la pantalla, fuera de la vista
                screen.get_width() + 100,
                # La coordenada [y] (posición vertical) es aleatoria dentro de los margenes de la pantalla
                random.randint(0, screen.get_height()),
            )
        )
        # La velocidad también es aleatoria
        self.speed = random.randint(3, 5)

    def update(self):
        # TODO (2.5): Mover a los enemigos

        # TODO (2.5): Destruir a los enemigos
        ...
