import sqlite3
from datetime import datetime

def obtenerRegistroMultas(conexion, cursor):
    fecha = datetime.now()

    print("Ejecutando Registro de infracciones")

    #Codigo_Multa = int(input("Ingrese el codigo de la multa: "))
    Codigo_Infraccion = int(input("Ingrese el codigo de la infraccion: "))
    Codigo_Infraccionado = int(input("Ingrese el codigo del infraccionado: "))
    Codigo_Policia = input("Ingrese el codigo del policia: ")
    Dia_Infraccion = fecha.strftime("%d/%m/%y")
    Hora_Infraccion = fecha.strftime("%H:%M")

    cursor.execute("""
                    INSERT INTO Multas (Codigo_Infraccion, Codigo_Infraccionado, Codigo_Policia, Dia_Infraccion, Hora_Infraccion)
                    VALUES (?, ?, ?, ?, ?) """,
                    (Codigo_Infraccion , Codigo_Infraccionado, Codigo_Policia, Dia_Infraccion, Hora_Infraccion))


    #Regresar el valor de la infraccion
    conexion.commit()


    cursor.execute("SELECT Monto FROM Infraccion WHERE codigo_infraccion =?", (Codigo_Infraccion,))
    monto_infraccion = cursor.fetchone()[0]
    print("Multa Agregada Correctamente")

    print(("El monto a pagar es:"))
    print(monto_infraccion)

    conexion.commit()

    print("Regresando a menu principal --------")
