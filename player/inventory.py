import pygame

class Inventory:
    """Clase que maneja el inventario del jugador."""

    def __init__(self, casillas, max_items, pantalla, fuente):
        """Inicializa el inventario."""
        self.casillas = casillas
        self.max_items = max_items
        self.pantalla = pantalla
        self.fuente = fuente
        self.inventario = [[None, 0] for _ in range(casillas)]  # Inicializa el inventario
        self.casilla_seleccionada = 0

    def agregar_bloque(self, tipo_bloque):
        """Añade un bloque al inventario."""
        for i in range(len(self.inventario)):
            if self.inventario[i][0] == tipo_bloque and self.inventario[i][1] < self.max_items:
                self.inventario[i][1] += 1
                return
        for i in range(len(self.inventario)):
            if self.inventario[i][1] == 0:
                self.inventario[i] = [tipo_bloque, 1]
                return

    def remover_bloque(self):
        """Remueve un bloque de la casilla seleccionada."""
        if self.inventario[self.casilla_seleccionada][1] > 0:
            self.inventario[self.casilla_seleccionada][1] -= 1
            if self.inventario[self.casilla_seleccionada][1] == 0:
                self.inventario[self.casilla_seleccionada] = [None, 0]
            return True
        return False

    def mover_seleccion_con_rueda(self, direccion):
        """Cambia la casilla seleccionada con la rueda del ratón."""
        self.casilla_seleccionada = (self.casilla_seleccionada - direccion) % self.casillas

    def dibujar(self):
        """Dibuja las casillas del inventario, los bloques disponibles y la selección."""
        casilla_size = 40  # Nuevo tamaño más pequeño para las casillas
        espacio = 5  # Espacio más pequeño entre las casillas

        # Calcular la posición inicial para centrar el inventario
        ancho_total_inventario = self.casillas * casilla_size + (self.casillas - 1) * espacio
        x_inventario = (self.pantalla.get_width() - ancho_total_inventario) // 2
        y_inventario = self.pantalla.get_height() - 50  # Ajustar la posición vertical

        for i in range(self.casillas):
            color_casilla = (255, 255, 255)
            if i == self.casilla_seleccionada:
                color_casilla = (255, 255, 0)  # Casilla seleccionada resaltada en amarillo

            # Dibujar el cuadro de la casilla
            pygame.draw.rect(self.pantalla, color_casilla, 
                             (x_inventario + i * (casilla_size + espacio), y_inventario, casilla_size, casilla_size), 2)

            # Mostrar la cantidad de bloques en la casilla
            if self.inventario[i][1] > 0:
                texto_bloques = self.fuente.render(f'{self.inventario[i][1]}', True, (255, 255, 255))
                self.pantalla.blit(texto_bloques, (x_inventario + i * (casilla_size + espacio) + 10, y_inventario + 10))
