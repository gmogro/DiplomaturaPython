import util_db as db

conexion = db.get_connection()

db.insert_cliente("Milagros","Siempre Viva",
                 "111111","mila@gmail.com")
db.insert_cliente("Pepe","Caseros 123",
                 "123123","pepe@gmail.com")


db.insert_producto("Televisores","55 pulgadas",
                    700000,10)
db.insert_producto("Televisores","32 pulgadas",
                    450000,5)

carrito = [1,2]
db.insert_venta(1,"12-09-2024",1000000)
for producto_id in carrito:
    db.insert_detalle_venta(1,producto_id,1,700000,700000)