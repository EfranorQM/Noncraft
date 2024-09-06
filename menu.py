import pygame
import sys

class Menu:
    """Clase que representa el menú principal del juego."""

    def __init__(self, pantalla):
        """Inicializa el menú."""
        pygame.init()  # Asegúrate de inicializar Pygame
        self.pantalla = pantalla
        self.fuente = pygame.font.SysFont(None, 60)
        self.opciones = ['Modo Supervivencia', 'Modo Creativo']
        self.opcion_seleccionada = 0  # Por defecto selecciona la primera opción

    def mostrar_menu(self):
        """Muestra el menú y espera la selección del usuario."""
        while True:
            self.pantalla.fill((0, 0, 0))  # Fondo negro
            self.mostrar_opciones()
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        self.opcion_seleccionada = (self.opcion_seleccionada + 1) % len(self.opciones)
                    elif event.key == pygame.K_UP:
                        self.opcion_seleccionada = (self.opcion_seleccionada - 1) % len(self.opciones)
                    elif event.key == pygame.K_RETURN:
                        # Devuelve el modo de juego seleccionado
                        if self.opcion_seleccionada == 0:
                            return "Supervivencia"
                        elif self.opcion_seleccionada == 1:
                            return "Creativo"

    def mostrar_opciones(self):
        """Muestra las opciones del menú."""
        for i, opcion in enumerate(self.opciones):
            if i == self.opcion_seleccionada:
                color = (255, 255, 0)  # Amarillo para la opción seleccionada
            else:
                color = (255, 255, 255)  # Blanco para las otras opciones
            texto = self.fuente.render(opcion, True, color)
            self.pantalla.blit(texto, (100, 150 + i * 100))
