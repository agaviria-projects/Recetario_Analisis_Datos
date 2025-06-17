-- consultas_basicas.sql
-- 📘 Ejemplos de consultas básicas en SQL

-- Seleccionar todos los campos de la tabla productos
SELECT * FROM productos;

-- Seleccionar columnas específicas
SELECT nombre, categoria FROM productos;

-- Filtrar con WHERE
SELECT * FROM clientes
WHERE ciudad = 'Medellín';

-- Operadores lógicos AND / OR
SELECT * FROM ventas
WHERE cantidad > 2 AND precio_unitario > 5000;

-- Ordenar resultados
SELECT * FROM ventas
ORDER BY precio_unitario DESC;

-- Uso de alias
SELECT precio_unitario AS precio
FROM ventas;

--🔧 1. Eliminar registros 2024
DELETE FROM ventas
WHERE YEAR(fecha) = 2024;
