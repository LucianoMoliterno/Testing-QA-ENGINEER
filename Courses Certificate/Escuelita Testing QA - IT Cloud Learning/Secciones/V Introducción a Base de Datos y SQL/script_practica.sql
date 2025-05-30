-- Creación de la tabla Cliente
CREATE TABLE cliente (
    id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    direccion TEXT NOT NULL,
    ciudad TEXT NOT NULL,
    pais TEXT NOT NULL,
    codigo_postal TEXT NOT NULL
);

-- Creación de la tabla Cuenta
CREATE TABLE cuenta (
    id INTEGER PRIMARY KEY,
    id_cliente INTEGER NOT NULL,
    tipo TEXT NOT NULL CHECK (tipo IN ('Ahorro', 'Corriente')),
    saldo REAL NOT NULL DEFAULT 0.0,
    moneda TEXT NOT NULL DEFAULT 'ARS',
    FOREIGN KEY (id_cliente) REFERENCES cliente(id)
);

-- Creación de la tabla Transaccion
CREATE TABLE transaccion (
    id INTEGER PRIMARY KEY,
    id_cuenta INTEGER NOT NULL,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    tipo TEXT NOT NULL CHECK (tipo IN ('Deposito', 'Extraccion', 'Transferencia')),
    monto REAL NOT NULL,
    descripcion TEXT,
    FOREIGN KEY (id_cuenta) REFERENCES cuenta(id)
);

-- Inserción de datos de ejemplo en la tabla Cliente
INSERT INTO cliente (id, nombre, email, direccion, ciudad, pais, codigo_postal) VALUES
(1, 'Ana Gómez', 'ana.gomez@example.com', 'Av. Siempre Viva 456', 'Córdoba', 'Argentina', '5000'),
(2, 'Luis Martínez', 'luis.martinez@example.com', 'Calle Libertad 789', 'Rosario', 'Argentina', '2000'),
(3, 'María López', 'maria.lopez@example.com', 'Diagonal Norte 1001', 'Buenos Aires', 'Argentina', 'C1001');

-- Inserción de datos de ejemplo en la tabla Cuenta
INSERT INTO cuenta (id, id_cliente, tipo, saldo, moneda) VALUES
(1, 1, 'Ahorro', 15000.00, 'ARS'),
(2, 1, 'Corriente', 8000.00, 'ARS'),
(3, 2, 'Ahorro', 22000.00, 'ARS'),
(4, 3, 'Corriente', 5600.00, 'ARS'),
(5, 3, 'Ahorro', 13400.00, 'ARS');

-- Inserción de datos de ejemplo en la tabla Transaccion
INSERT INTO transaccion (id, id_cuenta, tipo, monto, descripcion) VALUES
(1, 1, 'Deposito', 5000.00, 'Depósito inicial'),
(2, 1, 'Extraccion', 1000.00, 'Retiro en cajero'),
(3, 2, 'Transferencia', 2000.00, 'Transferencia a cuenta ahorro'),
(4, 3, 'Deposito', 10000.00, 'Pago de salario'),
(5, 3, 'Extraccion', 3000.00, 'Pago de alquiler'),
(6, 4, 'Deposito', 6000.00, 'Venta de auto'),
(7, 5, 'Transferencia', 4000.00, 'Transferencia desde cuenta corriente'),
(8, 5, 'Extraccion', 1000.00, 'Retiro por ventanilla');
