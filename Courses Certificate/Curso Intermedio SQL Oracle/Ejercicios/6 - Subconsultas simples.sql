/* Practicas */
/* 1. Cree un informe que muestre el número de empleado y el apellido de todos los empleados que ganan más que el sueldo medio. Clasifique los resultados en orden ascendente de salario */
SELECT employee_id, last_name, salary
FROM hr.employees
WHERE salary > (
    /* Esta subconsulta de una sola fila calcula el salario promedio */
    SELECT AVG(salary)
    FROM hr.employees
)
ORDER BY salary ASC;
/* 2. Escriba una consulta que muestre el número de empleado y el apellido de todos los empleados que trabajen en un departamento en que haya algún empleado cuyo apellido contenga una u */
SELECT employee_id, last_name, department_id
FROM hr.employees
WHERE department_id IN (
    /* Esta subconsulta devuelve una lista (múltiples filas) de IDs de departamento */
    SELECT DISTINCT department_id
    FROM hr.employees
    WHERE last_name LIKE '%u%'
);
/* 3. El departamento de recursos humanos necesita un informe que muestre el apellido, el número de departamento y el identificador de puesto de todos los empleados cuyos identificadores de ubicación de departamento sean 1700 */
SELECT last_name, department_id, job_id
FROM hr.employees
WHERE department_id IN (
    /* La subconsulta obtiene datos de una tabla diferente (departments) */
    SELECT department_id
    FROM hr.departments
    WHERE location_id = 1700
);
/* 4. Cree un informe para recursos humanos que muestre el apellido y el salario de todos los empleados que informen a King */
SELECT last_name, salary
FROM hr.employees
WHERE manager_id IN (
    /* La subconsulta busca el ID del manager 'King' */
    /* Se usa IN por si hay más de un empleado con apellido 'King'*/
    SELECT employee_id
    FROM hr.employees
    WHERE last_name = 'King'
);
/* 5. Cree un informe para recursos humanos que muestre el número de departamento, el apellido y el identificador de puesto de todos los empleados del departamento ejecutivo (‘Executive’) */
SELECT department_id, last_name, job_id
FROM hr.employees
WHERE department_id = (
    /* Subconsulta de una sola fila para obtener el ID del departamento */
    SELECT department_id
    FROM hr.departments
    WHERE department_name = 'Executive'
);
/* 6. Modifique la consulta de la práctica 3, para mostrar el número de empleado, el apellido y el salario de todos los empleados que ganen más que el salario medio y que trabajen en un departamento con algún empleado cuyo apellido contenga una u */
/* Esta consulta combina las condiciones de las prácticas 1, 2 y 3 */
SELECT employee_id, last_name, salary
FROM hr.employees
WHERE 
    -- Condición de la Práctica 3 (ubicación 1700)
    department_id IN (
        SELECT department_id
        FROM hr.departments
        WHERE location_id = 1700
    )
    -- Condición de la Práctica 1 (salario > medio)
    AND salary > (
        SELECT AVG(salary)
        FROM hr.employees
    )
    -- Condición de la Práctica 2 (departamento con 'u')
    AND department_id IN (
        SELECT DISTINCT department_id
        FROM hr.employees
        WHERE last_name LIKE '%u%'
    );
/* 7. Desarrolle una consulta que muestre a todos los empleados que no estén trabajando en el departamento 30 y que ganen más que todos los empleados que trabajan en el departamento 30 */
SELECT employee_id, last_name, salary
FROM hr.employees
/* (department_id <> 30 OR department_id IS NULL) asegura incluir empleados sin departamento */
WHERE (department_id <> 30 OR department_id IS NULL)
  AND salary > (
    /* se aclara lo siguiente: "Más que todos" se traduce en "mayor que el MÁXIMO" */
    SELECT MAX(salary)
    FROM hr.employees
    WHERE department_id = 30
);
/* 8. Realice una consulta que muestre los empleados que son gerentes, y el número de empleados subordinados a cada uno, ordenados descendentemente por número de subordinado. Excluya a los gerentes que tienen 5 empleados subordinados o menos */
/* Esta solución requiere una subconsulta en la cláusula FROM para obtener la cuenta */
SELECT e.employee_id, e.last_name, mgr_counts.num_subordinados
FROM hr.employees e
JOIN (
    /* La subconsulta interna agrupa por gerente y filtra usando HAVING */
    SELECT manager_id, COUNT(*) AS num_subordinados
    FROM hr.employees
    WHERE manager_id IS NOT NULL
    GROUP BY manager_id
    HAVING COUNT(*) > 5 
) mgr_counts ON e.employee_id = mgr_counts.manager_id
ORDER BY mgr_counts.num_subordinados DESC;
/* 9. Desarrolle una consulta que muestre el mayor salario entre los empleados que trabajan en el departamento 30, y quiénes son los empleados que ganan ese salario */
SELECT last_name, salary, department_id
FROM hr.employees
WHERE salary = (
    /* La subconsulta busca el salario MÁXIMO solo del departamento 30 */
    SELECT MAX(salary)
    FROM hr.employees
    WHERE department_id = 30
);
/* 10. Realice una consulta que liste los empleados que están en departamentos que tienen menos de 10 empleados */
SELECT employee_id, last_name, department_id
FROM hr.employees
WHERE department_id IN (
    /* La subconsulta usa GROUP BY y HAVING para encontrar los IDs de deptos pequeños */
    SELECT department_id
    FROM hr.employees
    GROUP BY department_id
    HAVING COUNT(*) < 10
);