import csv
import os

RUTA_PACIENTES = "data/pacientes.csv"
RUTA_TURNOS = "data/turnos.csv"

CAMPOS_PACIENTES = ["dni", "nombre", "apellido", "telefono"]
CAMPOS_TURNOS = ["id_turno", "dni", "fecha", "horario", "estado"]


def leer_csv(ruta):
    """
    Lee un archivo CSV y devuelve una lista de diccionarios.
    Si el archivo no existe o hay un error de lectura, devuelve una lista vacía.
    """
    try:
        if not os.path.exists(ruta):
            return []

        with open(ruta, mode="r", encoding="utf-8", newline="") as archivo:
            lector = csv.DictReader(archivo)

            if lector.fieldnames is None:
                return []

            return list(lector)

    except (OSError, csv.Error):
        return []


def escribir_csv(ruta, campos, datos):
    """
    Escribe una lista de diccionarios en un archivo CSV.
    Devuelve True si pudo escribir correctamente y False si ocurrió un error.
    """
    try:
        carpeta = os.path.dirname(ruta)

        if carpeta:
            os.makedirs(carpeta, exist_ok=True)

        with open(ruta, mode="w", encoding="utf-8", newline="") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writeheader()
            escritor.writerows(datos)

        return True

    except (OSError, csv.Error):
        return False


def buscar_paciente_por_dni(dni):
    """
    Busca un paciente por DNI.
    Si existe, devuelve el paciente.
    Si no existe, devuelve None.
    """
    pacientes = leer_csv(RUTA_PACIENTES)

    for paciente in pacientes:
        if paciente.get("dni") == dni:
            return paciente

    return None


def guardar_paciente(dni, nombre, apellido, telefono):
    """
    Guarda un nuevo paciente en pacientes.csv.
    No permite registrar dos pacientes con el mismo DNI.
    Devuelve True si guardó correctamente y False si no pudo guardar.
    """
    pacientes = leer_csv(RUTA_PACIENTES)

    for paciente in pacientes:
        if paciente.get("dni") == dni:
            return False

    nuevo_paciente = {
        "dni": dni,
        "nombre": nombre,
        "apellido": apellido,
        "telefono": telefono
    }

    pacientes.append(nuevo_paciente)

    return escribir_csv(RUTA_PACIENTES, CAMPOS_PACIENTES, pacientes)


def obtener_turnos():
    """
    Devuelve todos los turnos registrados.
    """
    return leer_csv(RUTA_TURNOS)


def turno_esta_disponible(fecha, horario):
    """
    Verifica si un turno está disponible.
    Un turno se considera ocupado si ya existe otro turno con la misma fecha,
    horario y estado 'Reservado'.
    """
    turnos = leer_csv(RUTA_TURNOS)

    for turno in turnos:
        if (
            turno.get("fecha") == fecha
            and turno.get("horario") == horario
            and turno.get("estado") == "Reservado"
        ):
            return False

    return True


def guardar_turno(id_turno, dni, fecha, horario, estado="Reservado"):
    """
    Guarda un nuevo turno en turnos.csv.

    Antes de guardar, vuelve a verificar que no exista otro turno reservado
    para la misma fecha y horario. Esto evita duplicados si otro usuario
    reservó el turno durante el proceso.
    """
    turnos = leer_csv(RUTA_TURNOS)

    for turno in turnos:
        if (
            turno.get("fecha") == fecha
            and turno.get("horario") == horario
            and turno.get("estado") == "Reservado"
        ):
            return False

    nuevo_turno = {
        "id_turno": id_turno,
        "dni": dni,
        "fecha": fecha,
        "horario": horario,
        "estado": estado
    }

    turnos.append(nuevo_turno)

    return escribir_csv(RUTA_TURNOS, CAMPOS_TURNOS, turnos)


def generar_id_turno():
    """
    Genera un ID simple para el próximo turno.
    Si el archivo está vacío o tiene datos inválidos, devuelve un ID seguro.
    """
    turnos = leer_csv(RUTA_TURNOS)

    if not turnos:
        return "1"

    ids_validos = []

    for turno in turnos:
        try:
            ids_validos.append(int(turno.get("id_turno", 0)))
        except ValueError:
            continue

    if not ids_validos:
        return "1"

    return str(max(ids_validos) + 1)