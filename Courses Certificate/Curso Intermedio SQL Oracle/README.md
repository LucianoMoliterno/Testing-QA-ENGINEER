# 🗄️ Curso SQL Intermedio - Oracle Database

Este repositorio contiene los ejercicios, scripts y apuntes del curso de **SQL Intermedio**, enfocado en el motor **Oracle Database**. A lo largo del curso se profundiza en la manipulación avanzada de datos, consultas complejas y control de transacciones utilizando el esquema de ejemplo `HR`.

## 🛠️ Tecnologías
* **Motor:** Oracle Database
* **Esquema:** HR (Human Resources)
* **Herramientas:** SQL Developer / SQL Plus

---

## 📚 Temario y Contenidos

### 1. Consultas Simples y Funciones 
Repaso y profundización en la selección y transformación de datos.
* **Expresiones Aritméticas:** Uso en `SELECT`, `WHERE` y `ORDER BY`
* **Manejo de Nulos:** Operadores `IS NULL` y `IS NOT NULL`
* **Patrones de Búsqueda:** Uso de `LIKE`, `%` y `_`
* **Funciones de Cadena:** `CONCAT`, `SUBSTR`, `LENGTH`, `INSTR`, `UPPER`, `LOWER` 
* **Funciones de Fecha:** Aritmética de fechas, `MONTHS_BETWEEN`, `ADD_MONTHS`, `NEXT_DAY`, `TRUNC` 

### 2. Agrupación de Datos 
Técnicas para generar reportes y resúmenes estadísticos.
* **Funciones de Grupo:** `COUNT`, `SUM`, `AVG`, `MAX`, `MIN` 
* **Cláusulas:** `GROUP BY` para segmentar y `HAVING` para filtrar grupos

### 3. Consultas Multitablas (JOINS) 
Estrategias para combinar datos de múltiples fuentes.
* **Inner Joins:** Sintaxis estándar SQL:1999 (`NATURAL JOIN`, `USING`, `ON`)
* **Outer Joins:** `LEFT JOIN`, `RIGHT JOIN` y `FULL OUTER JOIN` para incluir registros sin correspondencia 
* **Self Joins:** Unir una tabla consigo misma (ej. Empleado y Jefe)
* **Cross Joins:** Productos cartesianos

### 4. Subconsultas 
Uso de consultas anidadas para resolver lógica compleja.
* **Single-row vs Multi-row:** Uso de operadores `=`, `>`, `<` vs `IN`, `ANY`, `ALL`
* **Subconsultas Correlacionadas:** Consultas internas que dependen de la fila actual de la consulta externa
* **Cláusula EXISTS:** Validación eficiente de existencia de relaciones
* **Subconsultas Multicolumna:** Comparación de pares de valores

### 5. Tablas Derivadas y CTEs 
Estructuras avanzadas para modularizar queries.
* **Tablas Derivadas:** Subconsultas en la cláusula `FROM`
* **CTEs (Common Table Expressions):** Uso de la cláusula `WITH` para definir subconsultas reutilizables y mejorar la legibilidad

### 6. Operaciones de Conjuntos (SET Operators) 
Combinación de resultados basada en teoría de conjuntos.
* `UNION` y `UNION ALL`: Unir resultados (con o sin duplicados)
* `INTERSECT`: Filas comunes entre dos consultas
* `MINUS`: Filas presentes en la primera consulta pero no en la segunda (exclusivo de Oracle)

### 7. Control de Transacciones (TCL) 
Manejo de la integridad de los datos.
* **Commit:** Confirmar cambios en la base de datos
* **Rollback:** Revertir cambios no confirmados
* **Savepoint:** Puntos de guardado intermedios dentro de una transacción

---

## 📝 Snippets Clave

### Ejemplo de CTE (Common Table Expression)
```sql
WITH promedio_por_depto AS (
    SELECT department_id, AVG(salary) as salario_avg
    FROM hr.employees
    GROUP BY department_id
)
SELECT e.last_name, e.salary
FROM hr.employees e
JOIN promedio_por_depto p ON e.department_id = p.department_id
WHERE e.salary > p.salario_avg;
```

### Ejemplo de Subconsulta Correlacionada (EXISTS)
```sql
SELECT department_name
FROM hr.departments d
WHERE EXISTS (
    SELECT 1 FROM hr.employees e
    WHERE e.department_id = d.department_id
);
```

### Ejemplo de Operaciones de Conjunto (MINUS)
```sql
-- Empleados que NO son managers
SELECT employee_id FROM hr.employees
MINUS
SELECT manager_id FROM hr.employees;
```

## 🚀 Cómo ejecutar
  - Asegúrate de tener acceso a una instancia de Oracle Database.
  - Desbloquea el usuario HR si estás usando una instalación por defecto.
  - Ejecuta los scripts .sql en tu IDE de preferencia (SQL Developer, DBeaver, VS Code).

Este repositorio fue creado como parte de la cursada de SQL Intermedio.
