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

Si el paciente no se encuentra registrado, el chatbot deberá ofrecer la posibilidad de registrarlo.

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

Los turnos solo podrán asignarse de lunes a viernes.

### RN-09

Los turnos solo podrán asignarse dentro del horario de atención definido por el consultorio.

### RN-10

La duración de cada turno será de 30 minutos.

### RN-11

Los horarios disponibles serán:

* 09:00
* 09:30
* 10:00
* 10:30
* 11:00
* 11:30

### RN-12

No podrán existir dos turnos reservados para la misma fecha y horario.

### RN-13

El usuario deberá confirmar la reserva antes de que el turno sea registrado.

### RN-14

Si el horario seleccionado no se encuentra disponible, el sistema deberá informar la situación y permitir seleccionar otro horario.

---

## Consulta de Turnos

### RN-15

Un paciente podrá consultar sus turnos utilizando su DNI.

---

## Cancelación de Turnos

### RN-16

Un paciente podrá cancelar un turno previamente reservado.

### RN-17

Solo podrán cancelarse turnos asociados al DNI ingresado.

---

## Validaciones y Manejo de Errores

### RN-18

Si el usuario ingresa una opción inválida en el menú, el sistema deberá solicitar una nueva selección.

### RN-19

Si el usuario ingresa datos vacíos, el sistema deberá solicitar nuevamente la información.

### RN-20

Si el usuario ingresa un DNI inválido, el sistema deberá informar el error y solicitar un nuevo ingreso.

### RN-21

Si el usuario decide no confirmar una reserva, el turno no deberá registrarse.

---

## Persistencia de Datos

### RN-22

Todo paciente registrado deberá almacenarse en el archivo `pacientes.csv`.

### RN-23

Toda reserva confirmada deberá almacenarse en el archivo `turnos.csv`.

### RN-24

Toda cancelación deberá actualizar la información almacenada en `turnos.csv`.

