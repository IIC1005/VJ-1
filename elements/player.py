import pygame
from pygame.locals import K_DOWN, K_LEFT, K_RIGHT, K_UP

JorgePNG = pygame.image.load("assets/JorgeVJ.png")
JorgePNG_scaled = pygame.transform.scale(JorgePNG, (80, 80))


class Player(pygame.sprite.Sprite):
    def __init__(self, screen, *groups):

        # ? super().__init__() llama al constructor de la clase padre (Sprite) para inicializar el objeto correctamente
        # ? Aprovechamos de pasarle los grupos a los que pertenece para que pygame lo maneje automáticamente
        super().__init__(*groups)

        self.image = JorgePNG_scaled
        self.rect = self.image.get_rect()
        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()

    def update(self, pressed_keys):
        # TODO (2.5): Mover a Jorge

        # TODO: Mantener a Jorge en Pantalla
        ...
