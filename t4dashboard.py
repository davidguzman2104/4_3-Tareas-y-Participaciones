from nicegui import ui  # Importa la librería NiceGUI para crear interfaces gráficas web

# Agrupa los elementos en una fila horizontal
with ui.row():

    # Primer card (tarjeta) con información de ventas
    with ui.card():
        ui.label('Ventas')       # Título del dato
        ui.label(' $1,200')      # Valor de las ventas

    # Segundo card con información de usuarios
    with ui.card():
        ui.label('Usuarios')     # Título del dato
        ui.label(' 342')         # Número de usuarios

    # Tercer card con información de tickets
    with ui.card():
        ui.label('Tickets')      # Título del dato
        ui.label(' 18')          # Número de tickets

# Inicia la interfaz gráfica web
ui.run()
