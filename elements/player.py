import pygame
from pygame.locals import K_DOWN, K_LEFT, K_RIGHT, K_UP

JorgePNG = pygame.image.load("assets/JorgeVJ.png")
JorgePNG_scaled = pygame.transform.scale(JorgePNG, (80, 80))


class Player(pygame.sprite.Sprite):
    def __init__(self, screen):

        # ? super().__init__() inicializa la clase padre (Sprite)
        super().__init__()

        self.image = JorgePNG_scaled
        self.rect = self.image.get_rect()
        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()

    def update(self, pressed_keys):
        # TODO (2.5): Mover a Jorge

        # TODO (2.5): Mantener a Jorge en Pantalla
        pass
