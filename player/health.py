# health.py

import pygame

class HealthBar:
    def __init__(self, corazones, pantalla):
        """Inicializa la barra de vida con el número de corazones."""
        self.corazones = corazones
        self.pantalla = pantalla
        self.imagen_corazon = pygame.image.load('imagenes/corazon.png')  # Carga la imagen del corazón
        self.imagen_corazon = pygame.transform.scale(self.imagen_corazon, (40, 40))  # Ajustar tamaño a 40x40 px

    def dibujar(self):
        """Dibuja los corazones en la pantalla."""
        for i in range(self.corazones):
            x = 10 + i * 45  # Posición en X de cada corazón (separación de 45px)
            y = 10  # Posición en Y (siempre en la parte superior)
            self.pantalla.blit(self.imagen_corazon, (x, y))  # Dibuja el corazón en la pantalla
