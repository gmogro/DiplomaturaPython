import tkinter as tk
# Crear ventana principal
root = tk.Tk()
root.title("Ejemplo de Frame")
root.geometry("500x400")
# Crear un frame
frame = tk.Frame(root , width= 400,height=200,bg= "lightblue", padx =10, pady =10)
frame.pack(padx =20 , pady =20)
# Añadir widgets dentro del frame
label = tk.Label(frame , text ="Etiqueta dentro del Frame")
label.pack()
button= tk.Button(frame , text ="Botón dentro del Frame")
button.pack()
#Iniciar el loop de la aplicación
root.mainloop()