-- 📦 Semana 1 – Día 4: Recetario SQL básico

-- 1. Crear base de datos
CREATE DATABASE ventas_db;
USE ventas_db;

-- 2. Crear tabla clientes
CREATE TABLE clientes (
  id_cliente INT PRIMARY KEY,
  nombre VARCHAR(50),
  categoria VARCHAR(20),
  ciudad VARCHAR(50)
);

-- 3. Insertar datos de prueba
INSERT INTO clientes (id_cliente, nombre, categoria, ciudad) VALUES
(1, 'Andrés', 'Hombre', 'Medellín'),
(2, 'Diana', 'Mujer', 'Bogotá'),
(3, 'Laura', 'Mujer', 'Medellín'),
(4, 'Carlos', 'Hombre', 'Cali');

-- 4. Consultas básicas
-- Ver todos los clientes
SELECT * FROM clientes;

-- Filtrar por ciudad
SELECT * FROM clientes WHERE ciudad = 'Medellín';

-- Ordenar por nombre
SELECT * FROM clientes ORDER BY nombre ASC;

-- Mostrar solo 2 registros
SELECT * FROM clientes LIMIT 2;

--INSERT – Agregar nuevos clientes
INSERT INTO clientes (id_cliente, nombre, categoria, ciudad) VALUES
(5, 'Natalia', 'Mujer', 'Bucaramanga'),
(6, 'Julio', 'Hombre', 'Cartagena');

--UPDATE – Modificar datos
UPDATE clientes
SET ciudad = 'Barranquilla'
WHERE nombre = 'Carlos'

UPDATE clientes
SET categoria ='Otro'
WHERE nombre ='Laura'

--DELETE – Eliminar registros
DELETE FROM clientes
WHERE nombre ='Julio';

--Eliminar por ID
DELETE FROM clientes
WHERE id_cliente=3;

--Verificación (siempre útil después de cada acción)
