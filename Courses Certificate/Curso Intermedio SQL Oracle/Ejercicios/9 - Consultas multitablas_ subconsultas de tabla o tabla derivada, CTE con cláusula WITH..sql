/* Subconsultas de tabla o tabla derivada + Subconsulta en JOIN */
/* 1. Empleados con salario mayor al promedio de su departamento (usando tabla derivada) */
SELECT e.first_name, e.last_name, e.salary, e.department_id
FROM hr.employees e
JOIN (
    SELECT department_id, AVG(salary) AS avg_sal
    FROM hr.employees
    GROUP BY department_id
) dept_avg ON e.department_id = dept_avg.department_id -- "AS" eliminado
WHERE e.salary > dept_avg.avg_sal;
/* 2. Cantidad de empleados por departamento */
SELECT department_id, COUNT(*) AS cantidad_empleados
FROM hr.employees
GROUP BY department_id
ORDER BY department_id;
/* 3. Departamentos con más de 3 empleados */
SELECT department_id, cantidad
FROM (
    SELECT department_id, COUNT(*) AS cantidad
    FROM hr.employees
    GROUP BY department_id
) resumen_dept -- "AS" eliminado
WHERE cantidad > 3;
/* 4. Top 3 cargos con mayor promedio salarial */
SELECT job_id, promedio_sal
FROM (
    SELECT job_id, AVG(salary) AS promedio_sal
    FROM hr.employees
    GROUP BY job_id
    ORDER BY promedio_sal DESC
) top_cargos -- "AS" eliminado
FETCH FIRST 3 ROWS ONLY;
/* 5. Empleados que trabajan en departamentos con más de 5 empleados */
SELECT e.first_name, e.last_name, e.department_id
FROM hr.employees e
JOIN (
    SELECT department_id
    FROM hr.employees
    GROUP BY department_id
    HAVING COUNT(*) > 5
) dept_grandes ON e.department_id = dept_grandes.department_id; -- "AS" eliminado
------------------------------------------------------------------------------------
/* Hoja de Ejercicios – Conversión entre Tabla Derivada y CTE */
/* Top 5 salarios */ 
WITH top_salaries AS (
    SELECT first_name, last_name, salary
    FROM hr.employees
    ORDER BY salary DESC
)
SELECT *
FROM top_salaries
FETCH FIRST 5 ROWS ONLY;
/* Promedio salarial por cargo */
SELECT e.first_name, e.last_name, e.salary, e.job_id
FROM hr.employees e
JOIN (
    -- Esta es la tabla derivada
    SELECT job_id, AVG(salary) AS avg_sal
    FROM hr.employees
    GROUP BY job_id
) avg_table ON e.job_id = avg_table.job_id
WHERE e.salary > avg_table.avg_sal;
/* Departamentos con más de 3 empleados */
WITH resumen AS (
    SELECT department_id, COUNT(*) AS cantidad
    FROM hr.employees
    GROUP BY department_id
)
SELECT department_id, cantidad
FROM resumen
WHERE cantidad > 3;
/* Empleados en departamentos activos */
SELECT e.first_name, e.last_name, e.department_id
FROM hr.employees e
JOIN (
    -- Esta es la tabla derivada
    SELECT department_id
    FROM hr.employees
    GROUP BY department_id
    HAVING COUNT(*) > 5
) active_depts ON e.department_id = active_depts.department_id; 
/* Cargos con mayor promedio salarial */
WITH top_cargos AS (
    SELECT job_id, AVG(salary) AS promedio
    FROM hr.employees
    GROUP BY job_id
    ORDER BY promedio DESC
)
SELECT *
FROM top_cargos
FETCH FIRST 3 ROWS ONLY;