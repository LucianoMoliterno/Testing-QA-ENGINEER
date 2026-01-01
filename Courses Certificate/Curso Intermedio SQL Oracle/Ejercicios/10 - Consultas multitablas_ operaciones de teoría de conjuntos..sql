/* Ejercicios prácticos */
/* 1. Listar todos los job_id que aparecen en employees y en job_history */
SELECT job_id FROM hr.employees
UNION
SELECT job_id FROM hr.job_history;
/* 2. Mostrar los department_id que están en departments pero no en employees */
SELECT department_id FROM hr.departments
MINUS
SELECT department_id FROM hr.employees;
---------------------------------------------------------------------------------
/* Actividades para clase */
/* 1. Comparar resultados entre UNION y UNION ALL con COUNT(*) */
-- Conteo sin duplicados
SELECT COUNT(*) 
FROM (
    SELECT manager_id FROM hr.employees
    UNION
    SELECT employee_id FROM hr.employees
);

-- Conteo con duplicados
SELECT COUNT(*) 
FROM (
    SELECT manager_id FROM hr.employees
    UNION ALL
    SELECT employee_id FROM hr.employees
);
/* 2. Reescribir INTERSECT usando INNER JOIN */
-- Consulta original (basada en el ejemplo del documento )
SELECT employee_id FROM hr.employees
INTERSECT
SELECT manager_id FROM hr.employees;

-- Reescrito con INNER JOIN y DISTINCT
SELECT DISTINCT e.employee_id
FROM hr.employees e
INNER JOIN hr.employees m ON e.employee_id = m.manager_id;
/* 3. Reescribir MINUS usando NOT IN o NOT EXISTS */
-- Consulta original (basada en el ejemplo del documento )
SELECT employee_id FROM hr.employees
MINUS
SELECT manager_id FROM hr.employees;

-- Reescrito con NOT IN
SELECT employee_id
FROM hr.employees
WHERE employee_id NOT IN (
    SELECT manager_id 
    FROM hr.employees 
    WHERE manager_id IS NOT NULL
);

-- Reescrito con NOT EXISTS (generalmente preferido por su manejo de NULLs):
SELECT e.employee_id
FROM hr.employees e
WHERE NOT EXISTS (
    SELECT 1
    FROM hr.employees m
    WHERE m.manager_id = e.employee_id
);