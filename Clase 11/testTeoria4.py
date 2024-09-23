import tkinter as tk
class MiAplicacion :

    def __init__(self,root):
        self.button = tk.Button(root , text ="Presionar",command= self.accion ) 
        self.button.pack()

    def accion(self):
        print("Botón presionado")
ventana = tk.Tk()
ventana.geometry("500x400")
app = MiAplicacion(ventana)
ventana.mainloop()