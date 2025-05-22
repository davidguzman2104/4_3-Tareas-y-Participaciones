function verificarRespuesta(opcion) {
  const mensaje = document.getElementById('respuesta');
  if (opcion === 'b') {
    mensaje.textContent = '✅ ¡Muy bien! Reciclar es la mejor opción.';
    mensaje.style.color = '#2e7d32';
  } else {
    mensaje.textContent = '❌ Ups... Intenta otra vez. ¡Reciclar es lo mejor!';
    mensaje.style.color = '#d32f2f';
  }
}
