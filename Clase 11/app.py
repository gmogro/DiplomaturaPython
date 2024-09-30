import tkinter as tk
from tkinter import ttk
import util_db as db
class App(tk.Tk):
    def __init__(self,):
        super().__init__()
        self.configurar_ventana()
        self.configurar_grid()
        self.mostrar_titulo()
        self.mostrar_formulario()
        self.cargar_tabla()
        self.mostrar_botones()

    def configurar_ventana(self):
        self.geometry("700x500")
        self.title("Tienda de electrodomesticos")
        self.iconbitmap('tiendaElectIcon.ico')
        self.configure(background="#1d2d44")
        self.estilos = ttk.Style()
        self.estilos.theme_use('clam')
        self.estilos.configure(self, background="#1d2d44",foreground="white",fieldbackground="black")


    def configurar_grid(self):
        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=1)
    
    def mostrar_titulo(self):
        etiqueta = ttk.Label(self, text="Tienda de Electrodomesticos",
                            font=('Arial',20),foreground='white',background="#1d2d44")
        etiqueta.grid(row=0,column=0,columnspan=2,pady=30)
    
    def mostrar_formulario(self):
        self.frame_form = ttk.Frame()
        lnombre = ttk.Label(self.frame_form, text="Nombre")
        lnombre.grid(row=0,column=0,sticky=tk.W,padx=10,pady=10)
        self.eNombre = ttk.Entry(self.frame_form)
        self.eNombre.grid(row=0,column=1)

        ldescripcion = ttk.Label(self.frame_form, text="Descripcion")
        ldescripcion.grid(row=1,column=0,sticky=tk.W,padx=10,pady=10)
        self.eDescripcion = ttk.Entry(self.frame_form)
        self.eDescripcion.grid(row=1,column=1)

        lprecio = ttk.Label(self.frame_form, text="Precio")
        lprecio.grid(row=2,column=0,sticky=tk.W,padx=10,pady=10)
        self.ePrecio = ttk.Entry(self.frame_form)
        self.ePrecio.grid(row=2,column=1)

        lstock = ttk.Label(self.frame_form, text="Stock")
        lstock.grid(row=3,column=0,sticky=tk.W,padx=10,pady=10)
        self.eStock = ttk.Entry(self.frame_form)
        self.eStock.grid(row=3,column=1)

        self.frame_form.grid(row=1,column=0)

    def cargar_tabla(self):
        self.frame_tabla = ttk.Frame(self)
        self.estilos.configure('Treeview', background='black',foreground='white',fieldbackground='black', rowheight=20)
        
        columnas = ('Id','Nombre','Descripcion','Precio','Stock')
        self.tabla = ttk.Treeview(self.frame_tabla,columns=columnas,show='headings')
        self.tabla.heading('Id', text='Id', anchor=tk.CENTER)
        self.tabla.heading('Nombre', text='Nombre', anchor=tk.W)
        self.tabla.heading('Descripcion', text='Descripcion', anchor=tk.W)
        self.tabla.heading('Precio', text='Precio', anchor=tk.W)
        self.tabla.heading('Stock', text='Stock', anchor=tk.W)

        self.tabla.column('Id',anchor=tk.CENTER, width = 50)
        self.tabla.column('Nombre', anchor=tk.W, width = 100)
        self.tabla.column('Descripcion', anchor=tk.W, width = 100)
        self.tabla.column('Precio', anchor=tk.W, width = 100)
        self.tabla.column('Stock', anchor=tk.W, width = 100)

        productos = db.get_productos()
        print(productos)
        """ lista_productos = []
        for producto in productos:
            Producto.from_json(producto)

        for cliente in clientes:
            self.tabla.insert(parent='',index=tk.END,values=) """

        self.tabla.grid(row=0,column=0)
        self.frame_tabla.grid(row=1,column=1,padx=20)

    def mostrar_botones(self):
        self.frame_botones = ttk.Frame()

        btnAgregar = ttk.Button(self.frame_botones,text='Guardar')
        btnAgregar.grid(row=0,column=0,padx=30)

        btnEliminar = ttk.Button(self.frame_botones,text='Eliminar')
        btnEliminar.grid(row=0,column=1,padx=30)

        btnLimpiar = ttk.Button(self.frame_botones,text='Limpiar')
        btnLimpiar.grid(row=0,column=2,padx=30)

        self.estilos.configure('TButton',background='#005f73')
        self.estilos.map('TButton',background=[('active','#0a9396')])

        self.frame_botones.grid(row=2,column=0,columnspan=2,pady=20)

if __name__ == '__main__':
    app = App()
    app.mainloop()