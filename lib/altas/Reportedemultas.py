import sqlite3
from datetime import datetime


print("Ejecutando Reporte de infracciones")

conexion = sqlite3.connect("Infracciones.db")
cursor = conexion.cursor()


def menu():
    print("1: Reporte completo de multas realizadas")
    print("2: Multas por oficial")
    print("3: Total de dinero recaudado por fecha")

if __name__ == "__main__":
    while True:
        menu()
        opcion = input("Seleccione una opcion: ")
    
        if opcion == "1":
            fecha = input ("Ingrese fecha: ")
                        
            cursor.execute("SELECT * FROM Multas WHERE Dia_infraccion =?", (fecha,))
            infracciones = cursor.fetchall()
            print(infracciones)
        
            
        elif opcion == "5":
            break
        else:
            print("Opcion no valida. Por favor seleccione una opcion valida")
