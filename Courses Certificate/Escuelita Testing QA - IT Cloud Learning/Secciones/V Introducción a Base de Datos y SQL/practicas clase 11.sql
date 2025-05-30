-- Mostrar datos en mayúscula o minúscula
SELECT nombre "Nombre Original",
	   UPPER(nombre) "Nombre Mayúscula",
       LOWER(nombre) "Nombre Minúsucula"
FROM cliente;

-- Concatenar dos o más columnas de la base de datos
SELECT CONCAT(direccion, ', ', ciudad) "Dirección Completa"
FROM cliente;

-- Redondear números decimales
SELECT ROUND(monto, 2)
FROM transaccion;

-- Quiero saber el monto total que tienen los clientes en el banco
SELECT SUM(saldo) "Suma de Saldos",
	   MIN(saldo) "Saldo Mínimo",
       MAX(saldo) "Saldo Máximo",
       AVG(saldo) "Saldo Promedio"
FROM cuenta;

-- Quiero saber el monto total que tienen los clientes en el banco
SELECT SUM(saldo) "Suma de Saldos",
	   MIN(saldo) "Saldo Mínimo",
       MAX(saldo) "Saldo Máximo",
       AVG(saldo) "Saldo Promedio",
       COUNT(id) "Número de Cuentas (Id)",
       COUNT(*) "Número de Cuentas (Genérica)",
       COUNT(1) "Número de Cuentas (alternativo)"
FROM cuenta;

-- Obtener la sumatoria, mínimo, máximo, promedio y núemro de registros según el tipo de cuenta
SELECT tipo, SUM(saldo), MIN(saldo), MAX(saldo), AVG(saldo), COUNT(1)
FROM cuenta
GROUP BY tipo;

SELECT tipo, SUM(monto)
FROM transaccion
GROUP BY tipo;

SELECT fecha, tipo, SUM(monto)
FROM transaccion
GROUP BY fecha, tipo;

-- Obtener datos calculados por tipo de cuenta cuando el tipo tenga más de dos cuentas
SELECT tipo, SUM(saldo), MIN(saldo), MAX(saldo), AVG(saldo), COUNT(1)
FROM cuenta
WHERE saldo > 5000
GROUP BY tipo
HAVING COUNT(1) > 2;

-- Obtener datos calculados por tipo de cuenta cuando el tipo tenga más de dos cuentas
SELECT tipo, SUM(saldo), MIN(saldo), MAX(saldo), AVG(saldo), COUNT(1)
FROM cuenta
WHERE saldo > 5000
GROUP BY tipo
HAVING COUNT(1) > 1
ORDER BY tipo DESC;

-- Obtener datos calculados por tipo de cuenta cuando el tipo tenga más de dos cuentas
SELECT tipo, SUM(saldo), MIN(saldo), MAX(saldo), AVG(saldo), COUNT(1)
FROM cuenta
WHERE saldo > 5000
GROUP BY tipo
HAVING COUNT(1) > 1
ORDER BY tipo DESC;


