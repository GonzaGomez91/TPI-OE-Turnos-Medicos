# Reglas de Negocio

## Configuración del Consultorio

* El consultorio cuenta con un único médico.
* La atención se realiza de lunes a viernes.
* El horario de atención es de 09:00 a 12:00 hs.
* La duración de cada turno es de 30 minutos.

### Horarios Disponibles

* 09:00
* 09:30
* 10:00
* 10:30
* 11:00
* 11:30

---

## Gestión de Pacientes

### RN-01

Todo paciente debe identificarse mediante su DNI.

### RN-02

El DNI debe contener únicamente caracteres numéricos.

### RN-03

El sistema debe verificar si el paciente se encuentra registrado.

### RN-04

Si el paciente no se encuentra registrado, el chatbot deberá permitir su registro.

### RN-05

Para registrar un nuevo paciente se solicitarán los siguientes datos:

* DNI
* Nombre y apellido
* Teléfono

### RN-06

No podrán existir dos pacientes registrados con el mismo DNI.

---

## Reserva de Turnos

### RN-07

Solo los pacientes registrados podrán reservar turnos.

### RN-08

Los turnos solo podrán asignarse en las fechas ofrecidas por el sistema.

### RN-09

Los turnos solo podrán asignarse dentro de los horarios disponibles definidos por el sistema.

### RN-10

No podrán existir dos turnos reservados para la misma fecha y horario.

### RN-11

El usuario deberá confirmar la reserva antes de que el turno sea registrado.

### RN-12

Si el turno seleccionado deja de estar disponible durante el proceso de reserva, el sistema deberá informar la situación y permitir seleccionar otro turno.

---

## Validaciones y Manejo de Errores

### RN-13

Si el usuario ingresa una opción inválida en el menú, el sistema deberá solicitar una nueva selección.

### RN-14

Si el usuario ingresa datos vacíos, el sistema deberá solicitar nuevamente la información.

### RN-15

Si el usuario ingresa un DNI inválido, el sistema deberá informar el error y solicitar un nuevo ingreso.

### RN-16

Si el usuario decide no confirmar una reserva, el turno no deberá registrarse.

### RN-17

El usuario podrá cancelar la operación actual en cualquier momento mediante el comando:

```text
cancelar
```

En dicho caso, el sistema deberá regresar al menú principal sin registrar modificaciones.

---

## Persistencia de Datos

### RN-18

Todo paciente registrado deberá almacenarse en el archivo `pacientes.csv`.

### RN-19

Toda reserva confirmada deberá almacenarse en el archivo `turnos.csv`.
