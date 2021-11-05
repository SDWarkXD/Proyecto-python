import mysql.connector
from tkinter import*
from tkinter.ttk import*
import tkinter.font as tkFont
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import Game1                                              #Imports modules
import Game2                                              #Imports modules
import Game3                                              #Imports modules
import Game4                                              #Imports modules

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
            #print(row[0])
            #print(row[1])
            #print(row[2])
            #print(row[3])
            root.destroy()
            if row[2] == 0:
                Game1.main(row[3],row[0])
            elif row[2] == 1:
                Game2.main(row[3],row[0])
            elif row[2] == 2:
                Game3.main(row[3],row[0])
            elif row[2] == 3:
                Game4.main(row[3],row[0])
            elif row[2] == 4:
                Game1.main(row[3],row[0])    
        miConexion.close()

    Button(root, text="Iniciar", command = helloCallBack, style="MyButton.TButton").place(x=700, y=500)

    
    root.mainloop() 


