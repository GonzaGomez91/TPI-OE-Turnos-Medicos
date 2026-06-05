# Máquina de Estados

## ESTADO_MENU

El chatbot muestra las opciones principales disponibles:

* Reservar turno.
* Consultar turno.
* Cancelar turno.
* Salir.

---

## ESTADO_IDENTIFICAR_PACIENTE

El chatbot solicita el DNI del paciente y verifica si se encuentra registrado.

Si el DNI no corresponde a un paciente registrado, se deriva al estado de registro de paciente.

---

## ESTADO_REGISTRAR_PACIENTE

El chatbot solicita los datos necesarios para registrar un nuevo paciente:

* DNI.
* Nombre.
* Apellido.
* Teléfono.

Una vez registrado, el paciente puede continuar con la reserva del turno.

---

## ESTADO_SELECCIONAR_TURNO

El chatbot muestra las fechas y horarios disponibles.

El paciente selecciona un turno dentro de los próximos 5 días hábiles, en el horario de atención del consultorio.

---

## ESTADO_CONFIRMAR_RESERVA

El chatbot muestra un resumen del turno seleccionado y solicita confirmación al paciente.

---

## ESTADO_REGISTRAR_TURNO

El chatbot registra la reserva confirmada en el sistema.

---

## ESTADO_CONSULTAR_TURNO

El chatbot permite consultar los turnos asociados a un DNI.

---

## ESTADO_CANCELAR_TURNO

El chatbot permite cancelar un turno asociado a un DNI.

---

## ESTADO_FIN

El chatbot finaliza la operación actual.
