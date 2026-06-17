const chatBox = document.getElementById("chat-box");
const chatForm = document.getElementById("chat-form");
const inputMensaje = document.getElementById("mensaje");

function agregarMensaje(texto, tipo) {
    const mensaje = document.createElement("div");
    mensaje.classList.add("message");

    if (tipo === "bot") {
        mensaje.classList.add("bot-message");
    } else {
        mensaje.classList.add("user-message");
    }

    mensaje.textContent = texto;
    chatBox.appendChild(mensaje);
    chatBox.scrollTop = chatBox.scrollHeight;
}

async function enviarMensaje(texto) {
    const respuesta = await fetch("/mensaje", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            mensaje: texto
        })
    });

    const datos = await respuesta.json();
    agregarMensaje(datos.respuesta, "bot");
}

chatForm.addEventListener("submit", async function(evento) {
    evento.preventDefault();

    const texto = inputMensaje.value.trim();

    if (texto === "") {
        return;
    }

    agregarMensaje(texto, "user");
    inputMensaje.value = "";

    await enviarMensaje(texto);
});

window.addEventListener("load", async function() {
    await enviarMensaje("");
});