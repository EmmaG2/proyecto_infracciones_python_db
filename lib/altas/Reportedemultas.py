def getReporteDeMultas(conexion, cursor):
    print("Ejecutando Reporte de infracciones")

    opcion = -1

    def menu():
        print("1: Reporte completo de multas realizadas")
        print("2: Multas por oficial")
        print("3: Total de dinero recaudado por fecha")
        print("0: Salir")
        
    while opcion != 0:
        menu()
        opcion = int(input("Seleccione una opcion: "))
    
        if opcion == 1:
            fecha = input ("Ingrese fecha: ")
                        
            cursor.execute("SELECT * FROM Multas WHERE Dia_infraccion =?", (fecha,))
            infracciones = cursor.fetchall()
            print(infracciones)
        
            
        elif opcion == 5:
            break
        else:
            print("Opcion no valida. Por favor seleccione una opcion valida")
