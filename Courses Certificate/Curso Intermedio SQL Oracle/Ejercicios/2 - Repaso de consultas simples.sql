/* Expresiones aritméticas en el SELECT */
/* 1. Calcule el salario anual de cada empleado */
SELECT last_name, salary * 12 AS annual_salary
FROM HR.EMPLOYEES;
/* 2. Calcule el salario anual de cada empleado con un bono de $100 anual */
SELECT last_name, (salary * 12) + 100 AS annual_salary_with_bonus
FROM HR.EMPLOYEES;
/* 3. Calcule el salario anual de cada empleado con un bono de $100 mensual */
SELECT last_name, (salary + 100) * 12 AS annual_salary_with_monthly_bonus
FROM HR.EMPLOYEES;
/* 4. Calcule las comisiones de todos los empleados. Esta se calcula como un porcentaje del
salario anual */
SELECT last_name, (salary * 12 * commission_pct) AS annual_commission
FROM HR.EMPLOYEES;
/* Expresiones aritméticas en WHERE y ORDER BY */
/* 1. Calcule el salario anual de cada empleado */
SELECT 
    last_name AS "Apellido",
    salary AS "Salario Mensual",
    salary * 12 AS "Salario Anual"
FROM HR.EMPLOYEES;
/* 2. Calcule el salario anual de cada empleado con un bono de $100 anual */
SELECT 
    last_name AS "Apellido",
    salary AS "Salario Mensual",
    (salary * 12) + 100 AS "Salario Anual con Bono"
FROM HR.EMPLOYEES;
/* 3. Calcule el salario anual de cada empleado con un bono de $100 mensual */
SELECT 
    last_name AS "Apellido",
    salary AS "Salario Mensual",
    (salary + 100) * 12 AS "Salario Anual con Bono Mensual"
FROM HR.EMPLOYEES;
/* 4. Calcule las comisiones de todos los empleados. Esta se calcula como un porcentaje del
salario anual */
SELECT 
    last_name AS "Apellido",
    salary AS "Salario Mensual",
    salary * 12 AS "Salario Anual",
    commission_pct AS "Porcentaje Comisión",
    salary * 12 * commission_pct AS "Comisión Anual"
FROM HR.EMPLOYEES;
/* 5. Muestre empleados, salarios mensuales y anuales para salarios anuales inferiores a
$100000 */
SELECT 
    last_name AS "Apellido",
    salary AS "Salario Mensual",
    salary * 12 AS "Salario Anual"
FROM HR.EMPLOYEES
WHERE salary * 12 < 100000;
/* 6. Muestre empleados, salarios mensuales y anuales, y la comisión anual ordenados por
mayor comisión anual */
SELECT 
    last_name AS "Apellido",
    salary AS "Salario Mensual",
    salary * 12 AS "Salario Anual",
    salary * 12 * commission_pct AS "Comisión Anual"
FROM HR.EMPLOYEES
ORDER BY "Comisión Anual" DESC NULLS LAST;
/* Concatenación de los valores de la consulta */
/* 1. Liste los nombres y apellidos de todos los empleados como uno sola columna formada
de una sola cadena de resultado. Renombre la nueva columna adecuadamente */
SELECT first_name || ' ' || last_name AS "Nombre Completo"
FROM HR.EMPLOYEES;
/* 2. Reconstruya los emails de los empleados, sabiendo que pertenecen al dominio
company.com */
SELECT first_name || '.' || last_name || '@company.com' AS "Email"
FROM HR.EMPLOYEES;
/* 3. Genere datos para los recibos de pago del salario mensual con el siguiente formato:
El/La Sr./Sra. Apellido, Nombre ha recibido $salario en el corriente mes */
SELECT 'El/La Sr./Sra. ' || last_name || ', ' || first_name ||
       ' ha recibido $' || salary || ' en el corriente mes.' AS "Recibo"
FROM HR.EMPLOYEES;
/* Datos nulos */
/* 1. Liste las personas que no tienen comisión asignada */
SELECT last_name
FROM HR.EMPLOYEES
WHERE commission_pct IS NULL;
/* 2. Lista de las personas que no tienen un superior */
SELECT last_name
FROM HR.EMPLOYEES
WHERE manager_id IS NULL;
/* 3. Personas que no están asignadas a ningún departamento */
SELECT last_name
FROM HR.EMPLOYEES
WHERE department_id IS NULL;
/* Operador de Negación */
/* 1. Muestre empleados, salarios mensuales y anuales, y la comisión anual ordenados por
mayor comisión anual. Solo incluya aquellos que tienen comisión */
SELECT last_name, salary, salary * 12 AS annual_salary,
       salary * 12 * commission_pct AS annual_commission
FROM HR.EMPLOYEES
WHERE commission_pct IS NOT NULL
ORDER BY annual_commission DESC;
/* 2. Muestre empleados, salarios mensuales y anuales para salarios anuales que no sean
menores a $100000 */
SELECT last_name, salary, salary * 12 AS annual_salary
FROM HR.EMPLOYEES
WHERE NOT (salary * 12 < 100000);
/* Patrones de búsqueda */
/* 1. Muestre todos los empleados con apellidos que tengan como tercera letra una ‘a’ */
SELECT last_name
FROM HR.EMPLOYEES
WHERE last_name LIKE '__a%';
/* 2. Muestre los apellidos que contengan tanto una letra ‘a’ como una ‘e’, en cualquier orden */
SELECT last_name
FROM HR.EMPLOYEES
WHERE last_name LIKE '%a%' AND last_name LIKE '%e%';
/* 3. Liste los empleados con apellidos con inicial “H” */
SELECT last_name
FROM HR.EMPLOYEES
WHERE last_name LIKE 'H%';
/* 4. Liste los empleados con nombres hasta la letra “M” */
SELECT first_name
FROM HR.EMPLOYEES
WHERE first_name <= 'M';
/* ---------------------------------------------------------------------------- */
/* Más práctica: */
/* 1. Muestre apellido, puesto y salario de gente de Ventas (SA_) o de Encargados de
Inventario (ST_CLERK) siempre y cuando sus salarios no sean $2500, $3500 o $7000 */
SELECT last_name, job_id, salary
FROM HR.EMPLOYEES
WHERE (job_id LIKE 'SA__%' OR job_id = 'ST_CLERK')
  AND salary NOT IN (2500, 3500, 7000);
/* 2. Muestre los apellidos ordenados y número de departamento de todos los empleados de
los deptos. 20 y 50 */
SELECT last_name, department_id
FROM HR.EMPLOYEES
WHERE department_id IN (20, 50)
ORDER BY last_name;
/* 3. Muestre los apellidos y número de departamento ordenados de todos los empleados de
los deptos. 20 y 50 */
SELECT last_name, department_id
FROM HR.EMPLOYEES
WHERE department_id IN (20, 50)
ORDER BY department_id;
/* 4. Muestre todos los empleados junto con su salario siempre y cuando no ganen entre
$5000 y $12000, ordenados por mayor salario */
SELECT last_name, salary
FROM HR.EMPLOYEES
WHERE salary NOT BETWEEN 5000 AND 12000
ORDER BY salary DESC;
/* 5. El departamento de recursos humanos desea que cree una consulta para visualizar
códigos de puesto únicos de la tabla de empleados */
SELECT DISTINCT job_id
FROM HR.EMPLOYEES;