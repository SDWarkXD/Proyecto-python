
print ('Resultados de mysql.connector:')
import mysql.connector
miConexion = mysql.connector.connect( host='localhost', user= 'root', passwd='', db='kukulcan' )
cur = miConexion.cursor()
cur.execute( "SELECT usuario, contraseña FROM usuarios" )
for nombre, apellido in cur.fetchall() :
    print (nombre, apellido)
miConexion.close()