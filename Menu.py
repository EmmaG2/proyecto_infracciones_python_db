
import sqlite3
import os
conn = sqlite3.connect('db.db')
cursor = conn.cursor()

def menu():
    print("____________________________________________________________")
    print("__________________________Menú______________________________")
    print("____________________________________________________________")
    print("1: Alta de infraccionado")
    print("2: Alta de infacciones")
    print("3: Alta de policia")
    print("4: Registro de multas")
    print("0. Salir")     

if __name__ == "__main__":
    while True:
        menu()
        opcion = input("Seleccione una opcion: ")
    
        if opcion == "1":
            import Altadeinfraccionado 
           
        elif opcion == "2":
            import Altadeinfracciones
            
        elif opcion == "3":
            import Altadepolicia
            
        elif opcion == "4":
            import Registrodemultas
            
        elif opcion == "5":
            break
        else:
            print("Opcion no valida. Por favor seleccione una opcion valida")

# Obten el directorio actual
directorio_actual = os.getcwd()

# Lista de archivos que deberían estar en el mismo directorio
archivos_necesarios = ['altadeinfaccionado.py', 'Altadeinfracciones.py', 'Altadepolicia.py', 'Registrodemultas.py']

# Verifica si cada archivo necesario está en el directorio actual
archivos_faltantes = [archivo for archivo in archivos_necesarios if not os.path.isfile(os.path.join(directorio_actual, archivo))]

if archivos_faltantes:
    print(f"Error: Los siguientes archivos no están en el mismo directorio: {', '.join(archivos_faltantes)}")
else:
    print("Todos los archivos necesarios están en el mismo directorio.")
