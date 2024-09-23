import tkinter as tk
from tkinter import ttk
class App(tk.Tk):
    def __init__(self,):
        super().__init__()
        self.configurar_ventana()
        self.configurar_grid()
        self.mostrar_titulo()

    def configurar_ventana(self):
        self.geometry("700x500")
        self.title("Tienda de electrodomesticos")
        self.configure(background="#1d2d44")

    def configurar_grid(self):
        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=1)
    
    def mostrar_titulo(self):
        etiqueta = ttk.Label(self, text="Tienda de Electrodomestiocos",
                            font=('Arial',20),foreground='white',background="#1d2d44")
        etiqueta.grid(row=0,column=0,columnspan=2,pady=30)
    

    

if __name__ == '__main__':
    app = App()
    app.mainloop()