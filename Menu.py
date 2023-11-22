import sqlite3

from lib.altas.Altadeinfraccionado import crearAltaInfraccionado
from lib.createDatabase import createTables 
from lib.altas.Altadeinfracciones import crearInfraccion
from lib.altas.Altadepolicia import crearPolicia
from lib.altas.Registrodemultas import obtenerRegistroMultas

conn = sqlite3.connect("db.db")
cursor = conn.cursor()



opc = -1

createTables(conn, cursor)

def menu():
    print("____________________________________________________________")
    print("__________________________Menú______________________________")
    print("____________________________________________________________")
    print("1: Alta de infraccionado")
    print("2: Alta de infacciones")
    print("3: Alta de policia")
    print("4: Registro de multas")
    print("0. Salir")     

while (opc != 0):
    menu()
    opc = int(input("Seleccione una opcion: "))
        
    if opc == 1:
        crearAltaInfraccionado(conn, cursor)
    elif opc == 2:
        crearInfraccion(conn, cursor)
    elif opc== 3:
        crearPolicia(conn, cursor)
    elif opc == 4:
        obtenerRegistroMultas(conn, cursor)
    elif opc == 0:
        print("Hasta luego")
    else:
        print("Opcion inválida, por favor vuelve a ejecutar el programa")
    
conn.close()