# Chatbot para Reserva de Turnos Médicos

## Descripción del Proyecto

El proyecto consiste en el desarrollo de un chatbot para la reserva de turnos médicos, simulando el funcionamiento de un sistema automatizado de atención para un consultorio médico de un único profesional.

El chatbot permite:

* Registrar pacientes.
* Reservar turnos médicos.
* Mostrar únicamente fechas y horarios disponibles.
* Confirmar reservas de manera automática.

La información se almacena mediante archivos CSV, simulando una base de datos simple.

El objetivo principal del proyecto es modelar y automatizar el proceso administrativo de reserva de turnos médicos utilizando BPMN 2.0 e implementar una simulación funcional mediante Python y una interfaz web.

---

## Objetivos

* Modelar un proceso administrativo mediante BPMN 2.0.
* Implementar la lógica del chatbot respetando el flujo definido en el modelo BPMN.
* Simular persistencia de datos utilizando archivos CSV.
* Implementar validaciones y manejo de errores.
* Representar el flujo conversacional mediante una máquina de estados.
* Desarrollar una interfaz web que simule la interacción con un chatbot.

---

## Tecnologías y Herramientas

* Python
* Flask
* HTML
* CSS
* JavaScript
* Git
* GitHub
* GitHub Projects
* Archivos CSV
* BPMN 2.0

---

## Estructura del Repositorio

```text
.
├── README.md
├── bpmn/
├── data/
│   ├── pacientes.csv
│   └── turnos.csv
├── docs/
├── src/
│   ├── app.py
│   ├── bot.py
│   ├── estados.py
│   ├── persistencia.py
│   └── main.py
└── web/
    ├── static/
    │   ├── app.js
    │   └── styles.css
    └── templates/
        └── index.html
```

### Descripción de Carpetas y Archivos

| Elemento        | Descripción                                             |
| --------------- | ------------------------------------------------------- |
| README.md       | Documentación principal del proyecto.                   |
| bpmn/           | Diagramas BPMN AS-IS y TO-BE.                           |
| data/           | Archivos CSV utilizados para almacenar los datos.       |
| docs/           | Documentación complementaria del proyecto.              |
| src/            | Código fuente de la aplicación.                         |
| web/            | Interfaz web del chatbot.                               |
| pacientes.csv   | Almacena los pacientes registrados.                     |
| turnos.csv      | Almacena los turnos reservados.                         |
| app.py          | Aplicación Flask.                                       |
| bot.py          | Lógica conversacional del chatbot.                      |
| estados.py      | Definición de la máquina de estados.                    |
| persistencia.py | Gestión de persistencia en archivos CSV.                |
| main.py         | Simulación por consola utilizada durante el desarrollo. |

---

## Reglas de Negocio

* Todo paciente debe identificarse mediante su DNI.
* El DNI debe contener únicamente caracteres numéricos.
* Si el paciente no se encuentra registrado, deberá registrarse antes de reservar un turno.
* No podrán existir dos pacientes registrados con el mismo DNI.
* Los turnos solo podrán asignarse de lunes a viernes.
* Los turnos tendrán una duración de 30 minutos.
* Los horarios disponibles serán:

```text
09:00
09:30
10:00
10:30
11:00
11:30
```

* No podrán existir dos turnos reservados para la misma fecha y horario.
* El usuario deberá confirmar la reserva antes de que el turno sea registrado.

---

## Características Implementadas

* Registro automático de pacientes.
* Reserva de turnos médicos.
* Validación de DNI.
* Validación de datos obligatorios.
* Prevención de doble reserva para una misma fecha y horario.
* Verificación de disponibilidad antes de registrar un turno.
* Persistencia mediante archivos CSV.
* Manejo de errores de entrada.
* Máquina de estados para controlar el flujo conversacional.
* Interfaz web para simular la interacción con el chatbot.

---

## Instalación y Ejecución

### Requisitos

* Python 3.x
* Flask

### Instalación

Instalar Flask ejecutando:

```bash
pip install flask
```

### Ejecución

Desde la carpeta raíz del proyecto ejecutar:

```bash
python src/app.py
```

Una vez iniciado el servidor, abrir el navegador e ingresar a:

```text
http://127.0.0.1:5000
```

---

## Uso

1. Seleccionar la opción **Reservar turno**.
2. Ingresar el DNI del paciente.
3. Si el paciente no está registrado, completar los datos solicitados.
4. Seleccionar una fecha disponible.
5. Seleccionar un horario disponible.
6. Confirmar la reserva.

El sistema registrará automáticamente la información en los archivos CSV correspondientes.

---

## Comando de Cancelación

Durante cualquier etapa de la conversación se puede escribir:

```text
cancelar
```

para interrumpir la operación actual y regresar al menú principal.

---

## Modelado del Proceso

El proyecto incluye:

* Modelo BPMN AS-IS del proceso actual.
* Modelo BPMN TO-BE del proceso automatizado mediante chatbot.
* Máquina de estados utilizada para implementar el flujo conversacional.

---

## Autores

* Gonzalo Gomez
* Ana Laura Mansilla

---

## Licencia

Proyecto desarrollado con fines académicos para la materia Organización Empresarial.
