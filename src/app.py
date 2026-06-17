from flask import Flask, render_template, request, jsonify
from bot import crear_sesion, procesar_mensaje

app = Flask(
    __name__,
    template_folder="../web/templates",
    static_folder="../web/static"
)

sesion = crear_sesion()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/mensaje", methods=["POST"])
def mensaje():
    datos = request.get_json()
    texto_usuario = datos.get("mensaje", "")

    respuesta = procesar_mensaje(texto_usuario, sesion)

    return jsonify({
        "respuesta": respuesta
    })


if __name__ == "__main__":
    app.run(debug=True)