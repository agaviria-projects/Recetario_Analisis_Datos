"""
🧩 PLANTILLA UNIVERSAL PARA CONSULTAS JOIN EN SQL

OBJETIVO:
Recordar la lógica completa para hacer una consulta que combine múltiples tablas 
siguiendo esta pregunta guía:

¿Quién hizo qué → desde dónde → cuándo → cómo terminó?

ESTRUCTURA:

1. Tabla central (hecho principal)
2. JOIN con entidades relacionadas
3. Selección de columnas clave
4. Orden o filtros opcionales

EJEMPLO APLICADO (Pedidos y Entregas):

"""

consulta = """
SELECT 
    p.id_pedido,
    c.nombre AS cliente,           -- ¿Quién pidió?
    b.nombre_bodega,              -- ¿Desde dónde salió?
    p.fecha_pedido,               -- ¿Cuándo se pidió?
    e.fecha_entrega,              -- ¿Cuándo se entregó?
    e.estado,                     -- ¿Cómo terminó?
    e.dias_retraso,
    p.total
FROM pedidos p
JOIN clientes c ON p.id_cliente = c.id_cliente
JOIN bodegas b ON p.id_bodega = b.id_bodega
JOIN entregas e ON p.id_pedido = e.id_pedido
ORDER BY p.fecha_pedido;
"""
