import sqlite3

conexion = sqlite3.connect("Infracciones.db")
cursor = conexion.cursor()

Tipo_Infraccion = input("Ingrese el tipo de infraccion: ")
Monto = float(input("Ingrese el monto: "))

cursor.execute("""
                   INSERT INTO Infraccion (Tipo_Infraccion, Monto)
                   VALUES (?, ?) """,
                   (Tipo_Infraccion, Monto))

conexion.commit()
conexion.close()

print("Infraccion agregada con exito.")


