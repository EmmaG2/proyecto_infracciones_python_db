import sqlite3

def crearPolicia(conexion, cursor):
    print("Ejecutando Alta de Policia")

    Codigo_Policia = input("Ingrese el codigo del policia: ")
    Nombre = input("Ingrese el nombre del policia: ")

    cursor.execute("""
                    INSERT INTO Policia (Codigo_Policia, Nombre) 
                    VALUES (?, ?) """,
                    (Codigo_Policia, Nombre))
    conexion.commit()

    print("Policia agregado con exito.")


