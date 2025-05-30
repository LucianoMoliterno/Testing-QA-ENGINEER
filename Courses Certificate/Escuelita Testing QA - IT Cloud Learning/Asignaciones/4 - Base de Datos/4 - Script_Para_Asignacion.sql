-- Creación de la tabla Producto
CREATE TABLE producto (
    id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    descripcion TEXT,
    precio REAL NOT NULL,
    stock INTEGER NOT NULL
);

-- Creación de la tabla Pedido
CREATE TABLE pedido (
    id INTEGER PRIMARY KEY,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    total REAL NOT NULL,
    nombre_cliente TEXT NOT NULL,
    email TEXT NOT NULL,
    direccion TEXT NOT NULL,
    ciudad TEXT NOT NULL,
    pais TEXT NOT NULL,
    codigo_postal TEXT NOT NULL,
    tarjeta_credito TEXT NOT NULL
);

-- Creación de la tabla Detalle_Pedido
CREATE TABLE detalle_pedido (
    id_pedido INTEGER,
    id_producto INTEGER,
    cantidad INTEGER NOT NULL,
    precio_unitario REAL NOT NULL,
    PRIMARY KEY (id_pedido, id_producto),
    FOREIGN KEY (id_pedido) REFERENCES pedido(id),
    FOREIGN KEY (id_producto) REFERENCES producto(id)
);

-- Inserción de datos de ejemplo en la tabla Producto (con valores para 'id')
INSERT INTO producto (id, nombre, descripcion, precio, stock) VALUES
(1, 'Samsung Galaxy S6', 'Smartphone con pantalla Quad HD de 5.1", cámara de 16MP y procesador Exynos', 360.00, 15),
(2, 'Sony Xperia Z5', 'Teléfono resistente al agua con cámara de 23MP y lector de huellas', 320.00, 10),
(3, 'MacBook Pro 13"', 'Laptop con pantalla Retina, procesador M2 y 512GB SSD', 1500.00, 8);

-- Inserción de datos de ejemplo en la tabla Pedido (con valor para 'id')
INSERT INTO pedido (id, total, nombre_cliente, email, direccion, ciudad, pais, codigo_postal, tarjeta_credito)
VALUES (
    1, -- ID del pedido
    680.00,
    'Juan Pérez',
    'juan@example.com',
    'Calle Falsa 123',
    'Buenos Aires',
    'Argentina',
    'C1406',
    '4111-1111-1111-1111'
);

-- Inserción de datos de ejemplo en la tabla Detalle_Pedido
INSERT INTO detalle_pedido (id_pedido, id_producto, cantidad, precio_unitario)
VALUES
(1, 1, 1, 360.00), -- Pedido 1, Producto 1
(1, 2, 1, 320.00); -- Pedido 1, Producto 2
