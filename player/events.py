import pygame
import sys
from config.config import TAMANO_BLOQUE  # Asegúrate de importar esta constante

class EventManager:
    """Clase para manejar eventos del juego."""

    def __init__(self, juego):
        """Inicializa el manejador de eventos con la referencia al juego principal."""
        self.juego = juego

    def manejar_eventos(self):
        """Maneja los eventos del juego."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Evento para redimensionar la ventana
            if event.type == pygame.VIDEORESIZE:
                self.redimensionar_ventana(event.w, event.h)

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                columna = x // TAMANO_BLOQUE
                fila = y // TAMANO_BLOQUE

                if event.button == 1:  # Clic izquierdo para romper bloque
                    self.juego.romper_bloque(fila, columna)

                if event.button == 3:  # Clic derecho para colocar bloque
                    self.juego.colocar_bloque_desde_inventario(fila, columna)

            if event.type == pygame.MOUSEWHEEL:
                self.juego.inventario.mover_seleccion_con_rueda(event.y)

            if event.type == pygame.KEYDOWN:
                if pygame.K_1 <= event.key <= pygame.K_9:
                    self.juego.inventario.casilla_seleccionada = event.key - pygame.K_1
                elif event.key == pygame.K_0:
                    self.juego.inventario.casilla_seleccionada = 9

    def redimensionar_ventana(self, nuevo_ancho, nuevo_alto):
        """Llama al método de redimensionar del juego."""
        self.juego.redimensionar(nuevo_ancho, nuevo_alto)
