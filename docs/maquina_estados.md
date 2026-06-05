# Máquina de Estados

## Flujo de Reserva de Turnos

### ESTADO_MENU

Muestra las opciones principales del sistema:

* Reservar turno
* Consultar turno
* Cancelar turno
* Salir

---

### ESTADO_PEDIR_DNI

Solicita al usuario su número de DNI.

---

### ESTADO_VERIFICAR_PACIENTE

Verifica si el DNI se encuentra registrado.

#### Transiciones

* Si existe → ESTADO_PEDIR_FECHA
* Si no existe → ESTADO_REGISTRAR_NOMBRE

---

### ESTADO_REGISTRAR_NOMBRE

Solicita el nombre del paciente.

---

### ESTADO_REGISTRAR_APELLIDO

Solicita el apellido del paciente.

---

### ESTADO_REGISTRAR_TELEFONO

Solicita el teléfono del paciente.

---

### ESTADO_GUARDAR_PACIENTE

Registra el nuevo paciente en `pacientes.csv`.

#### Transiciones

* Continuar → ESTADO_PEDIR_FECHA

---

### ESTADO_PEDIR_FECHA

Muestra los próximos 5 días hábiles disponibles para la reserva.

---

### ESTADO_MOSTRAR_HORARIOS

Muestra los horarios disponibles para la fecha seleccionada.

Horarios:

* 09:00
* 09:30
* 10:00
* 10:30
* 11:00
* 11:30

---

### ESTADO_CONFIRMAR_RESERVA

Muestra el resumen del turno y solicita confirmación.

#### Transiciones

* Confirmar → ESTADO_GUARDAR_TURNO
* Cancelar → ESTADO_FIN

---

### ESTADO_GUARDAR_TURNO

Registra el turno en `turnos.csv`.

---

### ESTADO_FIN

Finaliza la operación actual.
