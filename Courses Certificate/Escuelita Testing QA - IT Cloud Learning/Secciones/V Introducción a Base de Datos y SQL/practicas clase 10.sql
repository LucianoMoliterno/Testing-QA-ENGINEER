-- Listar el nombre y correo de los clientes registrados 
SELECT nombre, email
FROM cliente;

-- Listar el nombre y correo de los clientes registrados de Argentina
SELECT nombre, email
FROM cliente
WHERE pais = 'Argentina';

-- Listar el nombre y correo de los clientes registrados de Argentina incluyendo un literal
SELECT nombre, email, 'Cliente Activo'
FROM cliente
WHERE pais = 'Argentina';

-- Listar las cuentas con su saldo en ARS y el equivalente en USD
SELECT 	id id_cuenta, 
		tipo tipo_cuenta,
        saldo 'Saldo en ARS',
        saldo / 1000 'Saldo en USD'
FROM cuenta;
-- Operadores aritméticos: + - * /

-- Listar las cuentas con su saldo en ARS y el equivalente en USD 
-- cuando el saldo en USD sea menor a 20 USD
SELECT 	id id_cuenta, 
		tipo tipo_cuenta,
        saldo 'Saldo en ARS',
        saldo / 1000 'Saldo en USD'
FROM cuenta
WHERE saldo / 1000 < 20;

-- Listar los clientes que no tengan correo registrado (valor nulo)
SELECT *
FROM cliente
WHERE email IS NULL;

-- Listar los clientes que SI tengan correo registrado 
SELECT *
FROM cliente
WHERE email IS NOT NULL;

-- Listar las cuentas con saldo menor a 10000 ARS
SELECT *
FROM cuenta
WHERE saldo < 10000;

-- Listar las cuentas cuyo saldo esté entre 10000 y 20000 ARS
SELECT *
FROM cuenta 
WHERE saldo BETWEEN 10000 AND 20000;

-- Listar las cuentas cuyo saldo sea 5600, 8000 o 13400
SELECT *
FROM cuenta
WHERE saldo IN (5600, 8000, 13400);

-- Listar las cuentas tipo Ahorro o Corriente
SELECT *
FROM cuenta
WHERE tipo IN ('Ahorro', 'Corriente');

-- Listar los clientes cuyo nombre comience con una 'A'
SELECT *
FROM cliente 
WHERE nombre LIKE 'A%';

-- Listar los clientes cuyo nombre terminen con una 'Z'
SELECT *
FROM cliente 
WHERE nombre LIKE '%Z';

-- Listar los clientes cuyo nombre tenga en la segunda letra una 'N'
SELECT *
FROM cliente 
WHERE nombre LIKE '_N%';

-- Listar los dos primeros registros de la tabla cliente
SELECT *
FROM cliente
LIMIT 2;

-- Listar las transacciones de la cuenta 5 ordenadas por monto en forma ascendente
SELECT *
FROM transaccion
WHERE id_cuenta = 5
ORDER BY monto;

-- Listar las transacciones de la cuenta 5 ordenadas por monto en forma descendente
SELECT *
FROM transaccion
WHERE id_cuenta = 5
ORDER BY monto DESC;

-- Listar las transacciones de la cuenta 5 ordenadas por monto en forma ascendente
SELECT *
FROM transaccion
WHERE id_cuenta = 5
ORDER BY monto ASC;

-- Listar las transacciones ordenando por la segunda columna
SELECT *
FROM transaccion
ORDER BY 2;

-- Listar las transacciones de tipo Deposito cuyo monto sea menor a 10000 ARS
SELECT *
FROM transaccion
WHERE tipo = 'Deposito'
AND monto < 10000;

