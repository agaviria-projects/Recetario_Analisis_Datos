-- subconsultas_y_alias.sql
-- 🧠 Subconsultas y alias

-- Clientes que han comprado más de 10000 en total
SELECT nombre, total
FROM (
  SELECT c.nombre, SUM(v.cantidad * v.precio_unitario) AS total
  FROM ventas v
  JOIN clientes c ON v.id_cliente = c.id_cliente
  GROUP BY c.nombre
) AS resumen
WHERE total > 10000;

-- Subconsulta en WHERE
SELECT nombre
FROM productos
WHERE id_producto IN (
  SELECT id_producto
  FROM ventas
  WHERE cantidad > 2
);
