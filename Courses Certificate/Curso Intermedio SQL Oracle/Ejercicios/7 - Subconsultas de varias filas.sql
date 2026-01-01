/* ----Prácticas---- */
/* 1. Muestre nombre de empleados y nombre de su departamento */
SELECT e.first_name, e.last_name,
       (SELECT d.department_name
        FROM hr.departments d
        WHERE d.department_id = e.department_id) AS department_name
FROM hr.employees e;
/* 2. Muestre empleados y ciudad donde trabajan */
SELECT e.first_name, e.last_name,
       (SELECT l.city
        FROM hr.locations l
        WHERE l.location_id = (SELECT d.location_id
                               FROM hr.departments d
                               WHERE d.department_id = e.department_id)) AS city
FROM hr.employees e;
/* 3. Muestre empleados y nombre del país donde trabajan */
SELECT e.first_name, e.last_name,
       (SELECT c.country_name
        FROM hr.countries c
        WHERE c.country_id = (SELECT l.country_id
                              FROM hr.locations l
                              WHERE l.location_id = (SELECT d.location_id
                                                     FROM hr.departments d
                                                     WHERE d.department_id = e.department_id))) AS country_name
FROM hr.employees e;
/* 4. Muestre empleados y nombre de su puesto (job_title) */
SELECT e.first_name, e.last_name,
       (SELECT j.job_title
        FROM hr.jobs j
        WHERE j.job_id = e.job_id) AS job_title
FROM hr.employees e;
/* 5. Muestre empleados y región donde trabajan */
SELECT e.first_name, e.last_name,
       (SELECT r.region_name
        FROM hr.regions r
        WHERE r.region_id = (SELECT c.region_id
                             FROM hr.countries c
                             WHERE c.country_id = (SELECT l.country_id
                                                   FROM hr.locations l
                                                   WHERE l.location_id = (SELECT d.location_id
                                                                            FROM hr.departments d
                                                                            WHERE d.department_id = e.department_id)))) AS region_name
FROM hr.employees e;
/* 6. Muestre empleados que trabajan en ciudades de Canadá */
SELECT e.first_name, e.last_name
FROM hr.employees e
WHERE e.department_id IN
      (SELECT d.department_id
       FROM hr.departments d
       WHERE d.location_id IN
             (SELECT l.location_id
              FROM hr.locations l
              WHERE l.country_id = 'CA'));
/* 7. Desarrolle una consulta que liste el código, nombre y apellido de los empleados y sus respectivos jefes con título Empleado y Jefe */
SELECT e.employee_id AS "Empleado ID",
       e.first_name AS "Empleado Nombre",
       e.last_name AS "Empleado Apellido",
       (SELECT m.first_name || ' ' || m.last_name
        FROM hr.employees m
        WHERE m.employee_id = e.manager_id) AS "Jefe"
FROM hr.employees e;
/* 8. Muestre empleados cuyo departamento tiene más de 5 empleados, y la ubicación del departamento */
SELECT e.first_name, e.last_name,
       (SELECT l.city || ', ' || l.street_address
        FROM hr.locations l
        WHERE l.location_id = (SELECT d.location_id
                               FROM hr.departments d
                               WHERE d.department_id = e.department_id)) AS "Ubicación"
FROM hr.employees e
WHERE e.department_id IN
      (SELECT emp_dept.department_id
       FROM hr.employees emp_dept
       GROUP BY emp_dept.department_id
       HAVING COUNT(*) > 5);
/* 9. Muestre empleados que trabajan en regiones llamadas 'Americas' */
SELECT e.first_name, e.last_name
FROM hr.employees e
WHERE e.department_id IN
      (SELECT d.department_id
       FROM hr.departments d
       WHERE d.location_id IN
             (SELECT l.location_id
              FROM hr.locations l
              WHERE l.country_id IN
                    (SELECT c.country_id
                     FROM hr.countries c
                     WHERE c.region_id =
                           (SELECT r.region_id
                            FROM hr.regions r
                            WHERE r.region_name = 'Americas'))));
