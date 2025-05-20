from nicegui import ui  # Importa la biblioteca NiceGUI para crear interfaces gráficas web

# Crea un campo de entrada de texto con la etiqueta 'Edad humana'
humano = ui.input(label='Edad humana')

# Crea una etiqueta vacía para mostrar el resultado
resultado = ui.label()

# Función que se ejecuta al presionar el botón
def calcular():
    try:
        edad_humana = int(humano.value)  # Convierte el valor ingresado a entero
        edad_mascota = edad_humana * 7  # Calcula la edad en "años perrunos"
        resultado.set_text(f'Edad estimada en años perrunos: {edad_mascota}')  # Muestra el resultado
    except (TypeError, ValueError):
        resultado.set_text('Por favor ingresa una edad válida.')  # Muestra un mensaje de error si la entrada no es válida

# Crea un botón que ejecuta la función 'calcular' al hacer clic
ui.button('Calcular edad de mascota', on_click=calcular)

# Inicia la interfaz gráfica
ui.run()

