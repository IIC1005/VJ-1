import random

import pygame

BUGpng = pygame.image.load("assets/bug.png")
BUGpng_scaled = pygame.transform.scale(BUGpng, (64, 64))


class Enemy(pygame.sprite.Sprite):
    def __init__(self, screen):

        # ? super().__init__() inicializa la clase padre (Sprite)
        super().__init__()

        self.image = BUGpng_scaled
        self.rect = self.image.get_rect(
            center=(
                screen.get_width() + 100,
                random.randint(0, screen.get_height()),
            )
        )
        # La velocidad también es aleatoria
        self.speed = random.randint(3, 5)

    def update(self):
        # TODO (2.5): Mover a los enemigos

        # TODO (2.5): Destruir a los enemigos
        pass
