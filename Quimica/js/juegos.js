// Juego 1: Adivina la Respuesta
const preguntas = [
    { pista: "Es el gas esencial para la respiración humana", respuesta: "Oxígeno" },
    { pista: "Es un elemento químico que compone el agua junto con el oxígeno", respuesta: "Hidrógeno" }
];

function mostrarPregunta() {
    let indice = Math.floor(Math.random() * preguntas.length);
    document.getElementById("pista").innerText = preguntas[indice].pista;
    document.getElementById("respuesta").dataset.respuestaCorrecta = preguntas[indice].respuesta;
}

function verificarRespuesta() {
    let respuestaUsuario = document.getElementById("respuesta").value.trim();
    let respuestaCorrecta = document.getElementById("respuesta").dataset.respuestaCorrecta;
    let resultado = document.getElementById("resultado");
    
    if (respuestaUsuario.toLowerCase() === respuestaCorrecta.toLowerCase()) {
        resultado.innerText = "✅ ¡Muy bien! La respuesta es correcta.";
        resultado.style.color = "green";
    } else {
        resultado.innerText = "❌ Lo siento, esa no es la respuesta correcta. Intenta otra vez.";
        resultado.style.color = "red";
    }
}

// Juego 2: Arrastra y Clasifica
function allowDrop(event) {
    event.preventDefault();
}

function drag(event) {
    event.dataTransfer.setData("text", event.target.id);
}

function drop(event) {
    event.preventDefault();
    let idElemento = event.dataTransfer.getData("text");
    let categoria = event.target.dataset.categoria;
    let elemento = document.getElementById(idElemento);

    if ((idElemento === "elemento1" && categoria === "gas") ||
        (idElemento === "elemento2" && categoria === "liquido") ||
        (idElemento === "elemento3" && categoria === "solido")) {
        event.target.appendChild(elemento);
    }
}
