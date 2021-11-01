import mysql.connector
from tkinter import*
from tkinter.ttk import*
import tkinter.font as tkFont
import tkinter as tk
from tkinter import ttk
import Game                   
from tkinter import messagebox
                           #Imports modules
def registrarse():
    root=Tk()

    root.title("Crear Cuenta")
    root.geometry("1200x700")
    root.resizable(width=False, height=False)


    imagen = PhotoImage(file = "f_crear.png")

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
            
            cur = miConexion.cursor()
            ##mycursor = mydb.cursor()
            sql = "INSERT INTO usuarios (usuario, contraseña) VALUES (%s, %s)"
            val = (username_login_entry.get(),password__login_entry.get())
            cur.execute(sql, val)

            miConexion.commit()
            root.destroy()
            Game.main()


        else:
            messagebox.showinfo(message="El nombre de usuario o contraseña es incorrecto", title="Error")

        miConexion.close()

    Button(root, text="Crear Cuenta", command = helloCallBack, style="MyButton.TButton").place(x=700, y=500)

    
    root.mainloop() 


