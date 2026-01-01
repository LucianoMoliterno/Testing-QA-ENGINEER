/* Funciones Estadisticas */
/* 1. Cuente cuántos empleados hay */
SELECT COUNT(*) 
FROM HR.EMPLOYEES;
/* 2. Cuente cuántos nombres hay */
SELECT COUNT(FIRST_NAME) 
FROM HR.EMPLOYEES;
/* 3. Cuente cuántos nombres distintos hay */
SELECT COUNT(DISTINCT FIRST_NAME) 
FROM HR.EMPLOYEES;
/* 4. Cuente cuántos apellidos hay */
SELECT COUNT(LAST_NAME) 
FROM HR.EMPLOYEES;
/* 5. Cuente cuántos apellidos distintos hay */
SELECT COUNT(DISTINCT LAST_NAME) 
FROM HR.EMPLOYEES;
/* 6. Cuente cuántos empleados reciben comisión */
SELECT COUNT(COMMISSION_PCT) 
FROM HR.EMPLOYEES;
/* 7. Cuente cuántos empleados NO reciben comisión */
SELECT COUNT(*) 
FROM HR.EMPLOYEES 
WHERE COMMISSION_PCT IS NULL;
/* 8. Sume el total que se paga de comisiones anuales */
SELECT SUM(SALARY * COMMISSION_PCT * 12) 
FROM HR.EMPLOYEES;
/* 9. Calcule la proporción de comisiones anuales sobre los salarios anuales */
SELECT SUM(SALARY * COMMISSION_PCT) / SUM(SALARY) 
FROM HR.EMPLOYEES;
/* 10. Calcule la proporción de comisiones anuales sobre los salarios anuales de los empleados que tienen comisión */
SELECT SUM(SALARY * COMMISSION_PCT) / SUM(SALARY) 
FROM HR.EMPLOYEES 
WHERE COMMISSION_PCT IS NOT NULL;
/* 11. Calcule el promedio de comisiones anuales sobre los salarios anuales, mediante SUM y COUNT, y luego mediante AVG */
/* ---SUM y COUNT--- */
SELECT SUM(NVL(COMMISSION_PCT, 0)) / COUNT(*) 
FROM HR.EMPLOYEES;
/* ---AVG--- */
SELECT AVG(NVL(COMMISSION_PCT, 0)) 
FROM HR.EMPLOYEES;
/* 12. Calcule el promedio de comisiones anuales sobre los salarios anuales, mediante SUM y COUNT, y luego mediante AVG de los empleados que tienen comisión */
/* ---SUM y COUNT--- */
SELECT SUM(COMMISSION_PCT) / COUNT(COMMISSION_PCT) 
FROM HR.EMPLOYEES;
/* ---AVG--- */
SELECT AVG(COMMISSION_PCT) 
FROM HR.EMPLOYEES;
/* 13. Muestre fecha más antigua y más reciente de contratación */
SELECT MIN(HIRE_DATE), MAX(HIRE_DATE) 
FROM HR.EMPLOYEES;
/* 14. Muestre el promedio, el máximo, el mínimo y la suma total de salarios de todos los representantes de departamento (JOB_ID con ‘%REP%’ */
SELECT AVG(SALARY), MAX(SALARY), MIN(SALARY), SUM(SALARY) 
FROM HR.EMPLOYEES 
WHERE JOB_ID LIKE '%REP%';
/* 15. Muestre el primero y el último apellido por orden alfabético */
SELECT MIN(LAST_NAME), MAX(LAST_NAME) 
FROM HR.EMPLOYEES;
/* 16. Cuántos empleados hay en el departamento 50 */
SELECT COUNT(*) 
FROM HR.EMPLOYEES 
WHERE DEPARTMENT_ID = 50;
/* 17. Cuántos empleados hay en el departamento 80 */
SELECT COUNT(*) 
FROM HR.EMPLOYEES 
WHERE DEPARTMENT_ID = 80;
/*-------------------------------------------------------------------------------------*/
/* Agrupando datos /*
/* 1. Cuál es la diferencia de salarios máximo y mínimo */
SELECT MAX(SALARY) - MIN(SALARY) 
FROM HR.EMPLOYEES;
/* 2. Muestre los promedios de salarios crecientes de los empleados de cada departamento*/
SELECT DEPARTMENT_ID, AVG(SALARY) 
FROM HR.EMPLOYEES 
GROUP BY DEPARTMENT_ID 
ORDER BY AVG(SALARY) ASC;
/*  3. Cuál es el promedio de salarios mínimos y máximos */
SELECT (MAX(SALARY) + MIN(SALARY)) / 2 
FROM HR.EMPLOYEES;
/*  4. Cuál es el máximo y el mínimo salario promedio por departamento */
SELECT MAX(AVG(SALARY)), MIN(AVG(SALARY)) 
FROM HR.EMPLOYEES 
GROUP BY DEPARTMENT_ID;
/*  5. Desarrolle una consulta que muestre el código del departamento con título Código del departamento, que cuente los empleados agrupados por departamentos, ordenados por código de departamento */
SELECT DEPARTMENT_ID AS "Código del departamento", COUNT(*) 
FROM HR.EMPLOYEES 
GROUP BY DEPARTMENT_ID 
ORDER BY DEPARTMENT_ID;
/*  6. Determine el número de supervisores sin listarlos */
SELECT COUNT(DISTINCT MANAGER_ID) 
FROM HR.EMPLOYEES;
/*  7. Cuántos subordinados tiene cada jefe */
SELECT MANAGER_ID, COUNT(*) 
FROM HR.EMPLOYEES 
WHERE MANAGER_ID IS NOT NULL 
GROUP BY MANAGER_ID;
/*  8. Cuántos empleados tiene cada jefe por departamento */
SELECT MANAGER_ID, DEPARTMENT_ID, COUNT(*) 
FROM HR.EMPLOYEES 
WHERE MANAGER_ID IS NOT NULL 
GROUP BY MANAGER_ID, DEPARTMENT_ID 
ORDER BY MANAGER_ID, DEPARTMENT_ID;
/*  9. Muestre el monto de salarios pagados por cargo (JOB_ID) por departamento(ordenados) */
SELECT DEPARTMENT_ID, JOB_ID, SUM(SALARY) 
FROM HR.EMPLOYEES 
GROUP BY DEPARTMENT_ID, JOB_ID 
ORDER BY DEPARTMENT_ID, JOB_ID;
/*  10. Realice una consulta que muestre el número de países por región, la consulta debe mostrar solo el código de la región, así como el número de países de cada región, ordenando el resultado por la región que tenga mayor número de países */
SELECT REGION_ID, COUNT(*) AS NUMERO_PAISES
FROM HR.COUNTRIES
GROUP BY REGION_ID
ORDER BY NUMERO_PAISES DESC;
/*  11. Desarrolle una consulta que liste los códigos de puestos con el número de empleados que pertenecen a cada puesto, ordenados por número de empleados: los puestos que tienen más empleados aparecen primero */
SELECT JOB_ID, COUNT(*) AS NUMERO_EMPLEADOS
FROM HR.EMPLOYEES
GROUP BY JOB_ID
ORDER BY NUMERO_EMPLEADOS DESC;
/*  12. Realice una consulta que muestre el número de departamentos por ubicación (LOCATION_ID) */
SELECT LOCATION_ID, COUNT(*) 
FROM HR.DEPARTMENTS
GROUP BY LOCATION_ID;
/*-------------------------------------------------------------------------------------*/
/* Restricción de resultados en los grupos */
/* 1. Cree un informe para mostrar el número de supervisor y el salario más bajo del empleado bajo ese supervisor. Excluya a los empleados cuyo supervisor no se conozca. Excluya los grupos en los que el salario mínimo sea 6000 dólares o menos. Clasifique la salida en orden descendente de salario */
SELECT MANAGER_ID, MIN(SALARY)
FROM HR.EMPLOYEES
WHERE MANAGER_ID IS NOT NULL
GROUP BY MANAGER_ID
HAVING MIN(SALARY) > 6000
ORDER BY MIN(SALARY) DESC;
/* 2. Realicé una consulta que muestre solo los nombres de los empleados que se repiten. (Pista: Having count(*)) */
SELECT FIRST_NAME
FROM HR.EMPLOYEES
GROUP BY FIRST_NAME
HAVING COUNT(*) > 1;
/* 3. Realicé una consulta que muestre solo los nombres de los empleados que no se repiten */
SELECT FIRST_NAME
FROM HR.EMPLOYEES
GROUP BY FIRST_NAME
HAVING COUNT(*) = 1;
/* 4. Realice una consulta que liste el número de empleados por departamento, que ganan como mínimo 5000 en concepto de salario. Omita los departamentos que tengan menos de 4 empleados con ese salario */
SELECT DEPARTMENT_ID, COUNT(*)
FROM HR.EMPLOYEES
WHERE SALARY >= 5000
GROUP BY DEPARTMENT_ID
HAVING COUNT(*) >= 4;
/* 5. Cantidad de empleados por departamento con más de 10 empleados */
SELECT DEPARTMENT_ID, COUNT(*)
FROM HR.EMPLOYEES
GROUP BY DEPARTMENT_ID
HAVING COUNT(*) > 10;
/* 6. Muestre departamentos con salario promedio mayor a 9000 */
SELECT DEPARTMENT_ID, AVG(SALARY)
FROM HR.EMPLOYEES
GROUP BY DEPARTMENT_ID
HAVING AVG(SALARY) > 9000;