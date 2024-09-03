from persona import Persona

class contacto(Persona):
    def __init__(self,apellido,nombre,telefono,email):
        super().__init__(apellido,nombre)
        self.telefono = telefono
        self.email = email
    
    def __str__(self):
        mensaje = super().__str__()
        return mensaje + f"- {self.telefono}"
    
    