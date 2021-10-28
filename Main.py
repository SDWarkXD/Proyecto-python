from tkinter import*
from tkinter.ttk import*
import tkinter.font as tkFont
import tkinter as tk
from tkinter import ttk
import iniciarsesion    
import registrarse                                         #Imports modules

root=Tk()
root.title("Kukulkan")
root.geometry("1200x700")
root.resizable(width=False, height=False)

imagen = PhotoImage(file = "f_principal.png")

# Con Label y la opción image, puedes mostrar una imagen en el widget:
background = Label(image = imagen, text = "Imagen S.O de fondo")

# Con place puedes organizar el widget de la imagen posicionandolo
# donde lo necesites (relwidth y relheight son alto y ancho en píxeles):
background.place(x = 0, y = 0, relwidth = 1, relheight = 1)

fontStyle = tkFont.Font(family="Malgun Gothic", size=80, slant="italic")
fontStyle2 = tkFont.Font(family="Malgun Gothic", size=30)


s = ttk.Style()
s.configure(
    "MyButton.TButton",
    foreground="#000000",
    background="#BCCA7E",
    font=("Malgun Gothic", 55,"bold"),
    anchor="w"
)


def ventana_login():
    root.destroy()
    iniciarsesion.iniciarSesion()

def ventana_registrarse():
    root.destroy()
    registrarse.registrarse()

def inicio_app():
    
    bt_inicio=Button(root, text="Iniciar Sesión", command=ventana_login, style="MyButton.TButton")
    bt_inicio.place(x=420, y=342)
    
    bt_registrarse=Button(root, text="Crear Cuenta", command=ventana_registrarse, style="MyButton.TButton")
    bt_registrarse.place(x=420, y=450)

root.wm_attributes('-transparentcolor','grey')

inicio_app()
root.mainloop()
