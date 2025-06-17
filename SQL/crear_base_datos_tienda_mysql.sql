-- crear_base_datos_tienda_mysql.sql
-- 🎯 Script para crear una base de datos empresarial en MySQL

-- 🧱 Eliminar base si existe
DROP DATABASE IF EXISTS tienda;
CREATE DATABASE tienda;
USE tienda;

-- 👥 Tabla de clientes
CREATE TABLE clientes (
    id_cliente INT PRIMARY KEY,
    nombre VARCHAR(100),
    ciudad VARCHAR(100)
);

-- 📦 Tabla de productos
CREATE TABLE productos (
    id_producto INT PRIMARY KEY,
    nombre VARCHAR(100),
    categoria VARCHAR(100)
);

-- 🧾 Tabla de ventas
CREATE TABLE ventas (
    id_venta INT PRIMARY KEY,
    id_cliente INT,
    id_producto INT,
    cantidad INT,
    precio_unitario DECIMAL(10,2),
    fecha DATE,
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente),
    FOREIGN KEY (id_producto) REFERENCES productos(id_producto)
);

-- 🔽 Insertar clientes
INSERT INTO clientes (id_cliente, nombre, ciudad) VALUES
(1, 'Ana', 'Bogotá'),
(2, 'Luis', 'Medellín'),
(3, 'Carlos', 'Cali'),
(4, 'Marta', 'Barranquilla'),
(5, 'Julia', 'Cartagena');

-- 🔽 Insertar productos
INSERT INTO productos (id_producto, nombre, categoria) VALUES
(101, 'Mouse', 'Accesorio'),
(102, 'Teclado', 'Accesorio'),
(103, 'Monitor', 'Pantalla'),
(104, 'Webcam', 'Accesorio'),
(105, 'Impresora', 'Oficina');

-- 🔽 Insertar ventas
INSERT INTO ventas (id_venta, id_cliente, id_producto, cantidad, precio_unitario, fecha) VALUES
(1, 1, 101, 2, 5000.00, '2024-06-01'),
(2, 2, 102, 1, 7000.00, '2024-06-02'),
(3, 3, 103, 3, 10000.00, '2024-06-03'),
(4, 4, 104, 1, 6000.00, '2024-06-04'),
(5, 5, 105, 2, 8000.00, '2024-06-05'),
(6, 1, 101, 1, 5000.00, '2024-06-06'),
(7, 2, 102, 2, 7000.00, '2024-06-07'),
(8, 3, 103, 1, 10000.00, '2024-06-08'),
(9, 4, 104, 3, 6000.00, '2024-06-09'),
(10, 5, 105, 2, 8000.00, '2024-06-10');
