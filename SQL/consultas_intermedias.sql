-- consultas_intermedias.sql
-- 📘 Ejemplos de consultas intermedias en SQL

--1️⃣ INNER JOIN: Ventas con nombres de clientes y productos
--✔️ Une las tres tablas y devuelve datos legibles para análisis.
SELECT v.id_venta, c.nombre AS cliente, p.nombre AS producto, v.fecha, v.cantidad, v.precio_unitario
FROM ventas v
INNER JOIN clientes c ON v.id_cliente = c.id_cliente
INNER JOIN productos p ON v.id_producto = p.id_producto;

--2️⃣ LEFT JOIN: Ver clientes aunque no hayan comprado aún
--✔️ Incluye clientes sin ventas (valor nulo en v.id_venta si no ha comprado).
SELECT c.nombre, v.id_venta, v.fecha
FROM clientes c
LEFT JOIN ventas v ON c.id_cliente = v.id_cliente;

--3️⃣ Ventas totales por ciudad
--✔️ Agrupa por ciudad y calcula valor total vendido.
SELECT c.ciudad, SUM(v.cantidad * v.precio_unitario) AS total_ventas
FROM ventas v
JOIN clientes c ON v.id_cliente = c.id_cliente
GROUP BY c.ciudad
ORDER BY total_ventas DESC;

--4️⃣ Conteo de productos vendidos por categoría
--✔️ Muy útil para saber qué categorías se venden más.
SELECT p.categoria, COUNT(v.id_venta) AS cantidad_ventas
FROM ventas v
JOIN productos p ON v.id_producto = p.id_producto
GROUP BY p.categoria
ORDER BY cantidad_ventas DESC;

--5️⃣ Producto más vendido por unidades
--✔️ Devuelve el producto más vendido en cantidad.
SELECT p.nombre, SUM(v.cantidad) AS total_unidades
FROM ventas v
JOIN productos p ON v.id_producto = p.id_producto
GROUP BY p.nombre
ORDER BY total_unidades DESC
LIMIT 1;

--6️⃣ Ventas por mes y año
--✔️ Ideal para Power BI si quieres validar contra medidas temporales.
SELECT YEAR(v.fecha) AS anio, MONTH(v.fecha) AS mes, SUM(v.cantidad * v.precio_unitario) AS total_ventas
FROM ventas v
GROUP BY anio, mes
ORDER BY anio, mes;

--Precio promedio de venta por categoría
SELECT p.categoria, AVG(v.precio_unitario) AS precio_promedio
FROM ventas v
JOIN productos p ON v.id_producto = p.id_producto
GROUP BY p.categoria;

--✅ Consulta SQL: Ventas asociadas a Medellín
SELECT v.*
FROM ventas v
JOIN clientes c ON v.id_cliente=c.id_cliente
WHERE c.ciudad = 'Medellin';