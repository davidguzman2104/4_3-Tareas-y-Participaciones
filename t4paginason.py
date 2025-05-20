from nicegui import ui
# Puedes usar una URL de un archivo de audio público o uno local en tu proyecto
AUDIO_URL = 'https://www.soundhelix.com/examples/mp3/SoundHelixSong-1.mp3'
ui.label(' Reproductor de audio')
# Control de audio
audio = ui.audio(AUDIO_URL, autoplay=False, controls=True)
# Botones para controlar manualmente desde Python
with ui.row():
 ui.button('Reproducir', on_click=lambda: audio.run_method('play'))
 ui.button('Pausar', on_click=lambda: audio.run_method('pause'))
 ui.run()