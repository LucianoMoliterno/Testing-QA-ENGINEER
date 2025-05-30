-- Consultar toda la información de las cuentas de clientes 
-- (Nombre Cliente, Numero Cuenta, Tipo Cuenta, Fecha Transaccion, Tipo Transaccion, Monto Transaccion)
SELECT 	cliente.nombre "Nombre Cliente",
		cuenta.id "Numero Cuenta",
        cuenta.tipo "Tipo Cuenta",
        transaccion.fecha "Fecha Transaccion",
        transaccion.tipo "Tipo Transaccion",
        transaccion.monto "Monto Transaccion"
FROM transaccion,
	 cuenta,
     cliente
WHERE cliente.id = cuenta.id_cliente
AND cuenta.id = transaccion.id_cuenta;

-- Consultar toda la información de las cuentas de clientes 
-- (Nombre Cliente, Numero Cuenta, Tipo Cuenta, Fecha Transaccion, Tipo Transaccion, Monto Transaccion)
SELECT 	cl.nombre "Nombre Cliente",
		c.id "Numero Cuenta",
        c.tipo "Tipo Cuenta",
        t.fecha "Fecha Transaccion",
        t.tipo "Tipo Transaccion",
        t.monto "Monto Transaccion"
FROM transaccion t,
	 cuenta c,
     cliente cl
WHERE cl.id = c.id_cliente
AND c.id = t.id_cuenta;

-- Consultar toda la información de las cuentas de clientes 
-- (Nombre Cliente, Numero Cuenta, Tipo Cuenta, Fecha Transaccion, Tipo Transaccion, Monto Transaccion)
SELECT 	nombre "Nombre Cliente",
		c.id "Numero Cuenta",
        c.tipo "Tipo Cuenta",
        t.fecha "Fecha Transaccion",
        t.tipo "Tipo Transaccion",
        t.monto "Monto Transaccion"
FROM transaccion t,
	 cuenta c,
     cliente cl
WHERE cl.id = c.id_cliente
AND c.id = t.id_cuenta;

-- Cuantas cuentas tiene cada cliente
SELECT cliente.id, cliente.nombre, COUNT(1) "Numero de Cuentas"
FROM cuenta, 
	 cliente
WHERE cuenta.id_cliente = cliente.id
GROUP BY cliente.id, cliente.nombre;

-- Listar clientes que tengan más de una cuenta
SELECT cliente.id, cliente.nombre, COUNT(1) "Numero de Cuentas"
FROM cuenta, 
	 cliente
WHERE cuenta.id_cliente = cliente.id
GROUP BY cliente.id, cliente.nombre
HAVING COUNT(1) > 1;

