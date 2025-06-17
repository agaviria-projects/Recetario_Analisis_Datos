-- joins_groupby.sql
-- 🔗 Ejemplos de JOINs y GROUP BY

-- INNER JOIN entre ventas y clientes
SELECT v.id_venta, c.nombre AS cliente, v.fecha
FROM ventas v
INNER JOIN clientes c ON v.id_cliente = c.id_cliente;

-- LEFT JOIN para ver todos los productos, incluso sin ventas
SELECT p.nombre AS producto, v.cantidad
FROM productos p
LEFT JOIN ventas v ON p.id_producto = v.id_producto;

-- GROUP BY para sumar ventas por producto
SELECT p.nombre AS producto, SUM(v.cantidad) AS total_vendido
FROM ventas v
JOIN productos p ON v.id_producto = p.id_producto
GROUP BY p.nombre;
