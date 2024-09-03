import sqlite3

def conectar_db(nombre_db):
    return sqlite3.connect(nombre_db)

def crear_tabla(conexion):
    with conexion:
        conexion.execute("""
        CREATE TABLE IF NOT EXISTS contacto(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            apellido TEXT,
            nombre TEXT NOT NULL,
            telefono TEXT NOT NULL,
            email TEXT NOT NULL)""")

def insertar_contacto(conexion,apellido,nombre,telefono,email):
    try:
        with conexion:
            conexion.execute("""
            INSERT INTO contacto (apellido,nombre,telefono,email)
            VALUES (?,?,?,?)
            """,(apellido,nombre,telefono,email))
        print("Se creo el contacto")
    except sqlite3.IntegrityError as e:
        print(f"Error al insertar : {e}")

def consultar_todos_contactos(conexion):
    cursor = conexion.cursor()
    cursor.execute("SELECT id,apellido,nombre,telefono,email from contacto")
    return cursor.fetchall()

def cerrar_conexion(conexion):
    conexion.close()
