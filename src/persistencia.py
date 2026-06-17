import csv
import os

RUTA_PACIENTES = "data/pacientes.csv"
RUTA_TURNOS = "data/turnos.csv"


def leer_csv(ruta):
    if not os.path.exists(ruta):
        return []

    with open(ruta, mode="r", encoding="utf-8", newline="") as archivo:
        lector = csv.DictReader(archivo)
        return list(lector)


def escribir_csv(ruta, campos, datos):
    with open(ruta, mode="w", encoding="utf-8", newline="") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(datos)


def buscar_paciente_por_dni(dni):
    pacientes = leer_csv(RUTA_PACIENTES)

    for paciente in pacientes:
        if paciente["dni"] == dni:
            return paciente

    return None


def guardar_paciente(dni, nombre, apellido, telefono):
    pacientes = leer_csv(RUTA_PACIENTES)

    nuevo_paciente = {
        "dni": dni,
        "nombre": nombre,
        "apellido": apellido,
        "telefono": telefono
    }

    pacientes.append(nuevo_paciente)

    campos = ["dni", "nombre", "apellido", "telefono"]
    escribir_csv(RUTA_PACIENTES, campos, pacientes)


def obtener_turnos():
    return leer_csv(RUTA_TURNOS)


def turno_esta_disponible(fecha, horario):
    turnos = leer_csv(RUTA_TURNOS)

    for turno in turnos:
        if (
            turno["fecha"] == fecha
            and turno["horario"] == horario
            and turno["estado"] == "Reservado"
        ):
            return False

    return True


def guardar_turno(id_turno, dni, fecha, horario, estado="Reservado"):
    turnos = leer_csv(RUTA_TURNOS)

    nuevo_turno = {
        "id_turno": id_turno,
        "dni": dni,
        "fecha": fecha,
        "horario": horario,
        "estado": estado
    }

    turnos.append(nuevo_turno)

    campos = ["id_turno", "dni", "fecha", "horario", "estado"]
    escribir_csv(RUTA_TURNOS, campos, turnos)


def generar_id_turno():
    turnos = leer_csv(RUTA_TURNOS)

    if not turnos:
        return "1"

    ultimo_id = max(int(turno["id_turno"]) for turno in turnos)
    return str(ultimo_id + 1)