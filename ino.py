import pygame

class Ino(pygame.sprite.Sprite):
    """клас прибульця"""

    def __init__(self, screen):
        """ініціалізуєм і задаєм початкову позицію"""
        super(Ino, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/ino.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):
        """виводить прибульця на екран"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """переміщає прибульців"""
        self.y += 0.1
        self.rect.y = self.y