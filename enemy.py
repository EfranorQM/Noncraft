import pygame
from config.config import TAMANO_BLOQUE

class Enemy:
    """Clase que representa a un enemigo."""

    def __init__(self, x, y, tamaño):
        """Inicializa al enemigo en la posición dada."""
        self.rect = pygame.Rect(x, y, tamaño, tamaño)  # Rectángulo que representa al enemigo
        self.velocidad_x = 2  # Velocidad horizontal del enemigo (moverse de izquierda a derecha)
        self.movimiento_derecha = True  # Indica si el enemigo se está moviendo a la derecha
        self.limite_izquierdo = x - 100  # Límite izquierdo del movimiento
        self.limite_derecho = x + 100  # Límite derecho del movimiento

    def mover(self):
        """Mueve al enemigo de izquierda a derecha."""
        if self.movimiento_derecha:
            self.rect.x += self.velocidad_x
            if self.rect.x >= self.limite_derecho:  # Si llega al límite derecho, cambiar de dirección
                self.movimiento_derecha = False
        else:
            self.rect.x -= self.velocidad_x
            if self.rect.x <= self.limite_izquierdo:  # Si llega al límite izquierdo, cambiar de dirección
                self.movimiento_derecha = True

    def dibujar(self, pantalla):
        """Dibuja al enemigo en la pantalla."""
        pygame.draw.rect(pantalla, (255, 0, 0), self.rect)  # Dibuja el enemigo en rojo

    def verificar_colision(self, jugador):
        """Verifica si el enemigo colisiona con el jugador."""
        if self.rect.colliderect(jugador.rect):  # Si hay colisión con el jugador
            return True
        return False
