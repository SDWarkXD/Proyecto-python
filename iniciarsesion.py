import mysql.connector
from tkinter import*
from tkinter.ttk import*
import tkinter.font as tkFont
import tkinter as tk
from tkinter import ttk
import Game                                              #Imports modules
def iniciarSesion():
    root=Tk()

    root.title("Iniciar Sesión")
    root.geometry("1200x700")
    root.resizable(width=False, height=False)


    imagen = PhotoImage(file = "fondo_inicio.png")

    # Con Label y la opción image, puedes mostrar una imagen en el widget:
    background = Label(image = imagen, text = "Imagen S.O de fondo")

    # Con place puedes organizar el widget de la imagen posicionandolo
    # donde lo necesites (relwidth y relheight son alto y ancho en píxeles):
    background.place(x = 0, y = 0, relwidth = 1, relheight = 1)

    fontStyle = tkFont.Font(family="Malgun Gothic", size=80, slant="italic")
    fontStyle2 = tkFont.Font(family="Malgun Gothic", size=46, weight="bold")
    fontStyle3 = tkFont.Font(family="Malgun Gothic", size=40 )

    s = ttk.Style()
    s.configure(
        "MyButton.TButton",
        foreground="#FFFFFF",
        background="#BCCA7E",
        font=("Malgun Gothic", 50,"bold")
    )

    
    tituloAPP=Label(root, text="Kukulkan", font=fontStyle, background="#BCCA7E")
    tituloAPP.place(x=10, y=10)

    Label(root, text="Iniciar Sesión", font=fontStyle2 ).place(x=150, y=200)
    Label(root, text="Usuario", font=fontStyle3 ).place(x=300, y=300)
    username_login_entry = Entry(root, font=fontStyle3)
    username_login_entry.place(x=600, y=300)
    Label(root, text="Contraseña", font=fontStyle3).place(x=300, y=400)
    password__login_entry = Entry(root, show= '*', font=fontStyle3)
    password__login_entry.place(x=600, y=400)
    def helloCallBack():
        miConexion = mysql.connector.connect( host='localhost', user= 'root', passwd='', db='kukulcan' )
        cur = miConexion.cursor()
        cur.execute( "SELECT * FROM usuarios where usuario = '"+username_login_entry.get()+"' and contraseña = '"+password__login_entry.get()+"'" )
        row = cur.fetchone()
        if row == None:
            print("There are no results for this query")
        else:
            print(row)
            root.destroy()
            Game.main()
        miConexion.close()

    Button(root, text="Login", command = helloCallBack, style="MyButton.TButton").place(x=700, y=500)

    
    root.mainloop() 


