from estados import (
    MENU,
    ESPERANDO_OPCION,
    ESPERANDO_DNI,
    REGISTRANDO_PACIENTE,
    SELECCIONANDO_FECHA,
    SELECCIONANDO_HORARIO,
    CONFIRMANDO_RESERVA,
    REGISTRANDO_TURNO,
    FIN
)

from persistencia import (
    buscar_paciente_por_dni,
    guardar_paciente,
    guardar_turno,
    generar_id_turno,
    turno_esta_disponible
)


HORARIOS_DISPONIBLES = [
    "09:00",
    "09:30",
    "10:00",
    "10:30",
    "11:00",
    "11:30"
]


FECHAS_DISPONIBLES = [
    "2026-06-22",
    "2026-06-23",
    "2026-06-24",
    "2026-06-25",
    "2026-06-26"
]


def crear_sesion():
    return {
        "estado": MENU,
        "dni": "",
        "nombre": "",
        "apellido": "",
        "telefono": "",
        "fecha": "",
        "horario": ""
    }


def mostrar_menu():
    return (
        "Bienvenido al sistema de turnos médicos.\n\n"
        "Seleccione una opción:\n"
        "1. Reservar turno\n"
        "2. Consultar turno\n"
        "3. Cancelar turno\n"
        "4. Salir"
    )


def obtener_horarios_disponibles(fecha):
    horarios_libres = []

    for horario in HORARIOS_DISPONIBLES:
        if turno_esta_disponible(fecha, horario):
            horarios_libres.append(horario)

    return horarios_libres


def obtener_fechas_disponibles():
    fechas_libres = []

    for fecha in FECHAS_DISPONIBLES:
        horarios_libres = obtener_horarios_disponibles(fecha)

        if len(horarios_libres) > 0:
            fechas_libres.append(fecha)

    return fechas_libres


def mostrar_fechas():
    fechas_libres = obtener_fechas_disponibles()

    if len(fechas_libres) == 0:
        return "No hay fechas disponibles para reservar turnos."

    texto = "Seleccione una fecha disponible:\n"

    for i, fecha in enumerate(fechas_libres, start=1):
        texto += f"{i}. {fecha}\n"

    return texto


def mostrar_horarios(fecha):
    horarios_libres = obtener_horarios_disponibles(fecha)

    if len(horarios_libres) == 0:
        return "No hay horarios disponibles para esa fecha. Seleccione otra fecha."

    texto = "Seleccione un horario disponible:\n"

    for i, horario in enumerate(horarios_libres, start=1):
        texto += f"{i}. {horario}\n"

    return texto


