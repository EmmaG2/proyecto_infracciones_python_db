def reset(cursor):
    for i in range(1, 100):
        # Insertar el usuario en la base de datos
        cursor.execute("""
                    INSERT INTO Infraccionado (Nombre_Infraccionado,Edad, Placa_vehicular, Tipo_Infraccion, Dia_Infraccion, Hora_Infraccion,Codigo_Policia)
                    VALUES (?, ?, ?, ?, ?, ?, ?) """,
                    ("", i, "","", "", "", ""))
    cursor.execute("DELETE FROM Infraccionado")
    
