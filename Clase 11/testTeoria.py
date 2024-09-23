import tkinter as tk
from tkinter import ttk
# Crear ventana
root = tk.Tk() 
root.title ("Ejemplo ttk")
root.geometry("500x400")
#Crear un botón
ttkbtn = ttk.Button(root , text ="Haz clicaquí")
ttkbtn.pack(pady =10)
#Crear un combobox
ttkcombo = ttk.Combobox(root , values =["Opción 1", "Opción 2", "Opción3"])
ttkcombo.set("Selecciona una opción")
ttkcombo.pack(pady =10)
#Iniciar la aplicación
root.mainloop()