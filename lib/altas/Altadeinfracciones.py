def crearInfraccion(conexion, cursor):
    Tipo_Infraccion = input("Ingrese el tipo de infraccion: ")
    Monto = float(input("Ingrese el monto: "))

    cursor.execute("""
                    INSERT INTO Infraccion (Tipo_Infraccion, Monto)
                    VALUES (?, ?) """,
                    (Tipo_Infraccion, Monto))

    conexion.commit()

    print("Infraccion agregada con exito.")


