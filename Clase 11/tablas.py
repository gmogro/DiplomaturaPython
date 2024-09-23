import sqlite3

# Conectar a la base de datos (se creará si no existe)
conexion = sqlite3.connect('tienda.db')

# Crear un cursor para ejecutar comandos SQL
cursor = conexion.cursor()

# Crear tabla clientes
cursor.execute('''
CREATE TABLE IF NOT EXISTS clientes (
    id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre VARCHAR(100),
    direccion VARCHAR(255),
    telefono VARCHAR(20),
    email VARCHAR(100)
);
''')

# Crear tabla productos
cursor.execute('''
CREATE TABLE IF NOT EXISTS productos (
    id_producto INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre VARCHAR(100),
    descripcion TEXT,
    precio DECIMAL(10, 2),
    stock INTEGER
);
''')

# Crear tabla ventas
cursor.execute('''
CREATE TABLE IF NOT EXISTS ventas (
    id_venta INTEGER PRIMARY KEY AUTOINCREMENT,
    id_cliente INTEGER,
    fecha_venta DATE,
    total DECIMAL(10, 2)
);
''')

# Crear tabla detalle_venta
cursor.execute('''
CREATE TABLE IF NOT EXISTS detalle_venta (
    id_detalle INTEGER PRIMARY KEY AUTOINCREMENT,
    id_venta INTEGER,
    id_producto INTEGER,
    cantidad INTEGER,
    precio_unitario DECIMAL(10, 2),
    subtotal DECIMAL(10, 2)
);
''')

""" # Crear tabla usuarios
cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
    id_rol INTEGER,
    nombre VARCHAR(100),
    direccion VARCHAR(255),
    telefono VARCHAR(20),
    email VARCHAR(100),
    password VARCHAR(250)
);
''')

# Crear tabla roles
cursor.execute('''
CREATE TABLE IF NOT EXISTS roles (
    id_rol INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre VARCHAR(100),
    descripcion VARCHAR(100)
);
''') """

# Guardar cambios y cerrar conexión
conexion.commit()
conexion.close()

print("Tablas creadas con éxito.")
