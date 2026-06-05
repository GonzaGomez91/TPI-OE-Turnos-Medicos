# Flujo del Chatbot

## Flujo Principal: Reserva de Turno

### 1. Inicio del proceso

El paciente inicia la interacción con el chatbot.

El sistema muestra un mensaje de bienvenida y presenta el menú principal.

Opciones disponibles:

- Reservar turno
- Consultar turno
- Cancelar turno
- Salir

---

### 2. Selección de opción

El paciente selecciona la opción **Reservar turno**.

Si el paciente ingresa una opción inválida, el sistema informa el error y vuelve a mostrar el menú principal.

---

### 3. Solicitud de DNI

El sistema solicita al paciente que ingrese su DNI.

El paciente ingresa su número de DNI.

El sistema valida que el DNI:

- No esté vacío.
- Contenga únicamente números.

Si el DNI es inválido, el sistema solicita ingresarlo nuevamente.

---

### 4. Verificación del paciente

El sistema consulta el archivo `pacientes.csv` para verificar si el DNI ingresado corresponde a un paciente registrado.

#### Si el paciente está registrado

El sistema continúa con el proceso de reserva de turno.

#### Si el paciente no está registrado

El sistema ofrece registrar un nuevo paciente.

Para registrar al paciente, solicita:

- Nombre y apellido.
- Teléfono.

Luego guarda los datos en `pacientes.csv` y continúa con el proceso de reserva.

---

### 5. Selección de fecha

El sistema solicita al paciente que ingrese una fecha para el turno.

La fecha debe corresponder a un día hábil, de lunes a viernes.

Si la fecha ingresada no es válida, el sistema solicita ingresar una nueva fecha.

---

### 6. Selección de horario

El sistema muestra los horarios disponibles para la fecha seleccionada.

Horarios posibles:

- 09:00
- 09:30
- 10:00
- 10:30
- 11:00
- 11:30

El paciente selecciona un horario.

Si el horario seleccionado no está disponible, el sistema informa la situación y permite seleccionar otro horario.

---

### 7. Confirmación de reserva

El sistema muestra un resumen del turno:

- Nombre del paciente.
- Fecha.
- Hora.

Luego solicita confirmación.

#### Si el paciente confirma

El sistema registra el turno en `turnos.csv`.

#### Si el paciente no confirma

El sistema cancela la operación y no registra el turno.

---

### 8. Fin del proceso

El sistema informa el resultado de la operación.

Si la reserva fue confirmada, muestra un mensaje de éxito.

Si la operación fue cancelada, informa que no se realizó ninguna reserva.