/* 10. Desarrolle una consulta que liste los países por región; los datos que debe mostrar son: el código de la región y nombre de la región con los nombres de sus países */
SELECT c.country_name,
       (SELECT r.region_id
        FROM hr.regions r
        WHERE r.region_id = c.region_id) AS region_id,
       (SELECT r.region_name
        FROM hr.regions r
        WHERE r.region_id = c.region_id) AS region_name
FROM hr.countries c
ORDER BY region_name, c.country_name;
/* 11. Realice una consulta que muestre el código, nombre, apellido, inicio y fin del historial de trabajo de los empleados */
SELECT jh.employee_id,
       (SELECT e.first_name
        FROM hr.employees e
        WHERE e.employee_id = jh.employee_id) AS first_name,
       (SELECT e.last_name
        FROM hr.employees e
        WHERE e.employee_id = jh.employee_id) AS last_name,
       jh.start_date,
       jh.end_date
FROM hr.job_history jh;
/* 12. Elabore una consulta que muestre el nombre y apellido del empleado con título Empleado, el salario, porcentaje de comisión, la comisión y salario total. Elabore una consulta que liste nombre del trabajo y el salario de los empleados que son jefes, cuyo código es 100 o 125 y cuyo salario sea mayor de 6000 */
SELECT first_name || ' ' || last_name AS "Empleado",
       salary AS "Salario",
       commission_pct AS "Porcentaje Comisión",
       salary * NVL(commission_pct, 0) AS "Comisión",
       salary * (1 + NVL(commission_pct, 0)) AS "Salario Total"
FROM hr.employees;
/* 13. Realice una consulta que muestre el código, nombre de la región y el nombre de los países que se encuentran en “Asia” */
SELECT (SELECT j.job_title
        FROM hr.jobs j
        WHERE j.job_id = e.job_id) AS job_title,
       e.salary
FROM hr.employees e
WHERE e.employee_id IN (SELECT DISTINCT manager_id
                        FROM hr.employees
                        WHERE manager_id IS NOT NULL)
  AND e.employee_id IN (100, 125)
  AND e.salary > 6000;
/* 14. Desarrolle una consulta que liste el código de la localidad, la ciudad y el nombre del departamento de únicamente de los que se encuentran fuera de estados unidos (US) */
SELECT d.department_name,
       l.location_id,
       l.city
FROM hr.departments d
JOIN hr.locations l ON d.location_id = l.location_id
WHERE l.country_id <> 'US';
-- Alternativa 100% con subconsultas (como pide la práctica ):
SELECT d.department_name,
       d.location_id,
       (SELECT l.city
        FROM hr.locations l
        WHERE l.location_id = d.location_id) AS city
FROM hr.departments d
WHERE d.location_id IN (SELECT l.location_id
                        FROM hr.locations l
                        WHERE l.country_id <> 'US');
/* 15. Elabore una consulta que liste el código de la región y nombre de la región, código de la localidad, la ciudad, código del país y nombre del país, de solamente de las localidades mayores a 2400 */
SELECT
    l.location_id,
    l.city,
    l.country_id,
    (SELECT c.country_name
     FROM hr.countries c
     WHERE c.country_id = l.country_id) AS country_name,
    (SELECT r.region_id
     FROM hr.regions r
     WHERE r.region_id = (SELECT c.region_id
                          FROM hr.countries c
                          WHERE c.country_id = l.country_id)) AS region_id,
    (SELECT r.region_name
     FROM hr.regions r
     WHERE r.region_id = (SELECT c.region_id
                          FROM hr.countries c
                          WHERE c.country_id = l.country_id)) AS region_name
