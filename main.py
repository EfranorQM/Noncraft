import pygame
import sys
from config.config import ANCHO_VENTANA, ALTO_VENTANA, TAMANO_BLOQUE, FILAS_TIERRA, FILAS_PIEDRA
from player.player import Player
from map.map import generar_map, dibujar_map
from player.inventory import Inventory
from player.events import EventManager
from player.health import HealthBar
from menu import Menu
from boton_regreso import BotonRegreso
from enemy import Enemy  # Importar la clase Enemy

class Juego:
    """Clase principal del juego."""

    def __init__(self, modo_juego):
        """Inicializa el juego, la ventana, el mapa, el jugador y el inventario."""
        pygame.init()
        self.modo_juego = modo_juego
        self.pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA), pygame.RESIZABLE)
        pygame.display.set_caption(f'Minecraft 2D - Modo {modo_juego}')
        self.reloj = pygame.time.Clock()

        # Generar un mapa más grande desde el principio (más columnas)
        self.columnas_totales = 100  # Número total de columnas del mapa
        self.filas_totales = ALTO_VENTANA // TAMANO_BLOQUE
        self.map = generar_map(FILAS_TIERRA, self.filas_totales, self.columnas_totales)

        # Crear al jugador en la parte superior del suelo
        self.player = Player(100, (ALTO_VENTANA - (FILAS_TIERRA + FILAS_PIEDRA) * TAMANO_BLOQUE) - TAMANO_BLOQUE, TAMANO_BLOQUE)

        # Crear inventario y eventos
        fuente = pygame.font.SysFont(None, 40)
        self.inventario = Inventory(10, 64, self.pantalla, fuente)
        self.event_manager = EventManager(self)

        # Inicializar la barra de vida y el enemigo si estamos en modo supervivencia
        if self.modo_juego == "Supervivencia":
            self.barra_vida = HealthBar(10, self.pantalla)  # 10 corazones de vida
            self.enemigo = Enemy(300, (ALTO_VENTANA - (FILAS_TIERRA + FILAS_PIEDRA) * TAMANO_BLOQUE) - TAMANO_BLOQUE, TAMANO_BLOQUE)  # Crear enemigo

        # Crear el botón de regreso
        self.boton_regreso = BotonRegreso(self.pantalla, self)

    def ejecutar(self):
        """Bucle principal del juego."""
        while True:
            self.event_manager.manejar_eventos()
            self.actualizar_juego()
            self.dibujar()
            pygame.display.flip()
            self.reloj.tick(60)

    def cambiar_modo(self, nuevo_modo):
        """Cambia el modo de juego al regresar al menú."""
        self.modo_juego = nuevo_modo
        nuevo_juego = Juego(nuevo_modo)
        nuevo_juego.ejecutar()

    def romper_bloque(self, fila, columna):
        """Rompe un bloque de tierra, pasto o piedra si está presente."""
        if self.map[fila][columna] == 1:  # Tierra
            self.map[fila][columna] = 0  # Romper el bloque
            self.inventario.agregar_bloque(1)  # Añadir un bloque de tierra al inventario
        elif self.map[fila][columna] == 2:  # Pasto
            self.map[fila][columna] = 0  # Romper el bloque
            self.inventario.agregar_bloque(2)  # Añadir un bloque de pasto al inventario
        elif self.map[fila][columna] == 3:  # Piedra
            self.map[fila][columna] = 0  # Romper el bloque
            self.inventario.agregar_bloque(3)  # Añadir un bloque de piedra al inventario

    def colocar_bloque_desde_inventario(self, fila, columna):
        """Coloca un bloque desde el inventario si hay disponible en la casilla seleccionada."""
        if self.inventario.inventario[self.inventario.casilla_seleccionada][1] > 0:
            if self.map[fila][columna] == 0:  # Solo coloca si el espacio está vacío
                self.map[fila][columna] = self.inventario.inventario[self.inventario.casilla_seleccionada][0]
                self.inventario.remover_bloque()  # Remover el bloque después de colocarlo
                # Forzar la actualización de la pantalla para reflejar el cambio
                self.dibujar()
                pygame.display.update()

    def redimensionar(self, nuevo_ancho, nuevo_alto):
        """Maneja la redimensión de la ventana."""
        global ANCHO_VENTANA, ALTO_VENTANA

        ANCHO_VENTANA = nuevo_ancho
        ALTO_VENTANA = nuevo_alto

        # Recalcular la cantidad de filas visibles
        self.filas_visibles = ALTO_VENTANA // TAMANO_BLOQUE
        self.columnas_visibles = ANCHO_VENTANA // TAMANO_BLOQUE

        # Redimensionar la ventana
        self.pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA), pygame.RESIZABLE)

        # Redibujar el mapa con el nuevo tamaño
        self.dibujar()
        pygame.display.update()

    def actualizar_juego(self):
        """Actualiza la lógica del juego."""
        teclas = pygame.key.get_pressed()
        self.player.manejar_movimiento(teclas, self.map)
        self.player.aplicar_gravedad(self.map)

        # Verificar si se presionó la tecla "P" para regresar al menú
        if teclas[pygame.K_p]:
            self.regresar_menu()

        # Actualizar enemigo solo en modo Supervivencia
        if self.modo_juego == "Supervivencia":
            self.enemigo.mover()  # El enemigo se mueve solo de izquierda a derecha

    def dibujar(self):
        """Dibuja solo la parte visible del mapa."""
        columnas_visibles = ANCHO_VENTANA // TAMANO_BLOQUE
        filas_visibles = ALTO_VENTANA // TAMANO_BLOQUE

        # Dibuja el mapa visible
        dibujar_map(self.pantalla, self.map, columnas_visibles, filas_visibles)

        # Dibuja el jugador
        self.player.dibujar(self.pantalla)

        # Dibuja el inventario
        self.inventario.dibujar()

        # Dibuja la barra de vida y enemigo en modo supervivencia
        if self.modo_juego == "Supervivencia":
            self.barra_vida.dibujar()
            self.enemigo.dibujar(self.pantalla)

        # Dibuja el botón de regreso
        self.boton_regreso.dibujar()

    def regresar_menu(self):
        """Regresa al menú principal."""
        menu = Menu(self.pantalla)
        modo_juego = menu.mostrar_menu()
        if modo_juego:
            self.cambiar_modo(modo_juego)


# Inicialización del juego
if __name__ == "__main__":
    pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
    menu = Menu(pantalla)

    # Mostrar el menú y obtener la selección del usuario
    modo_juego = menu.mostrar_menu()

    # Iniciar el juego según el modo seleccionado
    if modo_juego:
        juego = Juego(modo_juego)
        juego.ejecutar()
