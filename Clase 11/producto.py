class Producto:
    def __init__(self, id_producto, nombre, descripcion, precio, stock):
        self.id_producto = id_producto
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock
    
    def to_json(self):
        return {
           "id_producto": self.id_producto,
           "nombre" : self.nombre,
           "descripcion" : self.descripcion,
           "precio" : self.precio,
           "stock" : self.stock
        }

    @classmethod
    def from_json(cls,data):
        id_producto = data["id_producto"]
        nombre = data["nombre"]
        descripcion = data["descripcion"]
        precio = data["precio"]
        stock = data["stock"]
        return Producto(id_producto,nombre,descripcion,precio,stock)
