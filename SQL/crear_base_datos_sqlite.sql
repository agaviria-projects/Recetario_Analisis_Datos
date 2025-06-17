-- crear_base_datos_tienda.sql
-- Base de datos para practicar SQL: incluye tablas de ventas, clientes y productos

-- crear_base_datos_tienda.sql
CREATE DATABASE tienda;
USE tienda;

-- Crear tabla CLIENTES
CREATE TABLE clientes (
    id_cliente INTEGER PRIMARY KEY,
    nombre TEXT,
    ciudad TEXT
);

-- Crear tabla PRODUCTOS
CREATE TABLE productos (
    id_producto INTEGER PRIMARY KEY,
    nombre TEXT,
    categoria TEXT
);

-- Crear tabla VENTAS
CREATE TABLE ventas (
    id_venta INTEGER PRIMARY KEY,
    id_cliente INTEGER,
    id_producto INTEGER,
    cantidad INTEGER,
    precio_unitario REAL,
    fecha TEXT,
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente),
    FOREIGN KEY (id_producto) REFERENCES productos(id_producto)
);

-- Insertar datos en CLIENTES
INSERT INTO clientes (id_cliente, nombre, ciudad) VALUES
(1, 'Ana', 'Bogotá'),
(2, 'Luis', 'Medellín'),
(3, 'Carlos', 'Cali'),
(4, 'Marta', 'Barranquilla'),
(5, 'Julia', 'Cartagena');

-- Insertar datos en PRODUCTOS
INSERT INTO productos (id_producto, nombre, categoria) VALUES
(101, 'Mouse', 'Accesorio'),
(102, 'Teclado', 'Accesorio'),
(103, 'Monitor', 'Pantalla'),
(104, 'Webcam', 'Accesorio'),
(105, 'Impresora', 'Oficina');

-- Insertar datos en VENTAS
INSERT INTO ventas (id_venta, id_cliente, id_producto, cantidad, precio_unitario, fecha) VALUES
(1, 1, 101, 2, 5000, '2024-06-01'),
(2, 2, 102, 1, 7000, '2024-06-02'),
(3, 3, 103, 3, 10000, '2024-06-03'),
(4, 4, 104, 1, 6000, '2024-06-04'),
(5, 5, 105, 2, 8000, '2024-06-05'),
(6, 1, 101, 1, 5000, '2024-06-06'),
(7, 2, 102, 2, 7000, '2024-06-07'),
(8, 3, 103, 1, 10000, '2024-06-08'),
(9, 4, 104, 3, 6000, '2024-06-09'),
(10, 5, 105, 2, 8000, '2024-06-10');

-- Eliminar tablas si ya existen
DROP TABLE IF EXISTS ventas;
DROP TABLE IF EXISTS productos;
DROP TABLE IF EXISTS clientes;