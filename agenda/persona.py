class Persona:
    def __init__(self,apellido,nombre):
        self.apellido = apellido
        self.nombre = nombre
    
    def __str__(self):
        return f"{apellido},{nombre}"
