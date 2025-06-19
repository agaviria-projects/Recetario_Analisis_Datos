-- consultas_intermedias.sql
-- 📘 Ejemplos de consultas intermedias en SQL

-- Guía práctica:
-- Pregunta que te haces	        ¿Desde qué tabla partir (FROM)?
-- ¿Cuánto se vendió?	             ventas o envios (hecho)
-- ¿Quién compró más?	             ventas o envios (hecho)
-- ¿Cuánto costó enviar?	         envios o costos_envio (hecho)
-- ¿Qué producto no se ha vendido?	 productos (dimensión) con LEFT JOIN

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
-- Siempre colocar la tabla de hechos en el FROM:Porque es donde están los eventos, transacciones o 
-- acciones que se pueden contar, sumar, agrupar, etc
--Una tabla de hechos tiene muchas filas por producto, cliente o zona → cada fila es un registro de algo que pasó.
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

--Obtener el total de ventas monetarias por zona, incluyendo el nombre del producto, zona y ciudad.
-- FROM envios e → empezamos desde la tabla de hechos
-- JOIN productos p → para traer el precio del producto
-- JOIN zonas z → para saber a qué zona fue el envío
-- SUM(e.cantidad * p.precio_unitario) → calcula el total en dinero
-- GROUP BY → agrupamos por zona y producto
-- ORDER BY → ordenamos de mayor a menor
-- z=tabla zona, p=tabla productos, e=tabla envios
SELECT
	z.nombre_zona,
    z.ciudad,
    p.nombre AS producto,
    SUM(e.cantidad * p.precio_unitario)AS total_ventas
    FROM envios e
    JOIN productos p ON e.id_producto = p.id_producto
    JOIN zonas z ON e.id_zona = z.id_zona
    GROUP BY z.nombre_zona,z.ciudad,p.nombre
    ORDER BY total_ventas DESC;