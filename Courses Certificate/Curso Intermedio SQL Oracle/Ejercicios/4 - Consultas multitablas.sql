/* Práctica */
/* 1. Muestre nombre de empleados y nombre de su departamento */
SELECT
    e.first_name,
    e.last_name,
    d.department_name
FROM
    hr.employees e
JOIN
    hr.departments d ON e.department_id = d.department_id;
/* 2. Muestre empleados y ciudad donde trabajan */
SELECT
    e.first_name,
    e.last_name,
    l.city
FROM
    hr.employees e
JOIN
    hr.departments d ON e.department_id = d.department_id
JOIN
    hr.locations l ON d.location_id = l.location_id;
/* 3. Muestre empleados y nombre del país donde trabajan */
SELECT
    e.first_name,
    e.last_name,
    c.country_name
FROM
    hr.employees e
JOIN
    hr.departments d ON e.department_id = d.department_id
JOIN
    hr.locations l ON d.location_id = l.location_id
JOIN
    hr.countries c ON l.country_id = c.country_id;
/* 4. Muestre empleados y nombre de su puesto (job_title) */
SELECT
    e.first_name,
    e.last_name,
    j.job_title
FROM
    hr.employees e
JOIN
    hr.jobs j ON e.job_id = j.job_id;
/* 5. Muestre empleados y región donde trabajan */
SELECT
    e.first_name,
    e.last_name,
    r.region_name
FROM
    hr.employees e
JOIN
    hr.departments d ON e.department_id = d.department_id
JOIN
    hr.locations l ON d.location_id = l.location_id
JOIN
    hr.countries c ON l.country_id = c.country_id
JOIN
    hr.regions r ON c.region_id = r.region_id;
/* 6. Muestre empleados que trabajan en ciudades de Canadá */
SELECT
    e.first_name,
    e.last_name,
    l.city
FROM
    hr.employees e
JOIN
    hr.departments d ON e.department_id = d.department_id
JOIN
    hr.locations l ON d.location_id = l.location_id
JOIN
    hr.countries c ON l.country_id = c.country_id
WHERE
    c.country_name = 'Canada';
/* 7. Desarrolle una consulta que liste el código, nombre y apellido de los empleados y sus respectivos jefes con título Empleado y Jefe */
SELECT
    e.employee_id    AS "ID Empleado",
    e.first_name     AS "Nombre Empleado",
    e.last_name      AS "Apellido Empleado",
    m.employee_id    AS "ID Jefe",
    m.first_name     AS "Nombre Jefe",
    m.last_name      AS "Apellido Jefe"
FROM
    hr.employees e
JOIN
    hr.employees m ON e.manager_id = m.employee_id;
/* 8. Muestre empleados cuyo departamento tiene más de 5 empleados, y la ubicación del departamento */
SELECT
    e.first_name,
    e.last_name,
    d.department_name,
    l.city,
    l.street_address
FROM
    hr.employees e
JOIN
    hr.departments d ON e.department_id = d.department_id
JOIN
    hr.locations l ON d.location_id = l.location_id
WHERE
    e.department_id IN (
        SELECT
            department_id
        FROM
            hr.employees
        GROUP BY
            department_id
        HAVING
            COUNT(*) > 5
    );
/* 9. Muestre empleados que trabajan en regiones llamadas 'Americas'*/ 
SELECT
    e.first_name,
    e.last_name,
    r.region_name
FROM
    hr.employees e
JOIN
    hr.departments d ON e.department_id = d.department_id
JOIN
    hr.locations l ON d.location_id = l.location_id
JOIN
    hr.countries c ON l.country_id = c.country_id
JOIN
    hr.regions r ON c.region_id = r.region_id
WHERE
    r.region_name = 'Americas';
/* 10. Desarrolle una consulta que liste los países por región; los datos que debe mostrar son: el código de la región y nombre de la región con los nombres de sus países */
SELECT
    r.region_id,
    r.region_name,
    c.country_name
FROM
    hr.regions r
JOIN
    hr.countries c ON r.region_id = c.region_id
ORDER BY
    r.region_name,
    c.country_name;
/* 11. Realice una consulta que muestre el código, nombre, apellido, inicio y fin del historial de trabajo de los empleados */
SELECT
    e.employee_id,
    e.first_name,
    e.last_name,
    jh.start_date,
    jh.end_date
FROM
    hr.employees e
JOIN
    hr.job_history jh ON e.employee_id = jh.employee_id;
