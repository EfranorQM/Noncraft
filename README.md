
# Minecraft 2D - Proyecto en Pygame

### Descripción

Minecraft 2D es una recreación básica del famoso juego Minecraft, pero en dos dimensiones, desarrollado en Python utilizando la librería Pygame. Este proyecto incluye dos modos de juego principales:

- **Modo Supervivencia**: El jugador tiene una barra de vida con 10 corazones y puede recolectar, romper y colocar bloques en el mapa.
- **Modo Creativo**: El jugador puede colocar y romper bloques sin restricciones.

### Características principales

- **Generación de Mapas**: El mapa se genera automáticamente al inicio del juego, con una superficie de tierra, bloques de piedra y una fila de bloques inamovibles.
- **Modos de juego**:
  - **Supervivencia**: El jugador tiene una barra de vida y debe gestionar su inventario de bloques.
  - **Creativo**: El jugador tiene libertad total para construir sin restricciones.
- **Inventario**: El jugador tiene acceso a un inventario limitado con bloques recolectados.
- **Interfaz y controles**:
  - **Icono de regreso**: Permite volver al menú principal.
  - **Redimensionado**: La ventana del juego se puede redimensionar sin afectar el mapa.
  - **Teclas de movimiento**: Utiliza las teclas de dirección o `WASD` para moverte.

### Controles

- **Teclas de movimiento**: `WASD` o las flechas del teclado.
- **Clic izquierdo**: Romper bloque.
- **Clic derecho**: Colocar bloque.
- **Tecla `P`**: Volver al menú principal.
- **Rueda del mouse**: Cambiar de bloque en el inventario.

### Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/EfranorQM/minecraft-2d.git](https://github.com/EfranorQM/Noncraft.git
   cd minecraft-2d
   ```

2. Asegúrate de tener `Python` y `Pygame` instalados. Puedes instalar Pygame ejecutando:
   ```bash
   pip install pygame
   ```

3. Ejecuta el archivo principal `main.py` para iniciar el juego:
   ```bash
   python main.py
   ```

### Estructura del Proyecto

```plaintext
minecraft-2d/
├── config/
│   └── config.py        # Archivo de configuración del juego (dimensiones, colores, etc.)
├── map/
│   └── map.py           # Generación y dibujo del mapa
├── player/
│   ├── player.py        # Clase del jugador (movimiento, colisiones, gravedad)
│   ├── inventory.py     # Gestión del inventario de bloques
│   ├── events.py        # Gestión de eventos (teclado, ratón)
│   └── health.py        # Barra de vida en modo Supervivencia
├── imagenes/            # Directorio de imágenes (ícono de regreso, corazones)
├── menu.py              # Menú del juego (Supervivencia, Creativo)
├── boton_regreso.py     # Clase para el botón de regreso al menú
├── main.py              # Archivo principal que inicia el juego
└── README.md            # Descripción del proyecto
```


### Licencia

Este proyecto es de uso libre bajo la [Licencia MIT](LICENSE). Puedes utilizarlo y modificarlo como desees.
