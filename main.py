from nicegui import ui # llamamos la libreria 

ui.label('!Hola mundo!') # utilizamos una etiqueta que muestra un mensaje 

ui. button("Has click",on_click=lambda:ui.notify("!boton clickeado!"))# al crear un boton le asiganamos un evento de cuando de click nos notifique

ui.run() # ejecuta 