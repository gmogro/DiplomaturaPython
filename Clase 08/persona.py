class Persona:
    def __init__(self,nombre,apellido,edad):
        self.apellido = apellido
        self.nombre = nombre
        self.edad = edad
    
    def __str__(self):
        return f"{self.apellido} - {self.nombre} - {self.edad}"