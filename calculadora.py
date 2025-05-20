from nicegui import ui  # Importa la librería NiceGUI para crear interfaces gráficas web

# Crea un título para la aplicación
ui.label(' Calculadora de Suma Simple').classes('text-h4')

# Crea los campos de entrada numérica para los dos valores
num1 = ui.number(label='Número 1', value=0)
num2 = ui.number(label='Número 2', value=0)

# Crea una etiqueta para mostrar el resultado
resultado = ui.label('Resultado: 0').classes('text-h6')

# Agrupa los botones en una fila
with ui.row():

    # Función que realiza la suma y actualiza el resultado
    def suma():
        suma = num1.value + num2.value
        resultado.text = f'Resultado: {suma}'
        ui.notify(f'La suma es {suma}')  # Notificación emergente con el resultado

    # Crea un botón que ejecuta la suma al hacer clic
    ui.button('SUMA', on_click=suma)

    # Función que realiza la resta y actualiza el resultado
    def resta():
        resta = num1.value - num2.value
        resultado.text = f'Resultado: {resta}'
        ui.notify(f'La resta es {resta}')

    # Crea un botón que ejecuta la resta al hacer clic
    ui.button('RESTA', on_click=resta)

    # Función que realiza la multiplicación y actualiza el resultado
    def multiplicacion():
        multiplicacion = num1.value * num2.value
        resultado.text = f'Resultado: {multiplicacion}'
        ui.notify(f'La multiplicación es {multiplicacion}')

    # Crea un botón que ejecuta la multiplicación al hacer clic
    ui.button('MUltiplicacion', on_click=multiplicacion)

    # Función que realiza la división y actualiza el resultado
    def division():
        division = num1.value / num2.value
        resultado.text = f'Resultado: {division}'
        ui.notify(f'La división es {division}')

    # Crea un botón que ejecuta la división al hacer clic
    ui.button('Division', on_click=division)

# Inicia la aplicación web
ui.run()
