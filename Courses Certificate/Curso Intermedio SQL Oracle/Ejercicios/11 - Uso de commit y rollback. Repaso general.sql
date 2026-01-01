/* Oracle (HR): Ejercicios prácticos */
/* Ejercicio 1: Aumentar salario y revertir si hay error */
BEGIN
UPDATE employees SET salary = salary * 1.05 WHERE department_id = 90;
DELETE FROM employees WHERE employee_id = 999; -- no existe
COMMIT;
EXCEPTION
WHEN OTHERS THEN
ROLLBACK;
END;
-- ¿Qué ocurre si el empleado 999 no existe? ¿Se guarda el aumento de salario?
-- Sí, el aumento de salario se guarda. Porqué: La instrucción DELETE FROM employees WHERE employee_id = 999 no genera un error si el empleado 999 no existe. 
-- Simplemente, la consulta se ejecuta y no afecta a ninguna fila.
-- Como no se produce ningún error, el código dentro del bloque EXCEPTION (que contiene el ROLLBACK ) nunca se ejecuta.
-- La transacción continúa y llega al COMMIT, guardando permanentemente el UPDATE del salario.
/* Ejercicio 2: Uso de SAVEPOINT */
BEGIN
UPDATE employees SET salary = salary + 500 WHERE employee_id = 103;
SAVEPOINT antes_de_borrar;
DELETE FROM employees WHERE employee_id = 104;
ROLLBACK TO antes_de_borrar;
COMMIT;
END;
-- ¿Qué cambios se guardan y cuáles se revierten?
-- Se guarda el aumento de salario (UPDATE) y se revierte la eliminación (DELETE).
-- Porqué:
-- Se ejecuta el UPDATE del salario para el empleado 103.
-- Se establece un "punto de guardado" llamado antes_de_borrar.
-- Se elimina al empleado 104.
-- El comando ROLLBACK TO antes_de_borrar  deshace todos los cambios realizados después del punto de guardado. En este caso, revierte la eliminación del empleado 104.
-- El UPDATE del salario (que ocurrió antes del SAVEPOINT) no se ve afectado por el ROLLBACK TO.
-- El COMMIT  final guarda permanentemente todos los cambios que quedan pendientes (solo el UPDATE).
---------------------------------------------------------------------------
/* SQL Server (NorthWind): Ejercicios prácticos */
/* Ejercicio 1: Actualizar stock y confirmar */
BEGIN TRANSACTION;
UPDATE Products SET UnitsInStock = UnitsInStock - 5 WHERE ProductID = 1;
COMMIT TRANSACTION;
-- ¿Qué pasa si no se ejecuta el COMMIT?
-- Los cambios no se guardan permanentemente y la fila afectada queda bloqueada.
-- Porqué:
-- BEGIN TRANSACTION  inicia la transacción.
-- El UPDATE  modifica los datos, pero estos cambios solo son visibles para tu sesión actual.
-- Si nunca se ejecuta COMMIT TRANSACTION  (ni ROLLBACK TRANSACTION), la transacción permanece "abierta".
-- Esto causa que la fila (ProductID = 1) quede bloqueada, impidiendo que otras sesiones la modifiquen.
-- Si cierras la conexión (por ejemplo, cierras la ventana de consulta), la base de datos automáticamente revertirá la transacción (ROLLBACK) y los cambios se perderán.
/* Ejercicio 2: Manejo de errores */
BEGIN TRANSACTION;
BEGIN TRY
UPDATE Products SET UnitPrice = UnitPrice * 1.2 WHERE CategoryID = 3;
DELETE FROM Products WHERE ProductID = 999; -- no existe
COMMIT TRANSACTION;
END TRY
BEGIN CATCH
ROLLBACK TRANSACTION;
PRINT 'Error detectado';
END CATCH;
-- ¿Se guarda el aumento de precios si el DELETE falla?
-- Sí, el aumento de precios se guarda.
-- Porqué: El escenario es idéntico al del Ejercicio 1 de Oracle. El comando DELETE FROM Products WHERE ProductID = 999  no "falla" aunque el producto no exista. Simplemente no elimina filas.
-- Dado que no se genera un error real, el bloque BEGIN TRY  se completa con éxito.
-- El script llega al COMMIT TRANSACTION  y lo ejecuta.
-- El bloque BEGIN CATCH , que contiene el ROLLBACK, nunca es invocado.
-- Por lo tanto, tanto el UPDATE de precios como el DELETE (que no hizo nada) se confirman.