def procesar_mensaje(mensaje, sesion):
    mensaje = mensaje.strip()

    if mensaje.lower() == "cancelar":
        sesion["estado"] = ESPERANDO_OPCION
        return "Operación cancelada.\n\n" + mostrar_menu()

    if sesion["estado"] == MENU:
        sesion["estado"] = ESPERANDO_OPCION
        return mostrar_menu()

    if sesion["estado"] == ESPERANDO_OPCION:
        if mensaje == "1":
            sesion["estado"] = ESPERANDO_DNI
            return "Ingrese su DNI:"

        elif mensaje == "2":
            return "Funcionalidad de consulta de turno en desarrollo."

        elif mensaje == "3":
            return "Funcionalidad de cancelación de turno en desarrollo."

        elif mensaje == "4":
            sesion["estado"] = FIN
            return "Gracias por utilizar el sistema."

        else:
            return "Opción inválida. Seleccione una opción del 1 al 4."

    if sesion["estado"] == ESPERANDO_DNI:
        if not mensaje.isdigit():
            return "DNI inválido. Ingrese solo números:"

        sesion["dni"] = mensaje
        paciente = buscar_paciente_por_dni(mensaje)

        if paciente:
            sesion["nombre"] = paciente["nombre"]
            sesion["apellido"] = paciente["apellido"]
            sesion["telefono"] = paciente["telefono"]
            sesion["estado"] = SELECCIONANDO_FECHA
            return mostrar_fechas()

        sesion["estado"] = REGISTRANDO_PACIENTE
        return (
            "Paciente no registrado.\n"
            "Ingrese nombre, apellido y teléfono separados por coma.\n"
            "Ejemplo: Juan,Perez,1122334455"
        )

    if sesion["estado"] == REGISTRANDO_PACIENTE:
        datos = mensaje.split(",")

        if len(datos) != 3:
            return "Formato inválido. Ingrese nombre, apellido y teléfono separados por coma."

        nombre = datos[0].strip()
        apellido = datos[1].strip()
        telefono = datos[2].strip()

        if nombre == "" or apellido == "" or telefono == "":
            return "Los datos no pueden estar vacíos. Intente nuevamente."

        if not telefono.isdigit():
            return "Teléfono inválido. Debe contener solo números."

        sesion["nombre"] = nombre
        sesion["apellido"] = apellido
        sesion["telefono"] = telefono

        guardar_paciente(
            sesion["dni"],
            sesion["nombre"],
            sesion["apellido"],
            sesion["telefono"]
        )

        sesion["estado"] = SELECCIONANDO_FECHA
        return "Paciente registrado correctamente.\n\n" + mostrar_fechas()

    if sesion["estado"] == SELECCIONANDO_FECHA:
        fechas_libres = obtener_fechas_disponibles()

        if len(fechas_libres) == 0:
            sesion["estado"] = MENU
            return "No hay fechas disponibles.\n\n" + mostrar_menu()

        if not mensaje.isdigit():
            return "Opción inválida. Seleccione una fecha por número."

        opcion = int(mensaje)

        if opcion < 1 or opcion > len(fechas_libres):
            return "Opción inválida. Seleccione una fecha disponible."

        sesion["fecha"] = fechas_libres[opcion - 1]
        sesion["estado"] = SELECCIONANDO_HORARIO
        return mostrar_horarios(sesion["fecha"])

    if sesion["estado"] == SELECCIONANDO_HORARIO:
        horarios_libres = obtener_horarios_disponibles(sesion["fecha"])

        if len(horarios_libres) == 0:
            sesion["estado"] = SELECCIONANDO_FECHA
            return "No hay horarios disponibles para esa fecha.\n\n" + mostrar_fechas()

        if not mensaje.isdigit():
            return "Opción inválida. Seleccione un horario por número."

        opcion = int(mensaje)

        if opcion < 1 or opcion > len(horarios_libres):
            return "Opción inválida. Seleccione un horario disponible."

        sesion["horario"] = horarios_libres[opcion - 1]
        sesion["estado"] = CONFIRMANDO_RESERVA

        return (
            "Resumen de la reserva:\n"
            f"Paciente: {sesion['nombre']} {sesion['apellido']}\n"
            f"DNI: {sesion['dni']}\n"
            f"Fecha: {sesion['fecha']}\n"
            f"Horario: {sesion['horario']}\n\n"
            "¿Confirma la reserva? Responda SI o NO."
        )

    if sesion["estado"] == CONFIRMANDO_RESERVA:
        if mensaje.lower() == "si":
            sesion["estado"] = REGISTRANDO_TURNO
            return registrar_turno(sesion)

        if mensaje.lower() == "no":
            sesion["estado"] = ESPERANDO_OPCION
            return "Reserva cancelada.\n\n" + mostrar_menu()

        return "Respuesta inválida. Responda SI o NO."

    if sesion["estado"] == FIN:
        return "La conversación ha finalizado."

    return "Estado no reconocido."


def registrar_turno(sesion):
    if not turno_esta_disponible(sesion["fecha"], sesion["horario"]):
        sesion["estado"] = SELECCIONANDO_FECHA
        return (
            "El turno seleccionado ya no está disponible.\n"
            "Por favor seleccione otra fecha u horario.\n\n"
            + mostrar_fechas()
        )

    id_turno = generar_id_turno()

    guardar_turno(
        id_turno,
        sesion["dni"],
        sesion["fecha"],
        sesion["horario"],
        "Reservado"
    )

    sesion["estado"] = MENU

    return (
        "Turno registrado correctamente.\n\n"
        f"Fecha: {sesion['fecha']}\n"
        f"Horario: {sesion['horario']}\n\n"
        + mostrar_menu()
    )