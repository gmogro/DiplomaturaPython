import tkinter as tk
class MiVentana :

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Ventana")
        self.root.geometry("500x400")
        self.label = tk.Label(self.root,text ="¡Hola")
        self.label.pack()

    def mostrar(self):
        self.root.mainloop()

#Instaciando la Ventana
ventana = MiVentana()

ventana.mostrar()