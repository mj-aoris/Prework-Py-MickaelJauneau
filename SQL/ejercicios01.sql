/*Ejercicio 1
1. Crear una tabla llamada "Clientes" con las columnas: id (entero, clave primaria),
nombre (texto) y email (texto).*/

CREATE TABLE  IF NOT EXISTS public.clientes (
	id SERIAL PRIMARY KEY,
	nombre  VARCHAR(255),
	email VARCHAR(255)	
);

/*2. Insertar un nuevo cliente en la tabla "Clientes" con id=1, nombre="Juan" y
email="juan@example.com".*/


INSERT INTO public.clientes (nombre,email)
VALUES ('Juan','juan@gmail.com');


/*3. Actualizar el email del cliente con id=1 a "juan@gmail.com".*/

UPDATE public.clientes SET email = 'juan@GMAIL.com'
WHERE public.clientes.id = 1

/*4. Eliminar el cliente con id=1 de la tabla "Clientes".*/

DELETE FROM public.clientes 
WHERE public.clientes.id = 1

/*5. Crear una tabla llamada "Pedidos" con las columnas: id (entero, clave primaria),
cliente_id (entero, clave externa referenciando a la tabla "Clientes"), producto
(texto) y cantidad (entero).*/

CREATE TABLE IF NOT EXISTS public.pedidos (
	id SERIAL PRIMARY KEY,
	cliente_id INT,
	producto VARCHAR(1024),
	cantidad INT,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id)	
);


/*6. Insertar un nuevo pedido en la tabla "Pedidos" con id=1, cliente_id=1,
producto="Camiseta" y cantidad=2.*/


INSERT INTO public.pedidos (cliente_id, producto,cantidad)
VALUES ('1','Camiseta', 2)


/*7. Actualizar la cantidad del pedido con id=1 a 3.*/

UPDATE public.pedidos SET cantidad = 3
WHERE public.pedidos.id = 1


/*8. Eliminar el pedido con id=1 de la tabla "Pedidos".*/


UPDATE public.pedidos SET cantidad = 3
WHERE public.pedidos.id = 1



/*9. Crear una tabla llamada "Productos" con las columnas: id (entero, clave
primaria), nombre (texto) y precio (decimal).*/

CREATE TABLE IF NOT EXISTS public.productos (
	id SERIAL PRIMARY KEY,
	nombre VARCHAR(255),
	precio DECIMAL(7,2)
)




/*10. Insertar varios productos en la tabla "Productos" con diferentes valores.*/

INSERT INTO public.productos (nombre, precio)
VALUES ('Gorra',25.95), ('Camisa',45.00),('Jersey',100),('Vaqueros',99.99),('Calcetines',3.33),('Bragas',21),('Guantes',35.35)



/*11. Consultar todos los clientes de la tabla "Clientes".*/

SELECT * from public.clientes

/*12. Consultar todos los pedidos de la tabla "Pedidos" junto con los nombres de los
clientes correspondientes.*/


SELECT p.id, p.producto, p.cantidad, c.nombre FROM public.pedidos p
LEFT JOIN public.clientes c
ON p.cliente_id = c.id 



/*13. Consultar los productos de la tabla "Productos" cuyo precio sea mayor a $50.*/

SELECT * FROM public.productos
WHERE precio > 50


/*14. Consultar los pedidos de la tabla "Pedidos" que tengan una cantidad mayor o
igual a 5.*/

SELECT * FROM public.pedidos
WHERE cantidad >= 5


/*15. Consultar los clientes de la tabla "Clientes" cuyo nombre empiece con la letra
"A".*/


SELECT * FROM public.clientes
WHERE nombre ILIKE 'j%'