/* 12. Elabore una consulta que muestre el nombre y apellido del empleado con título Empleado, el salario, porcentaje de comisión, la comisión y salario total. Elabore una consulta que liste nombre del trabajo y el salario de los empleados que son jefes, cuyo código es 100 o 125 y cuyo salario sea mayor de 6000 */
/* PARTE 1: */
SELECT
    first_name || ' ' || last_name AS "Empleado",
    salary,
    commission_pct,
    ( salary * NVL(commission_pct, 0) ) AS "Comision",
    ( salary + (salary * NVL(commission_pct, 0)) ) AS "Salario Total"
FROM
    hr.employees;
/* PARTE 2: */
SELECT
    j.job_title,
    e.salary
FROM
    hr.employees e
JOIN
    hr.jobs j ON e.job_id = j.job_id
WHERE
    e.employee_id IN (100, 125) AND e.salary > 6000;
/* 13. Realice una consulta que muestre el código, nombre de la región y el nombre de los países que se encuentran en “Asia” */ 
SELECT
    r.region_id,
    r.region_name,
    c.country_name
FROM
    hr.regions r
JOIN
    hr.countries c ON r.region_id = c.region_id
WHERE
    r.region_name = 'Asia';
/* 14. Desarrolle una consulta que liste el código de la localidad, la ciudad y el nombre del departamento de únicamente de los que se encuentran fuera de estados unidos (US) */
SELECT
    l.location_id,
    l.city,
    d.department_name
FROM
    hr.departments d
JOIN
    hr.locations l ON d.location_id = l.location_id
WHERE
    l.country_id <> 'US';
/* 15. Elabore una consulta que liste el código de la región y nombre de la región, código de la localidad, la ciudad, código del país y nombre del país, de solamente de las localidades mayores a 2400 */
SELECT
    r.region_id,
    r.region_name,
    l.location_id,
    l.city,
    c.country_id,
    c.country_name
FROM
    hr.locations l
JOIN
    hr.countries c ON l.country_id = c.country_id
JOIN
    hr.regions r ON c.region_id = r.region_id
WHERE
    l.location_id > 2400;
/* 16. Desarrolle una consulta donde muestre el código de región con un alias de Región, el nombre de la región con una etiqueta Nombre Región, que muestre una cadena string (concatenación) que diga la siguiente frase “Código País: CA Nombre: Canadá”, CA es el código de país y Canadá es el nombre del país con etiqueta País, el código de localización con etiqueta Localización, la dirección de calle con etiqueta Dirección y el código postal con etiqueta “Código Postal”, esto a su vez no deben aparecer código postal que sean nulos */
SELECT
    r.region_id AS "Región",
    r.region_name AS "Nombre Región",
    'Código País: ' || c.country_id || ' Nombre: ' || c.country_name AS "País",
    l.location_id AS "Localización",
    l.street_address AS "Dirección",
    l.postal_code AS "Código Postal"
FROM
    hr.locations l
JOIN
    hr.countries c ON l.country_id = c.country_id
JOIN
    hr.regions r ON c.region_id = r.region_id
WHERE
    l.postal_code IS NOT NULL;
/* 17. Desarrolle una consulta que muestre el nombre de la región, el nombre del país, el estado de la provincia, el código de los empleados que son manager, el nombre y apellido del empleado que es manager de los países del Reino Unido (UK), Estados Unidos de América (US), respectivamente de los estados de Washington y Oxford */
SELECT
    r.region_name,
    c.country_name,
    l.state_province,
    e.employee_id,
    e.first_name,
    e.last_name
FROM
    hr.employees e
JOIN
    hr.departments d ON e.department_id = d.department_id
JOIN
    hr.locations l ON d.location_id = l.location_id
JOIN
    hr.countries c ON l.country_id = c.country_id
JOIN
    hr.regions r ON c.region_id = r.region_id
WHERE
    e.employee_id IN (
        SELECT DISTINCT
            manager_id
        FROM
            hr.employees
        WHERE
            manager_id IS NOT NULL
    )
    AND l.country_id IN ('UK', 'US')
    AND l.state_province IN ('Washington', 'Oxford');
/* 18. Realice una consulta que muestre el nombre y apellido de los empleados que trabajan para departamentos que están localizados en países cuyo nombre comienza con la letra C, que muestre el nombre del país */
SELECT
    e.first_name,
    e.last_name,
    c.country_name
FROM
    hr.employees e
JOIN
    hr.departments d ON e.department_id = d.department_id
JOIN
    hr.locations l ON d.location_id = l.location_id
JOIN
    hr.countries c ON l.country_id = c.country_id
WHERE
    c.country_name LIKE 'C%';