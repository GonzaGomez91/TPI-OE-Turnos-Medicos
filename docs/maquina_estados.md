# Máquina de Estados

La lógica conversacional del chatbot se implementa mediante una máquina de estados finitos. Cada estado representa una etapa específica del proceso de reserva de turnos.

---

## MENU

Estado inicial del sistema.

El chatbot muestra las opciones disponibles:

* Reservar turno.
* Salir.

---

## ESPERANDO_OPCION

El chatbot espera que el usuario seleccione una opción del menú principal.

Según la opción elegida, el flujo continúa hacia el proceso de reserva o finaliza la conversación.

---

## ESPERANDO_DNI

El chatbot solicita el DNI del paciente.

Si el paciente ya se encuentra registrado, continúa con la selección de fecha.

Si el paciente no existe en el sistema, pasa al estado de registro de paciente.

---

## REGISTRANDO_PACIENTE

El chatbot solicita los datos necesarios para registrar un nuevo paciente:

* Nombre.
* Apellido.
* Teléfono.

Una vez completado el registro, el proceso continúa con la selección de fecha.

---

## SELECCIONANDO_FECHA

El chatbot muestra las fechas disponibles para la reserva de turnos.

El paciente selecciona una de las opciones ofrecidas.

---

## SELECCIONANDO_HORARIO

El chatbot muestra los horarios disponibles para la fecha seleccionada.

El paciente selecciona el horario deseado.

---

## CONFIRMANDO_RESERVA

El chatbot presenta un resumen de la reserva:

* Paciente.
* DNI.
* Fecha.
* Horario.

El paciente debe confirmar o cancelar la operación.

---

## REGISTRANDO_TURNO

El chatbot verifica nuevamente la disponibilidad del turno seleccionado y registra la reserva en el sistema.

Esta validación evita inconsistencias en caso de que otro usuario haya reservado el mismo turno durante el proceso.

---

## FIN

Estado utilizado para finalizar la conversación cuando el usuario selecciona la opción de salida.
