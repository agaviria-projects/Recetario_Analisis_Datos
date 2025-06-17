-- practicas_sql_tienda.sql
-- 🛒 Consultas aplicadas a un modelo de tienda

-- Total de ventas por cliente
--Esto indica que trabajamos con la tabla ventas, pero le damos un alias v
-- Hacemos un INNER JOIN para unir la tabla clientes con la tabla ventas.
--Le damos a clientes el alias c, por eso escribimos c.nombre después.
--La condición ON v.id_cliente = c.id_cliente enlaza ambas tablas mediante la clave foránea.
SELECT c.nombre, SUM(v.cantidad * v.precio_unitario) AS total_ventas
FROM ventas v
JOIN clientes c ON v.id_cliente = c.id_cliente
GROUP BY c.nombre;

-- Categoría más vendida
--p.categoria: vas a mostrar la categoría del producto (viene de la tabla productos).
--SUM(v.cantidad): suma la cantidad de productos vendidos por categoría.
--AS total_vendido: a esa suma le das el nombre total_vendido.
--Indica que vas a trabajar con la tabla ventas, usando el alias v.
--JOIN...Estás uniendo la tabla ventas con la tabla productos, porque necesitas saber de qué categoría es cada producto vendido.
--p es alias de productos.
--La unión es por la columna en común: id_producto.
--Agrupas todas las ventas por categoría, para poder usar SUM y sumar la cantidad de unidades por categoría.
--Ordenas los resultados de mayor a menor (ventas más altas primero).
--LIMIT 1; Solo quieres ver una fila, es decir, la categoría con más ventas.

SELECT p.categoria, SUM(v.cantidad) AS total_vendida
FROM ventas v
JOIN productos p ON v.id_producto = p.id_producto
GROUP BY p.categoria
ORDER BY total_vendida DESC
LIMIT 1;

-- Promedio de unidades por venta
SELECT AVG(cantidad) AS promedio_unidades
FROM ventas;
