from persona import Persona
class Contacto(Persona):
    def __init__(self,nombre,apellido,edad,telefono,email):
        super().__init__(nombre,apellido,edad)
        self.telefono = telefono
        self.email = email
    
    def __str__(self):
        return f"{self.apellido},{self.nombre}-{self.telefono}"

""" if __name__ == "__main__":
    contacto = Contacto("Guillermo","mogro",32,"12122121","g@aw.com")
    print(contacto) """