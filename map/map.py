# map.py

import pygame
from config.config import TAMANO_BLOQUE, MARRON, VERDE_PASTO, GRIS_PIEDRA, AZUL_CIELO, FILAS_PIEDRA

def generar_map(filas_tierra, filas_totales, columnas):
    """Genera una matriz representando el mapa con bloques de tierra, pasto, cielo, piedra e invisibles."""
    map = []

    # Agregar filas de cielo
    for _ in range(filas_totales - (filas_tierra + FILAS_PIEDRA)):
        fila = [0] * columnas  # Fila de cielo
        map.append(fila)

    # Agregar las filas de tierra
    for i in range(filas_tierra):
        if i == 0:
            # Primera fila de tierra (será pasto visualmente pero funcionalmente como tierra)
            fila = [2] * columnas  # Bloque de pasto encima de la tierra
        else:
            fila = [1] * columnas  # Bloque de tierra
        map.append(fila)

    # Agregar las filas de piedra
    for _ in range(FILAS_PIEDRA):
        fila = [3] * columnas  # Bloque de piedra
        map.append(fila)

    # Añadir la última fila de bloques inrompibles invisibles (tipo 4)
    fila_invisible = [4] * columnas
    map.append(fila_invisible)

    return map
def dibujar_map(pantalla, mapa, columnas_visibles, filas_visibles):
    """Dibuja el mapa en la pantalla, utilizando el mapa proporcionado."""
    
    filas_totales = len(mapa)  # Número total de filas en el mapa
    columnas_totales = len(mapa[0])  # Número total de columnas en el mapa (asumiendo que todas las filas tienen el mismo número de columnas)

    for fila in range(filas_visibles):
        for columna in range(columnas_visibles):
            # Nos aseguramos de que no intentemos acceder a índices fuera de los límites del mapa
            if fila < filas_totales and columna < columnas_totales:
                bloque = mapa[fila][columna]
                x = columna * TAMANO_BLOQUE
                y = fila * TAMANO_BLOQUE
                bloque_rect = pygame.Rect(x, y, TAMANO_BLOQUE, TAMANO_BLOQUE)

                # Dibujamos los bloques según su tipo
                if bloque == 1:  # Tierra
                    pygame.draw.rect(pantalla, (139, 69, 19), bloque_rect)  # Color marrón tierra
                elif bloque == 2:  # Tierra con pasto
                    pygame.draw.rect(pantalla, (139, 69, 19), bloque_rect)  # Color marrón tierra
                    pygame.draw.rect(pantalla, (34, 139, 34), bloque_rect)  # Color verde pasto
                elif bloque == 3:  # Piedra
                    pygame.draw.rect(pantalla, (128, 128, 128), bloque_rect)  # Color gris piedra
                elif bloque == 4:  # Bloque invisible
                    pygame.draw.rect(pantalla, (0, 0, 0), bloque_rect)  # Color negro invisible
                else:  # Espacio vacío (cielo)
                    pygame.draw.rect(pantalla, (135, 206, 235), bloque_rect)  # Color cielo azul claro
            else:
                # Si estamos fuera de los límites del mapa, dibujamos piedra
                x = columna * TAMANO_BLOQUE
                y = fila * TAMANO_BLOQUE
                bloque_rect = pygame.Rect(x, y, TAMANO_BLOQUE, TAMANO_BLOQUE)
                pygame.draw.rect(pantalla, (128, 128, 128), bloque_rect)  # Color gris piedra