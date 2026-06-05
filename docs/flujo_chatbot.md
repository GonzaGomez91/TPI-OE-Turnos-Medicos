# Flujo del Chatbot

## Flujo Principal: Reserva de Turno

### 1. Inicio

El paciente inicia la interacción con el chatbot.

El chatbot muestra un mensaje de bienvenida y presenta el menú principal.

Opciones disponibles:

* Reservar turno.
* Consultar turno.
* Cancelar turno.
* Salir.

---

### 2. Identificación del Paciente

El paciente selecciona la opción **Reservar turno**.

El chatbot solicita el DNI del paciente y verifica si se encuentra registrado.

---

### 3. Registro de Paciente

Si el paciente no se encuentra registrado, el chatbot ofrece realizar el registro.

Para registrar al paciente, solicita:

* DNI.
* Nombre.
* Apellido.
* Teléfono.

Luego, el paciente continúa con el proceso de reserva.

---

### 4. Selección del Turno

El chatbot muestra los próximos 5 días hábiles disponibles.

Luego muestra los horarios disponibles para la fecha seleccionada.

Horarios posibles:

* 09:00.
* 09:30.
* 10:00.
* 10:30.
* 11:00.
* 11:30.

El paciente selecciona el turno deseado.

---

### 5. Confirmación de Reserva

El chatbot muestra un resumen del turno seleccionado:

* Paciente.
* Fecha.
* Hora.

El paciente debe confirmar la reserva.

---

### 6. Registro del Turno

Si el paciente confirma la reserva, el chatbot registra el turno.

Si el paciente no confirma, la operación se cancela y no se registra ningún turno.

---

### 7. Fin

El chatbot informa el resultado de la operación y finaliza el proceso.

---

## Flujo Secundario: Consulta de Turno

El paciente selecciona la opción **Consultar turno**.

El chatbot solicita el DNI.

El sistema busca los turnos asociados a ese DNI.

Si existen turnos, los muestra al paciente.

Si no existen turnos, informa que no hay reservas registradas.

---

## Flujo Secundario: Cancelación de Turno

El paciente selecciona la opción **Cancelar turno**.

El chatbot solicita el DNI.

El sistema busca los turnos asociados a ese DNI.

Si existen turnos, el paciente selecciona cuál desea cancelar.

El chatbot solicita confirmación.

Si el paciente confirma, el turno se cancela.

Si el paciente no confirma, no se realiza ninguna modificación.
