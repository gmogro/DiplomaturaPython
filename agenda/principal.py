import util_db as db

# Conectar a la base de datos
conexion = db.conectar_db('agenda.db')
# Crear la tabla
db.crear_tabla(conexion)

# Insertar usuarios
db.insertar_contacto(conexion,"Quispe",'Juan', "11111111", 'juan@example.com')
db.insertar_contacto(conexion,"Tevez", 'Pedro',"222222", 'pedro@example.com')
db.insertar_contacto(conexion,"Messi",'Juan',"4444444", 'juan@example.com')


contactos = db.consultar_todos_contactos(conexion)
for contacto in contactos:
    print(contacto)

db.cerrar_conexion(conexion)