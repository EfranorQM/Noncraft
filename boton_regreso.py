import pygame
from menu import Menu

class BotonRegreso:
    """Clase que maneja el ícono de regreso al menú."""

    def __init__(self, pantalla, juego):
        """Inicializa el ícono de regreso."""
        self.pantalla = pantalla
        self.juego = juego

        # Cargar el ícono de regreso
        self.icono_regreso = pygame.image.load("imagenes/icono_regreso.png")
        self.icono_regreso = pygame.transform.scale(self.icono_regreso, (50, 50))  # Ajustar tamaño del ícono

        # Definir la posición del ícono en la esquina superior derecha
        self.rect = self.icono_regreso.get_rect(topright=(self.pantalla.get_width() - 60, 20))

    def dibujar(self):
        """Dibuja el ícono en la pantalla."""
        self.pantalla.blit(self.icono_regreso, self.rect.topleft)

    def verificar_click(self, event):
        """Verifica si se hizo clic en el ícono de regreso."""
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if self.rect.collidepoint(x, y):
                # Si se hace clic en el ícono, volver al menú
                menu = Menu(self.pantalla)
                modo_juego = menu.mostrar_menu()
                if modo_juego:
                    self.juego.cambiar_modo(modo_juego)

    def manejar_eventos(self, event):
        """Manejar eventos para regresar al menú."""
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.verificar_click(event)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            # Permitir también regresar con la tecla 'p'
            menu = Menu(self.pantalla)
            modo_juego = menu.mostrar_menu()
            if modo_juego:
                self.juego.cambiar_modo(modo_juego)
