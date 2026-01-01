/* AL NO EXISTIR EJERCICIOS, DECIDI HACER ALGUNOS POR MI CUENTA PARA COMPLETAR LA TAREA */

/* LEFT OUTER JOIN */
/* Mostrar una lista de todos los empleados y el nombre de su departamento. La lista debe incluir a los empleados aunque no tengan un departamento asignado */
SELECT
    e.last_name,
    e.department_id,
    d.department_name
FROM
    hr.employees e
LEFT OUTER JOIN
    hr.departments d ON (e.department_id = d.department_id);
/* RIGHT OUTER JOIN */
/* Mostrar una lista de todos los departamentos y los apellidos de los empleados que trabajan en ellos. La lista debe incluir a los departamentos aunque no tengan empleados */
SELECT
    e.last_name,
    d.department_id,
    d.department_name
FROM
    hr.employees e
RIGHT OUTER JOIN
    hr.departments d ON (e.department_id = d.department_id);
/* FULL OUTER JOIN */
/* Crear una consulta que muestre todos los empleados y todos los departamentos, incluyendo empleados sin departamento y departamentos sin empleados */
SELECT
    e.last_name,
    d.department_id,
    d.department_name
FROM
    hr.employees e
FULL OUTER JOIN
    hr.departments d ON (e.department_id = d.department_id);
/* CROSS JOIN (Producto Cartesiano) */
/* Generar un informe que muestre todas las combinaciones posibles entre cada empleado y cada departamento */
SELECT
    e.last_name,
    d.department_name
FROM
    hr.employees e
CROSS JOIN
    hr.departments d;