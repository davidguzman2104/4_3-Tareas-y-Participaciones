from nicegui import ui  # Importa la librería NiceGUI para crear interfaces gráficas web

# Lista de diccionarios con datos de ejemplo (nombre y edad de personas)
datos = [
    {'Nombre': 'Ana', 'Edad': 21},
    {'Nombre': 'Luis', 'Edad': 23},
    {'Nombre': 'Carla', 'Edad': 22},
]

# Definición de las columnas de la tabla (nombre, etiqueta visible y campo asociado)
columnas = [
    {'name': 'Nombre', 'label': 'Nombre', 'field': 'Nombre'},
    {'name': 'Edad', 'label': 'Edad', 'field': 'Edad'},
]

# Crea una tabla con las columnas y filas definidas, usando el nombre como clave única de cada fila
ui.table(columns=columnas, rows=datos, row_key='Nombre')

# Inicia la aplicación web
ui.run()
