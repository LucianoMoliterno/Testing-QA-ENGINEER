-- 1. 🔍 Empleados con salario superior al promedio de su departamento
-- Muestra el employee_id, first_name, salary y department_id de los empleados cuyo salario es superior al salario promedio de su propio departamento.
-- 💡 Usa una subconsulta correlacionada.
SELECT 
    employee_id, 
    first_name, 
    salary, 
    department_id
FROM 
    hr.employees e1
WHERE 
    salary > (SELECT AVG(e2.salary) 
              FROM hr.employees e2 
              WHERE e2.department_id = e1.department_id)
ORDER BY
    department_id, salary DESC;

----------------------
-- 2. 🧩 Departamentos sin empleados
-- Lista los department_id y department_name de los departamentos que no tienen empleados asignados.
-- 💡 Usa LEFT JOIN y filtra con IS NULL.
SELECT 
    d.department_id, 
    d.department_name
FROM 
    hr.departments d
LEFT JOIN 
    hr.employees e ON d.department_id = e.department_id
WHERE 
    e.employee_id IS NULL
ORDER BY
    d.department_name;
----------------------------------
-- 3. 🧮 Salario total por departamento (solo si supera 20,000)
-- Muestra el department_id y el total de salarios (SUM(salary)) de cada departamento, pero solo si ese total supera 20,000.
-- 💡 Usa GROUP BY y HAVING.
SELECT 
    department_id, 
    SUM(salary) AS total_salary
FROM 
    hr.employees
GROUP BY 
    department_id
HAVING 
    SUM(salary) > 20000
ORDER BY
    total_salary DESC;

---------------------------------
-- 4. 🧭 Empleados que trabajan en la misma ciudad que su manager
-- Muestra el employee_id, first_name, manager_id y la ciudad (city) si el empleado y su manager trabajan en la misma ciudad.
-- 💡 Requiere JOIN entre employees, departments y locations.
SELECT 
    e.employee_id, 
    e.first_name, 
    e.manager_id, 
    l_e.city 
FROM 
    hr.employees e
JOIN 
    hr.departments d_e ON e.department_id = d_e.department_id
JOIN 
    hr.locations l_e ON d_e.location_id = l_e.location_id
JOIN 
    hr.employees m ON e.manager_id = m.employee_id
JOIN 
    hr.departments d_m ON m.department_id = d_m.department_id
JOIN 
    hr.locations l_m ON d_m.location_id = l_m.location_id
WHERE 
    l_e.city = l_m.city;

---------------------------------------------------------------------
-- 5. 🕵️‍♂️ Empleados con el mismo trabajo que el empleado 105
-- Muestra el employee_id, first_name, job_id y salary de todos los empleados que tienen el mismo job_id que el empleado con employee_id = 105, excluyendo al propio 105.
-- 💡 Usa una subconsulta simple en el WHERE.
SELECT 
    employee_id, 
    first_name, 
    job_id, 
    salary
FROM 
    hr.employees
WHERE 
    job_id = (SELECT job_id 
              FROM hr.employees 
              WHERE employee_id = 105)
AND 
    employee_id <> 105;