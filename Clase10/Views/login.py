from tkinter import * #importar todos los componentes de tkinter
from tkinter import messagebox

def verificar_login(ventana_login,usuario,password):
    usario_bd = selectUsuario()
    if usuario == "admin" and password == "1234":
        abrir_ventana_principal(ventana_login)
    else:
        messagebox.showerror("Error","Usuario o contraseña incorrecta")

def abrir_ventana_principal(ventana_login):
    ventana_login.destroy()

    ventana_principal = Tk()
    ventana_principal.title("Inicio")
    ventana_principal.geometry("500x600")

    label_bievenida = Label(ventana_principal,text="¡Bienvenido a la aplicacion...")
    label_bievenida.pack(pady=30)

    boton_salir = Button(ventana_principal,text="Salir",command=ventana_principal.quit)
    boton_salir.pack(pady=20)

    return ventana_principal

def inicio_sesion():
    ventana_login = Tk()
    ventana_login.title("Inicio de Sesion")
    ventana_login.geometry("300x200")

    #Crear las etiquetas y los entrys
    label_usuario = Label(ventana_login, text = "Usuario: ")
    label_usuario.grid(row=0,column=0)
    entry_usuario = Entry(ventana_login)
    entry_usuario.grid(row=0,column=1)

    """ label_password = Label(ventana_login, text = "Contraseña")
    label_password.pack(pady = 5)
    entry_password = Entry(ventana_login,show="*")
    entry_password.pack(pady = 5) """

    """ boton_login  = Button(ventana_login,text="Iniciar Sesion", command= lambda: verificar_login(ventana_login,entry_usuario.get(),entry_password.get()))
    boton_login.pack(pady=5) """

    ventana_login.mainloop()