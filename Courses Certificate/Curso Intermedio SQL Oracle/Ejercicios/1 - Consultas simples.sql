/*Consultas simples (SELECT *)*/
/* consulta de todas las columnas y filas de cada tabla de la base HR de Oracle Live SQL*/
SELECT * FROM HR.COUNTRIES;
SELECT * FROM HR.DEPARTMENTS;
SELECT * FROM HR.EMPLOYEES;
SELECT * FROM HR.JOBS;
SELECT * FROM HR.JOB_HISTORY;
SELECT * FROM HR.LOCATIONS;
SELECT * FROM HR.REGIONS;
/*-----------------------------------------------------------------------------------*/
/* 1.Liste los nombres y apellidos de todos los empleados junto con su email*/
SELECT FIRST_NAME, LAST_NAME, EMAIL FROM HR.EMPLOYEES;
/* 2.Liste los ID de departamento y su nombre*/
SELECT DEPARTMENT_ID, DEPARTMENT_NAME FROM HR.DEPARTMENTS;
/* 3.Liste los cargos (JOB_TITLE) y el salario máximo y mínimo*/
SELECT JOB_TITLE, MAX_SALARY, MIN_SALARY FROM HR.JOBS;
/* 4.Detalle las ciudades y su identificador (LOCATION_ID)*/
SELECT LOCATION_ID, CITY FROM HR.LOCATIONS;
/* 5.Liste los países*/
SELECT COUNTRY_NAME FROM HR.COUNTRIES;
/* 6.Liste las regiones*/
SELECT REGION_NAME FROM HR.REGIONS;
/*-----------------------------------------------------------------------------------*/
/*Condiciones con WHERE*/
/* 1. Liste los empleados del departamento 60*/
SELECT * FROM HR.EMPLOYEES WHERE DEPARTMENT_ID = 60;
/* 2. Liste empleados con salario entre 7000 y 12000*/
SELECT * FROM HR.EMPLOYEES WHERE SALARY BETWEEN 7000 AND 12000;
/* 3. Muestre empleados que trabajan en los departamentos 10, 20 o 30*/
SELECT * FROM HR.EMPLOYEES WHERE DEPARTMENT_ID IN (10, 20, 30);
/* 4. Muestre empleados con salario mayor a 10000 y del departamento 90*/
SELECT * FROM HR.EMPLOYEES WHERE SALARY > 10000 AND DEPARTMENT_ID = 90;
/* 5. Liste los empleados con apellidos con inicial “H”*/
SELECT * FROM HR.EMPLOYEES WHERE LAST_NAME LIKE 'H%';
/* 6. Liste los empleados con nombres hasta la letra “M”*/
SELECT * FROM HR.EMPLOYEES WHERE FIRST_NAME < 'N';
/* 7. Empleados con comisión menor a 0.50*/
SELECT * FROM HR.EMPLOYEES WHERE COMMISSION_PCT < 0.50;
/* 8. Cargos con más de $3000 de salario mínimo*/
SELECT * FROM HR.JOBS WHERE MIN_SALARY > 3000;
/* 9. Salarios de empleados por debajo de $6000*/
SELECT * FROM HR.EMPLOYEES WHERE SALARY < 6000;
/* 10. Identificador y región de Argentina*/
SELECT COUNTRY_ID, REGION_ID FROM HR.COUNTRIES WHERE COUNTRY_NAME = 'Argentina';
/*-----------------------------------------------------------------------------------*/
/*Ordenamiento (ORDER BY)*/
/* 1. Liste los nombres y apellidos de todos los empleados junto con su email, ordenado por el apellido en forma ascendente*/
SELECT FIRST_NAME, LAST_NAME, EMAIL FROM HR.EMPLOYEES ORDER BY LAST_NAME ASC;
/* 2. Liste los ID de departamento con sus nombres ordenados*/
SELECT DEPARTMENT_ID, DEPARTMENT_NAME FROM HR.DEPARTMENTS ORDER BY DEPARTMENT_ID;
/* 3. Salarios de empleados por debajo de $6000 en forma decreciente*/
SELECT EMPLOYEE_ID, SALARY FROM HR.EMPLOYEES WHERE SALARY < 6000 ORDER BY SALARY DESC;
/* 4. Muestre empleados que trabajan en los departamentos 10, 20 o 30 en ese orden*/
SELECT * FROM HR.EMPLOYEES WHERE DEPARTMENT_ID IN (10, 20, 30) ORDER BY DEPARTMENT_ID;
/* 5. Liste empleados con salario entre 7000 y 12000, de arriba a abajo*/
SELECT * FROM HR.EMPLOYEES WHERE SALARY BETWEEN 7000 AND 12000 ORDER BY SALARY DESC;
/* 6. Liste los países alfabéticamente*/
SELECT COUNTRY_NAME FROM HR.COUNTRIES ORDER BY COUNTRY_NAME ASC;
/* 7. Países ordenados por identificador*/
SELECT COUNTRY_ID, COUNTRY_NAME FROM HR.COUNTRIES ORDER BY COUNTRY_ID;
/*-----------------------------------------------------------------------------------*/
/*Eliminación de duplicados (DISTINCT)*/
/* 1. Salarios de empleados por debajo de $6000 en forma decreciente sin repetición*/
SELECT DISTINCT SALARY FROM HR.EMPLOYEES WHERE SALARY < 6000 ORDER BY SALARY DESC;
/* 2. Lista de apellidos sin repetición*/
SELECT DISTINCT LAST_NAME FROM HR.EMPLOYEES;
/* 3. Lista de identificador de cargos (JOB_ID) de los empleados, sin repetición*/
SELECT DISTINCT JOB_ID FROM HR.EMPLOYEES;