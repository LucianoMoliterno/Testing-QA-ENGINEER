-- 1. Listar los productos cuyo precio sea mayor a 350USD
SELECT id, nombre, precio
FROM producto
WHERE precio > 350;

-- 2. Listar los productos que contengan la palabra 'Mac'
SELECT id, nombre, descripcion
FROM producto
WHERE nombre LIKE '%Mac%' OR descripcion LIKE '%Mac%';

-- 3. Listar los pedidos que ha hecho el usuario cuyo correo electrónico es <juan@example.com>
-- Nota: No hay pedidos para luan@example.com en los datos de ejemplo, por eso le coloque la j.
SELECT id, fecha, total
FROM pedido
WHERE email = 'juan@example.com';

-- 4. Listar los productos que se compraron en el pedido 1 indicando nombre y precio del producto
SELECT p.nombre, dp.precio_unitario
FROM detalle_pedido dp
JOIN producto p ON dp.id_producto = p.id
WHERE dp.id_pedido = 1;

-- 5. Mostrar el monto total del pedido 1 únicamente utilizando la tabla detalle_pedido
SELECT SUM(cantidad * precio_unitario) AS total_pedido
FROM detalle_pedido
WHERE id_pedido = 1;

-- 6. Mostrar cuántos productos hay registrados
SELECT COUNT(*) AS total_productos
FROM producto;