FROM hr.locations l
WHERE l.location_id > 2400;
/* 16. Desarrolle una consulta donde muestre el código de región con un alias de Región, el nombre de la región con una etiqueta Nombre Región, que muestre una cadena string (concatenación) que diga la siguiente frase “Código País: CA Nombre: Canadá”, CA es el código de país y Canadá es el nombre del país con etiqueta País, el código de localización con etiqueta Localización, la dirección de calle con etiqueta Dirección y el código postal con etiqueta “Código Postal”, esto a su vez no deben aparecer código postal que sean nulos */
SELECT
    r.region_id AS "Región",
    r.region_name AS "Nombre Región",
    'Código País: ' || l.country_id || ' Nombre: ' || c.country_name AS "País",
    l.location_id AS "Localización",
    l.street_address AS "Dirección",
    l.postal_code AS "Código Postal"
FROM hr.locations l
JOIN hr.countries c ON l.country_id = c.country_id
JOIN hr.regions r ON c.region_id = r.region_id
WHERE l.postal_code IS NOT NULL;
/* 17. Desarrolle una consulta que muestre el nombre de la región, el nombre del país, el estado de la provincia, el código de los empleados que son manager, el nombre y apellido del empleado que es manager de los países del Reino Unido (UK), Estados Unidos de América (US), respectivamente de los estados de Washington y Oxford */
SELECT
    r.region_name,
    c.country_name,
    l.state_province,
    e.employee_id AS manager_employee_id,
    e.first_name,
    e.last_name
FROM hr.employees e
JOIN hr.departments d ON e.department_id = d.department_id
JOIN hr.locations l ON d.location_id = l.location_id
JOIN hr.countries c ON l.country_id = c.country_id
JOIN hr.regions r ON c.region_id = r.region_id
WHERE e.employee_id IN (SELECT DISTINCT manager_id
                        FROM hr.employees
                        WHERE manager_id IS NOT NULL)
  AND l.country_id IN ('UK', 'US')
  AND l.state_province IN ('Washington', 'Oxford');
/* 18. Realice una consulta que muestre el nombre y apellido de los empleados que trabajan para departamentos que están localizados en países cuyo nombre comienza con la letra C, que muestre el nombre del país */
SELECT e.first_name, e.last_name,
       (SELECT c.country_name
        FROM hr.countries c
        WHERE c.country_id = (SELECT l.country_id
                              FROM hr.locations l
                              WHERE l.location_id = (SELECT d.location_id
                                                     FROM hr.departments d
                                                     WHERE d.department_id = e.department_id))) AS country_name
FROM hr.employees e
WHERE e.department_id IN
      (SELECT d.department_id
       FROM hr.departments d
       WHERE d.location_id IN
             (SELECT l.location_id
              FROM hr.locations l
              WHERE l.country_id IN
                    (SELECT c.country_id
                     FROM hr.countries c
                     WHERE c.country_name LIKE 'C%')));

/* ----Práctica OUTER JOIN---- */
/* 1. Cree un reporte que muestre apellido de empleados y su identificador junto con el su jefe, incluido el jefe de todos que no tiene superior; ordene por identificador de empleado */
SELECT e.last_name AS "Empleado Apellido",
       e.employee_id AS "Empleado ID",
       m.last_name AS "Jefe Apellido",
       m.employee_id AS "Jefe ID"
FROM hr.employees e
LEFT OUTER JOIN hr.employees m ON e.manager_id = m.employee_id
ORDER BY e.employee_id;
/* 2. Muestre todos los empleados y datos de sus departamentos, aun los que no pertenezcan a ninguno */
SELECT e.first_name, e.last_name, d.*
FROM hr.employees e
LEFT OUTER JOIN hr.departments d ON e.department_id = d.department_id;
/* 3. Muestre todos los departamentos y datos de sus empleados, incluidos aquellos que no tengan empleados */
SELECT d.department_name, e.first_name, e.last_name
FROM hr.departments d
LEFT OUTER JOIN hr.employees e ON d.department_id = e.department_id;
/* 4. Muestre todos los departamentos y todos los empleados en una única consulta */
SELECT e.first_name, e.last_name, d.department_name
FROM hr.employees e
FULL OUTER JOIN hr.departments d ON e.department_id = d.department_id;