from nicegui import ui  # Importa NiceGUI para crear interfaces web

def enviar():
    ui.notify(f'Usuario {nombre.value} registrado con éxito')  # Muestra notificación con el nombre ingresado

nombre = ui.input(label='Nombre')  # Campo para ingresar el nombre
email = ui.input(label='Email')  # Campo para ingresar el email
contraseña = ui.input(label='Contraseña', password=True)  # Campo para contraseña oculta
ui.checkbox('Acepto los términos')  # Casilla para aceptar términos (no se guarda el valor)
ui.button('Registrarse', on_click=enviar)  # Botón que llama a la función enviar al hacer clic

ui.run()  # Ejecuta la aplicación web
