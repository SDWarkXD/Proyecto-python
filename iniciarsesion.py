import mysql.connector
from tkinter import*
from tkinter.ttk import*
import tkinter.font as tkFont
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import Game1                                              #Imports modules
def iniciarSesion():
    root=Tk()

    root.title("Iniciar Sesión")
    root.geometry("1200x700")
    root.resizable(width=False, height=False)


    imagen = PhotoImage(file = "f_iniciar.png")

    # Con Label y la opción image, puedes mostrar una imagen en el widget:
    background = Label(image = imagen, text = "Imagen S.O de fondo")

    # Con place puedes organizar el widget de la imagen posicionandolo
    # donde lo necesites (relwidth y relheight son alto y ancho en píxeles):
    background.place(x = 0, y = 0, relwidth = 1, relheight = 1)

    fontStyle3 = tkFont.Font(family="Malgun Gothic", size=35 )

    s = ttk.Style()
    s.configure(
        "MyButton.TButton",
        foreground="#000000",
        background="#BCCA7E",
        font=("Malgun Gothic", 40,"bold")
    )

    username_login_entry = Entry(root, font=fontStyle3)
    username_login_entry.place(x=550, y=300)
    password__login_entry = Entry(root, show= '*', font=fontStyle3)
    password__login_entry.place(x=550, y=400)
    def helloCallBack():
        miConexion = mysql.connector.connect( host='localhost', user= 'root', passwd='', db='kukulcan' )
        cur = miConexion.cursor()
        cur.execute( "SELECT * FROM usuarios where usuario = '"+username_login_entry.get()+"' and contraseña = '"+password__login_entry.get()+"'" )
        row = cur.fetchone()
        if row == None:
            print("There are no results for this query")
            messagebox.showinfo(message="El nombre de usuario o contraseña es incorrecto", title="Error")
        else:
            print(row)
            root.destroy()
            Game1.main()
        miConexion.close()

    Button(root, text="Iniciar", command = helloCallBack, style="MyButton.TButton").place(x=700, y=500)

    
    root.mainloop() 


