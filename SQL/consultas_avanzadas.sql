-- 📅 Día 2 – Consultas SQL Avanzadas (Semana 3)
-- Base de datos: logistica_pedidos

-- 1️⃣ Total de pedidos por ciudad de cliente
--Cuántos pedidos vienen de clientes según su ciudad de origen.
--JOIN unir tablas
--GROUP BY agrupa
SELECT c.ciudad, COUNT(p.id_pedido) AS total_pedidos
FROM pedidos p
JOIN clientes c ON p.id_cliente = c.id_cliente
GROUP BY c.ciudad;

-- 2️⃣ Promedio de retraso en entregas por ciudad de bodega
--Une entregas con pedidos → y de ahí con bodegas
--Filtra solo entregas retrasado
--Calcula el promedio de días de retraso por ciudad
SELECT b.ciudad, ROUND(AVG(e.dias_retraso), 2) AS retraso_promedio
FROM entregas e
JOIN pedidos p ON e.id_pedido = p.id_pedido
JOIN bodegas b ON p.id_bodega = b.id_bodega
WHERE e.estado = 'retrasado'
GROUP BY b.ciudad;

-- 3️⃣ Pedidos entregados a tiempo vs retrasados
--Cuántas entregas están:
--entregado
--pendiente
--retrasado
SELECT estado, COUNT(*) AS total
FROM entregas
GROUP BY estado;

-- 4️⃣ Pedidos con formato de fecha y total en miles
--Formatea la fecha como DD-MM-YYYY
--Formatea el total con separadores de miles (320000 → 320,000 o según configuración)
SELECT 
  id_pedido,
  DATE_FORMAT(fecha_pedido, '%d-%m-%Y') AS fecha_formateada,
  FORMAT(total, 0) AS total_en_miles
FROM pedidos;

-- 5️⃣ Pedidos con más de 250.000
SELECT * FROM pedidos
WHERE total > 250000
ORDER BY total DESC;

-- 6️⃣ TOP 3 ciudades con más entregas completadas
SELECT c.ciudad, COUNT(e.id_entrega) AS total_entregas
FROM entregas e
JOIN pedidos p ON e.id_pedido = p.id_pedido
JOIN clientes c ON p.id_cliente = c.id_cliente
WHERE e.estado = 'entregado'
GROUP BY c.ciudad
ORDER BY total_entregas DESC
LIMIT 3;

-- 7️⃣ Porcentaje de entregas pendientes
SELECT 
  ROUND(SUM(CASE WHEN estado = 'pendiente' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS porcentaje_pendientes
FROM entregas;

-- 8️⃣ Entregas con días de retraso mayores a 3
SELECT * FROM entregas
WHERE dias_retraso > 3;

-- Clasificación de pedidos según el monto total
--CASE evalúa cada fila individualmente.
-- Retorna una etiqueta
--   'Alto' si total ≥ 300,000
--   'Medio' si está entre 200,000 y 299,999
--   'Bajo' si es menor a 200,000
--ORDER BY total DESC organiza los pedidos de mayor a menor valor.
-- Te da una nueva columna llamada categoria_pedido
SELECT 
  id_pedido,
  total,
  CASE
    WHEN total >= 300000 THEN 'Alto'
    WHEN total BETWEEN 200000 AND 299999 THEN 'Medio'
    ELSE 'Bajo'
  END AS categoria_pedido
FROM pedidos
ORDER BY total DESC;

--Usar IF() para mostrar un mensaje personalizado
-- Si total es mayor a 250.000, devuelve 'Pedido Grande'
-- Si no, devuelve 'Pedido Estándar'
-- útil si quieres hacer clasificaciones rápidas sin CASE.
SELECT 
  id_pedido,
  total,
  IF(total > 250000, 'Pedido Grande', 'Pedido Estándar') AS tipo_pedido
FROM pedidos;

--Usar HAVING con agrupación
--Agrupa los pedidos por ciudad del cliente
--Filtra los grupos que tengan más de 2 pedidos
--HAVING se usa después de GROUP BY, a diferencia de WHERE que se usa antes.
SELECT 
  c.ciudad,
  COUNT(p.id_pedido) AS total_pedidos
FROM pedidos p
JOIN clientes c ON p.id_cliente = c.id_cliente
GROUP BY c.ciudad
HAVING total_pedidos > 2;
