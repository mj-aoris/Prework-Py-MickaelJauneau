/*Ejercicios 2*/
/*16. Realizar una consulta que muestre el nombre del cliente y el total de pedidos
realizados por cada cliente.*/


SELECT c.nombre,p.cantidad FROM public.clientes c
LEFT JOIN public.pedidos p
ON c.id = p.cliente_id

SELECT c.nombre, count(p.id) FROM public.clientes c
LEFT JOIN public.pedidos p
ON c.id = p.cliente_id
group BY c.nombre  


/*17. Realizar una consulta que muestre el nombre del producto y la cantidad total de
pedidos de ese producto.*/

# No hay FK hacia la tabla de productos. 

SELECT producto, count(producto) FROM public.pedidos
group BY producto

/*18. Agregar una columna llamada "fecha" a la tabla "Pedidos" de tipo fecha.*/

ALTER TABLE public.pedidos
ADD fecha DATE


/*19. Agregar una clave externa a la tabla "Pedidos" que haga referencia a la tabla
"Productos" en la columna "producto".*/



# asumiendo la utilización del id, ajustamos las entradas antes de realizar los 2 cambios, y añadimos un FK: 

ALTER TABLE public.pedidos
ALTER COLUMN producto TYPE int USING producto::integer;

ALTER TABLE public.pedidos 
ADD FOREIGN KEY (producto) REFERENCES public.productos(id)



/*20. Realizar una consulta que muestre los nombres de los clientes, los nombres de
los productos y las cantidades de los pedidos donde coincida la clave externa.*/


SELECT c.nombre,p.cantidad,r.nombre FROM public.clientes c
LEFT JOIN public.pedidos p
ON p.cliente_id = c.id
LEFT JOIN public.productos r
ON p.producto = r.id


