document.addEventListener("DOMContentLoaded", () => { // Espera a que el DOM esté completamente cargado
    const botones = document.querySelectorAll(".boton-curso"); // Selecciona todos los botones de cursos
    const letrero = document.getElementById("bienvenido"); // Selecciona el elemento del mensaje de bienvenida
  
    const toni = document.querySelector(".toni-lateral img"); // Selecciona la imagen del avatar Toni
  
    // Evento: cuando el cursor entra en la imagen de Toni
    toni.addEventListener("mouseenter", () => {
      toni.style.transform = "scale(1.1)"; // Agranda ligeramente la imagen (efecto zoom)
    });
  
    // Evento: cuando el cursor sale de la imagen de Toni
    toni.addEventListener("mouseleave", () => {
      toni.style.transform = "scale(1)"; // Restaura el tamaño original
    });
  });

  let numero1, numero2, operador, respuestaCorrecta; 
// Declaración de variables globales para los números y operador de la operación, 
// así como para almacenar la respuesta correcta.

function nuevaOperacion() { 
    // Función que genera una nueva operación cuando es llamada.

    numero1 = Math.floor(Math.random() * 10) + 1; 
    // Genera un número aleatorio entre 1 y 10 para numero1.

    numero2 = Math.floor(Math.random() * 10) + 1; 
    // Genera un número aleatorio entre 1 y 10 para numero2.

    const operadores = ['+', '-', '×', '÷']; 
    // Array que contiene los operadores posibles para la operación.

    operador = operadores[Math.floor(Math.random() * 4)]; 
    // Selecciona aleatoriamente un operador del array de operadores.

    // Asegura que la división sea exacta, evitando números decimales en la respuesta.
    if (operador === '÷') { 
        numero1 = numero2 * (Math.floor(Math.random() * 5) + 1); 
        // Si el operador es división, asegura que el primer número (numero1)
        // sea múltiplo del segundo número (numero2) para que la división sea exacta.
    }

    // Calcula la respuesta correcta según el operador seleccionado.
    switch (operador) { 
        case '+': respuestaCorrecta = numero1 + numero2; break; 
        // Si el operador es suma, la respuesta correcta es la suma de numero1 y numero2.
        case '-': respuestaCorrecta = numero1 - numero2; break; 
        // Si el operador es resta, la respuesta correcta es la resta de numero1 y numero2.
        case '×': respuestaCorrecta = numero1 * numero2; break; 
        // Si el operador es multiplicación, la respuesta correcta es el producto de numero1 y numero2.
        case '÷': respuestaCorrecta = numero1 / numero2; break; 
        // Si el operador es división, la respuesta correcta es el cociente de numero1 y numero2.
    }

    // Muestra la operación generada en el elemento con id 'operacion' en la página web.
    document.getElementById('operacion').textContent = `${numero1} ${operador} ${numero2} = ?`; 
    // Reinicia el campo de respuesta y el resultado al mostrar una nueva operación.
    document.getElementById('respuesta').value = ''; 
    document.getElementById('resultado').textContent = ''; 
}

function verificarRespuesta() { 
    // Función que verifica si la respuesta del usuario es correcta.

    const respuestaUsuario = parseFloat(document.getElementById('respuesta').value); 
    // Obtiene el valor introducido por el usuario en el campo de respuesta y lo convierte a número.

    const resultadoElement = document.getElementById('resultado'); 
    // Obtiene el elemento donde se mostrará el resultado de la verificación.

    if (isNaN(respuestaUsuario)) { 
        // Verifica si el valor introducido no es un número.
        resultadoElement.textContent = '¡Escribe un número!'; 
        // Muestra un mensaje de error si no se introdujo un número.
        resultadoElement.style.color = 'red'; 
        // Cambia el color del mensaje a rojo.
    } else if (respuestaUsuario === respuestaCorrecta) { 
        // Verifica si la respuesta del usuario es igual a la respuesta correcta.
        resultadoElement.textContent = '✅ ¡Correcto! ¡Eres un genio!'; 
        // Muestra un mensaje de éxito si la respuesta es correcta.
        resultadoElement.style.color = 'lightgreen'; 
        // Cambia el color del mensaje a verde claro.
    } else { 
        // Si la respuesta es incorrecta, se ejecuta este bloque.
        resultadoElement.textContent = `❌ Incorrecto. La respuesta es ${respuestaCorrecta}. ¡Intenta otra vez!`; 
        // Muestra un mensaje de error con la respuesta correcta.
        resultadoElement.style.color = 'pink'; 
        // Cambia el color del mensaje a rosa.
    }
}

// Ejecuta la función nuevaOperacion cuando la página se carga.
window.onload = nuevaOperacion;
