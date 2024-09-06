import pygame
from config.config import TAMANO_BLOQUE, GRAVEDAD, VELOCIDAD_SALTO, AZUL_JUGADOR

class Player:
    """Clase que representa al jugador."""

    def __init__(self, x, y, tamaño):
        """Inicializa al jugador en la posición dada."""
        self.rect = pygame.Rect(x, y, tamaño, tamaño)  # Rectángulo que representa al jugador
        self.velocidad_y = 0  # Velocidad inicial en el eje Y
        self.velocidad_x = 0  # Velocidad inicial en el eje X, si se necesita
        self.en_suelo = False  # Indica si el jugador está tocando el suelo

    def manejar_movimiento(self, teclas, mapa):
        """Maneja el movimiento del jugador basado en las teclas presionadas."""
        movimiento_horizontal = 0

        # Movimiento izquierda (A o flecha izquierda)
        if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
            movimiento_horizontal = -5
        # Movimiento derecha (D o flecha derecha)
        if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
            movimiento_horizontal = 5

        # Aplicar el movimiento horizontal y verificar colisiones en X antes de mover
        self.mover_horizontal(movimiento_horizontal, mapa)

        # Movimiento hacia arriba (salto) solo si está en el suelo
        if (teclas[pygame.K_UP] or teclas[pygame.K_w]) and self.en_suelo:
            self.velocidad_y = VELOCIDAD_SALTO

    def mover_horizontal(self, movimiento_horizontal, mapa):
        """Aplica el movimiento horizontal y verifica las colisiones en el eje X."""
        # Aplicar movimiento horizontal temporalmente
        self.rect.x += movimiento_horizontal

        # Verificar si hay colisiones después de mover
        for fila in range(len(mapa)):
            for columna in range(len(mapa[fila])):
                if mapa[fila][columna] in (1, 2, 3, 4):  # Tierra, pasto, piedra o bloque inrompible
                    bloque_rect = pygame.Rect(columna * TAMANO_BLOQUE, fila * TAMANO_BLOQUE, TAMANO_BLOQUE, TAMANO_BLOQUE)

                    if self.rect.colliderect(bloque_rect):  # Si hay colisión horizontal
                        if movimiento_horizontal > 0:  # Moviéndose hacia la derecha
                            self.rect.right = bloque_rect.left  # Detenemos al jugador a la izquierda del bloque
                        elif movimiento_horizontal < 0:  # Moviéndose hacia la izquierda
                            self.rect.left = bloque_rect.right  # Detenemos al jugador a la derecha del bloque

    def aplicar_gravedad(self, mapa):
        """Aplica gravedad al jugador."""
        self.velocidad_y += GRAVEDAD  # Aumenta la velocidad de caída
        if self.velocidad_y > 10:  # Limitar la velocidad de caída
            self.velocidad_y = 10  # Esto evita que el jugador caiga demasiado rápido
        self.rect.y += self.velocidad_y  # Mueve al jugador en el eje Y
        self.verificar_colisiones_eje_y(mapa)  # Verificar colisiones en Y

    def verificar_colisiones_eje_y(self, mapa):
        """Verifica si el jugador colisiona con un bloque al moverse en el eje Y."""
        self.en_suelo = False  # Asumimos que no está en el suelo

        for fila in range(len(mapa)):
            for columna in range(len(mapa[fila])):
                if mapa[fila][columna] in (1, 2, 3, 4):  # Tierra, pasto, piedra o bloque inrompible
                    bloque_rect = pygame.Rect(columna * TAMANO_BLOQUE, fila * TAMANO_BLOQUE, TAMANO_BLOQUE, TAMANO_BLOQUE)

                    # Colisiones desde abajo (el jugador está cayendo sobre un bloque)
                    if self.rect.colliderect(bloque_rect):
                        if self.velocidad_y > 0 and self.rect.bottom <= bloque_rect.bottom:  # Solo detiene si está cayendo
                            self.rect.bottom = bloque_rect.top  # Detiene la caída
                            self.velocidad_y = 0  # Detiene la velocidad en Y
                            self.en_suelo = True  # Marca que el jugador está en el suelo

                        elif self.velocidad_y < 0 and self.rect.top >= bloque_rect.top:  # Si está saltando y colisiona arriba
                            self.rect.top = bloque_rect.bottom
                            self.velocidad_y = 0  # Detener el salto

    def dibujar(self, pantalla):
        """Dibuja al jugador en la pantalla."""
        pygame.draw.rect(pantalla, AZUL_JUGADOR, self.rect)  # Dibuja al jugador como un rectángulo azul
