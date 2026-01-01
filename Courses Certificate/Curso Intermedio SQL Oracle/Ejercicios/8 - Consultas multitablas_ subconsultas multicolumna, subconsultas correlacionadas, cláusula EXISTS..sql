/* Consultas multitablas */
/* 1. Empleados que han trabajado en el mismo cargo y departamento que Steven King */
SELECT first_name, last_name, job_id, department_id
FROM hr.employees
WHERE (job_id, department_id) IN (
    SELECT job_id, department_id
    FROM hr.employees
    WHERE first_name = 'Steven' AND last_name = 'King'
)
AND (first_name <> 'Steven' OR last_name <> 'King');
/* 2. Empleados que han tenido el mismo cargo y departamento que algún registro en el historial laboral */
SELECT first_name, last_name, job_id, department_id
FROM hr.employees
WHERE (job_id, department_id) IN (
    SELECT DISTINCT job_id, department_id
    FROM hr.job_history
);
/* 3. Empleados que comparten nombre y apellido con alguien en el historial */
SELECT e.first_name, e.last_name
FROM hr.employees e
WHERE (e.first_name, e.last_name) IN (
    SELECT e_hist.first_name, e_hist.last_name
    FROM hr.employees e_hist
    JOIN hr.job_history jh ON e_hist.employee_id = jh.employee_id
);
/* 4. Departamentos que aparecen en el historial con un cargo específico (IT_PROG por ejemplo) */
SELECT department_name, department_id
FROM hr.departments
WHERE department_id IN (
    SELECT DISTINCT department_id
    FROM hr.job_history
    WHERE job_id = 'IT_PROG'
);
/* 5. Empleados que tienen el mismo cargo y jefe que algún otro empleado */
SELECT department_name, department_id
FROM hr.departments
WHERE department_id IN (
    SELECT DISTINCT department_id
    FROM hr.job_history
    WHERE job_id = 'IT_PROG'
);
/* 6. Empleados que tienen la misma combinación de cargo y departamento que los empleados con salario mayor a 10000 */
SELECT first_name, last_name, job_id, department_id
FROM hr.employees
WHERE (job_id, department_id) IN (
    SELECT DISTINCT job_id, department_id
    FROM hr.employees
    WHERE salary > 10000
);
/* 7. Departamentos donde se repite la misma combinación de cargo y empleado en el historial */
SELECT d.department_name
FROM hr.departments d
WHERE d.department_id IN (
    SELECT jh.department_id
    FROM hr.job_history jh
    GROUP BY jh.department_id, jh.employee_id, jh.job_id
    HAVING COUNT(*) > 1
);
------------------------------------------------------------------------------------------------
/* Subconsultas correlacionadas */
/* 8. Empleados con salario superior al promedio de su departamento */
SELECT e.first_name, e.last_name, e.salary, e.department_id
FROM hr.employees e
WHERE e.salary > (
    SELECT AVG(i.salary)
    FROM hr.employees i
    WHERE i.department_id = e.department_id
);
/* 9. Empleados cuyo salario es el más alto de su departamento */
SELECT e.first_name, e.last_name, e.salary, e.department_id
FROM hr.employees e
WHERE e.salary = (
    SELECT MAX(i.salary)
    FROM hr.employees i
    WHERE i.department_id = e.department_id
);
/* 10. Departamentos donde algún empleado gana más que el promedio general */
SELECT d.department_name
FROM hr.departments d
WHERE EXISTS (
    SELECT 1
    FROM hr.employees e
    WHERE e.department_id = d.department_id
    AND e.salary > (SELECT AVG(salary) FROM hr.employees)
);
/* 11. Empleados que ganan más que su jefe */
SELECT e.first_name, e.last_name, e.salary
FROM hr.employees e
WHERE e.salary > (
    SELECT m.salary
    FROM hr.employees m
    WHERE m.employee_id = e.manager_id
);
/* 12. Empleados cuyo salario es mayor que el salario promedio de los empleados con el mismo cargo */
SELECT e.first_name, e.last_name, e.salary, e.job_id
FROM hr.employees e
WHERE e.salary > (
    SELECT AVG(i.salary)
    FROM hr.employees i
    WHERE i.job_id = e.job_id
);
/* 13. Muestre empleados que tienen más años de antigüedad que el promedio de su departamento */
SELECT e.first_name, e.last_name, e.hire_date
FROM hr.employees e
WHERE (SYSDATE - e.hire_date) > (
    SELECT AVG(SYSDATE - i.hire_date)
    FROM hr.employees i
    WHERE i.department_id = e.department_id
);
/* 14. Empleados cuyo salario es mayor que el salario promedio de todos los empleados que tienen el mismo jefe */
SELECT e.first_name, e.last_name, e.salary, e.manager_id
FROM hr.employees e
WHERE e.salary > (
    SELECT AVG(i.salary)
    FROM hr.employees i
    WHERE i.manager_id = e.manager_id
);
/* 15. Empleados que comparten nombre y apellido con alguien en el historial laboral */
-- Es el mismo ejercicio que el 3 y 17.
SELECT e.first_name, e.last_name
FROM hr.employees e
WHERE (e.first_name, e.last_name) IN (
    SELECT e_hist.first_name, e_hist.last_name
    FROM hr.employees e_hist
    JOIN hr.job_history jh ON e_hist.employee_id = jh.employee_id
);
/* 16. Empleados que han tenido el mismo cargo y departamento en el pasado */
SELECT e.first_name, e.last_name
FROM hr.employees e
WHERE (e.job_id, e.department_id) IN (
    SELECT jh.job_id, jh.department_id
    FROM hr.job_history jh
    WHERE jh.employee_id = e.employee_id
);
/* 17. Empleados que comparten nombre y apellido con alguien en el historial (Solución sugerida, subconsulta con JOIN) */
-- Es el mismo ejercicio que el 3 y 15. La solución del 3 ya usa JOIN
SELECT e.first_name, e.last_name
FROM hr.employees e
WHERE (e.first_name, e.last_name) IN (
    SELECT e_hist.first_name, e_hist.last_name
    FROM hr.employees e_hist
    JOIN hr.job_history jh ON e_hist.employee_id = jh.employee_id
);
---------------------------------------------------------------------------------------
/* Cláusula EXISTS */
/* 18. Empleados que trabajan en el mismo departamento que 'Steven King' */
SELECT e.first_name, e.last_name
FROM hr.employees e
WHERE EXISTS (
    SELECT 1
    FROM hr.employees k
    WHERE k.first_name = 'Steven' AND k.last_name = 'King'
    AND k.department_id = e.department_id
)
AND (e.first_name <> 'Steven' OR e.last_name <> 'King');
/* 19. Empleados que han tenido al menos un trabajo diferente al actual */
SELECT e.first_name, e.last_name
FROM hr.employees e
WHERE EXISTS (
    SELECT 1
    FROM hr.job_history jh
    WHERE jh.employee_id = e.employee_id
    AND jh.job_id <> e.job_id
);
/* 20. Empleados que han trabajado en el departamento 90 en el pasado */
SELECT e.first_name, e.last_name
FROM hr.employees e
WHERE EXISTS (
    SELECT 1
    FROM hr.job_history jh
    WHERE jh.employee_id = e.employee_id
    AND jh.department_id = 90
);
/* 21. Liste los empleados que trabajan en departamentos donde hay al menos un empleado con salario mayor a 10000 */
SELECT e.first_name, e.last_name
FROM hr.employees e
WHERE EXISTS (
    SELECT 1
    FROM hr.employees s
    WHERE s.department_id = e.department_id
    AND s.salary > 10000
);
/* 22. Muestre los nombres de empleados que alguna vez trabajaron en un departamento distinto al actual */
SELECT e.first_name, e.last_name
FROM hr.employees e
WHERE EXISTS (
    SELECT 1
    FROM hr.job_history jh
    WHERE jh.employee_id = e.employee_id
    AND jh.department_id <> e.department_id
);
/* 23. Encuentre los empleados cuyo jefe también trabaja en el mismo departamento */
SELECT e.first_name, e.last_name
FROM hr.employees e
WHERE EXISTS (
    SELECT 1
    FROM hr.employees m
    WHERE m.employee_id = e.manager_id
    AND m.department_id = e.department_id
);
/* 24. Liste los departamentos donde algún empleado haya cambiado de puesto (job_id) según su historial */
SELECT d.department_name
FROM hr.departments d
WHERE EXISTS (
    SELECT 1
    FROM hr.employees e
    JOIN hr.job_history jh ON e.employee_id = jh.employee_id
    WHERE e.department_id = d.department_id
    AND e.job_id <> jh.job_id
);
/* 25. Liste los empleados que han trabajado en más de un departamento (según job_history) */
SELECT e.first_name, e.last_name
FROM hr.employees e
WHERE e.employee_id IN (
    SELECT jh.employee_id
    FROM hr.job_history jh
    GROUP BY jh.employee_id
    HAVING COUNT(DISTINCT jh.department_id) > 1
);
/* 26. Empleados que nunca trabajaron en el departamento 90 */
SELECT e.first_name, e.last_name
FROM hr.employees e
WHERE NOT EXISTS (
    SELECT 1
    FROM hr.job_history jh
    WHERE jh.employee_id = e.employee_id
    AND jh.department_id = 90
);
/* 27. Muestre empleados cuyo manager trabaja en el mismo departamento */
-- Es el mismo ejercicio que el 23.
SELECT e.first_name, e.last_name
FROM hr.employees e
WHERE EXISTS (
    SELECT 1
    FROM hr.employees m
    WHERE m.employee_id = e.manager_id
    AND m.department_id = e.department_id
);
/* 28. Liste empleados que han trabajado en más de un departamento */
-- Es el mismo ejercicio que el 25.
SELECT e.first_name, e.last_name
FROM hr.employees e
WHERE e.employee_id IN (
    SELECT jh.employee_id
    FROM hr.job_history jh
    GROUP BY jh.employee_id
    HAVING COUNT(DISTINCT jh.department_id) > 1
);
/* 29. Filtre los departamentos donde algún empleado cambió de puesto */
-- Es el mismo ejercicio que el 24.
SELECT d.department_name
FROM hr.departments d
WHERE EXISTS (
    SELECT 1
    FROM hr.employees e
    JOIN hr.job_history jh ON e.employee_id = jh.employee_id
    WHERE e.department_id = d.department_id
    AND e.job_id <> jh.job_id
);
/* 30. Muestre empleados que alguna vez trabajaron en el departamento 90 */
-- Es el mismo ejercicio que el 20 (y el opuesto al 26).
SELECT e.first_name, e.last_name
FROM hr.employees e
WHERE EXISTS (
    SELECT 1
    FROM hr.job_history jh
    WHERE jh.employee_id = e.employee_id
    AND jh.department_id = 90
);
/* 31. Empleados que han trabajado en el mismo cargo y departamento más de una vez (Solución sugerida doble subconsulta anidada) */
SELECT e.first_name, e.last_name
FROM hr.employees e
WHERE EXISTS (
    SELECT 1
    FROM hr.job_history jh1
    WHERE jh1.employee_id = e.employee_id
    AND EXISTS (
        SELECT 1
        FROM hr.job_history jh2
        WHERE jh2.employee_id = jh1.employee_id
        AND jh2.job_id = jh1.job_id
        AND jh2.department_id = jh1.department_id
        AND jh2.start_date <> jh1.start_date -- Clave para asegurar que es un registro diferente
    )
);