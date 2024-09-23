import sqlite3

def get_connection():
    return sqlite3.connect('tienda.db')


def insert_cliente(nombre, direccion, telefono, email):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO clientes (nombre, direccion, telefono, email)
        VALUES (?, ?, ?, ?)
    ''', (nombre, direccion, telefono, email))
    conn.commit()
    conn.close()

def insert_producto(nombre, descripcion, precio, stock):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO productos (nombre, descripcion, precio, stock)
        VALUES (?, ?, ?, ?)
    ''', (nombre, descripcion, precio, stock))
    conn.commit()
    conn.close()

def insert_venta(id_cliente, fecha_venta, total):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO ventas (id_cliente, fecha_venta, total)
        VALUES (?, ?, ?)
    ''', (id_cliente, fecha_venta, total))
    conn.commit()
    conn.close()

def insert_detalle_venta(id_venta, id_producto, cantidad, precio_unitario, subtotal):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO detalle_venta (id_venta, id_producto, cantidad, precio_unitario, subtotal)
        VALUES (?, ?, ?, ?, ?)
    ''', (id_venta, id_producto, cantidad, precio_unitario, subtotal))
    conn.commit()
    conn.close()

def update_cliente(id_cliente, nombre=None, direccion=None, telefono=None, email=None):
    conn = get_connection()
    cursor = conn.cursor()
    if nombre:
        cursor.execute('''
            UPDATE clientes
            SET nombre = ?
            WHERE id_cliente = ?
        ''', (nombre, id_cliente))
    if direccion:
        cursor.execute('''
            UPDATE clientes
            SET direccion = ?
            WHERE id_cliente = ?
        ''', (direccion, id_cliente))
    if telefono:
        cursor.execute('''
            UPDATE clientes
            SET telefono = ?
            WHERE id_cliente = ?
        ''', (telefono, id_cliente))
    if email:
        cursor.execute('''
            UPDATE clientes
            SET email = ?
            WHERE id_cliente = ?
        ''', (email, id_cliente))
    conn.commit()
    conn.close()

def update_producto(id_producto, nombre=None, descripcion=None, precio=None, stock=None):
    conn = get_connection()
    cursor = conn.cursor()
    if nombre:
        cursor.execute('''
            UPDATE productos
            SET nombre = ?
            WHERE id_producto = ?
        ''', (nombre, id_producto))
    if descripcion:
        cursor.execute('''
            UPDATE productos
            SET descripcion = ?
            WHERE id_producto = ?
        ''', (descripcion, id_producto))
    if precio:
        cursor.execute('''
            UPDATE productos
            SET precio = ?
            WHERE id_producto = ?
        ''', (precio, id_producto))
    if stock:
        cursor.execute('''
            UPDATE productos
            SET stock = ?
            WHERE id_producto = ?
        ''', (stock, id_producto))
    conn.commit()
    conn.close()

def delete_cliente(id_cliente):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        DELETE FROM clientes
        WHERE id_cliente = ?
    ''', (id_cliente,))
    conn.commit()
    conn.close()

def delete_producto(id_producto):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        DELETE FROM productos
        WHERE id_producto = ?
    ''', (id_producto,))
    conn.commit()
    conn.close()

def get_clientes():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clientes')
    rows = cursor.fetchall()
    conn.close()
    return rows

def get_cliente(id_cliente):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clientes WHERE id_cliente = ?', (id_cliente,))
    row = cursor.fetchone()
    conn.close()
    return row

def get_cliente(id_cliente):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clientes WHERE id_cliente = ?', (id_cliente,))
    row = cursor.fetchone()
    conn.close()
    return row

def get_productos():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM productos')
    rows = cursor.fetchall()
    conn.close()
    return rows

def get_producto(id_producto):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM productos WHERE id_producto = ?', (id_producto,))
    row = cursor.fetchone()
    conn.close()
    return row



