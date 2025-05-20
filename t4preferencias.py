from nicegui import ui  # Importa la librería NiceGUI para interfaces gráficas web

# Función que se ejecuta al hacer clic en el botón
def mostrar():
    # Muestra una notificación con el color seleccionado y el estado del tema
    ui.notify(f'Color: {color.value}, Tema oscuro: {tema.value}')

# Crea un menú desplegable para seleccionar un color favorito
color = ui.select(['Rojo', 'Verde', 'Azul'], label='Color favorito')

# Crea un interruptor (switch) para activar o desactivar el tema oscuro
tema = ui.switch('Tema oscuro')

# Crea un botón que llama a la función 'mostrar' al hacer clic
ui.button('Guardar preferencias', on_click=mostrar)

# Inicia la aplicación web
ui.run()
