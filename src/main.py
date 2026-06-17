from bot import crear_sesion, procesar_mensaje


def main():
    """
    Ejecuta una simulación por consola del chatbot.
    """
    sesion = crear_sesion()

    print("=== Simulación del Chatbot de Turnos Médicos ===")
    print(procesar_mensaje("", sesion))

    while sesion["estado"] != "FIN":
        mensaje_usuario = input("\nPaciente: ")
        respuesta_bot = procesar_mensaje(mensaje_usuario, sesion)
        print(f"\nChatbot: {respuesta_bot}")


if __name__ == "__main__":
    main()