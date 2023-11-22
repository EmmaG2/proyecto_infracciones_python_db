def ejecutar_altadeinfraccionado(cursor, conn):
    #Codigo_Infraccionado = int(input("Ingrese el codigo del infraccionado: "))
    Nombre_Infraccionado = input("Ingrese el nombre del infraccionado: ")
    Edad = int(input("Ingrese la edad del infraccionado: "))
    Placa_vehicular = input("Ingrese la placa vehicular del infraccionado: ")
    Tipo_Infraccion = input("Ingrese el tipo de infraccion: ")
    Dia_Infraccion = input("Ingrese la fecha de la infraccion: ")
    Hora_Infraccion = input("Ingrese la hora de la infraccion: ")
    Codigo_Policia = input("Ingrese el codigo del policia: ")


    cursor.execute("""
                    INSERT INTO Infraccionado (Nombre_Infraccionado,Edad, Placa_vehicular, Tipo_Infraccion, Dia_Infraccion, Hora_Infraccion,Codigo_Policia)
                    VALUES (?, ?, ?, ?, ?, ?, ?) """,
                    (Nombre_Infraccionado, Edad, Placa_vehicular,Tipo_Infraccion, Dia_Infraccion, Hora_Infraccion, Codigo_Policia))

    conn.commit()
    conn.close()


