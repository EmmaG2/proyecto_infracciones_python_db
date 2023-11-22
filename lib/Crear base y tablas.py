import sqlite3

conexion = sqlite3.connect("Infracciones.db")
cursor = conexion.cursor()

print("Se crea la tabla Infraccion")
cursor.execute("""
                   CREATE TABLE IF NOT EXISTS Infraccion (
                   Codigo_Infraccion integer primary key AUTOINCREMENT,
                   Tipo_Infraccion text,
                   Monto real
                   )
""")

print("Se crea la tabla Infraccionado")
cursor.execute("""
                   CREATE TABLE IF NOT EXISTS Infraccionado (
                   Codigo_Infraccionado integer primary key AUTOINCREMENT,
                   Nombre_Infraccionado text,
                   Edad char(2),
                   Placa_vehicular char(9),
                   Tipo_Infraccion text,
                   Dia_Infraccion date,
                   Hora_Infraccion time,
                   Codigo_Policia char(6),
                   FOREIGN KEY (Codigo_Policia) REFERENCES Policia(Codigo_Policia)
                   )
""")

print("Se crea la tabla Policia")
cursor.execute("""
                   CREATE TABLE IF NOT EXISTS Policia (
                   Codigo_Policia integer primary key AUTOINCREMENT,
                   Nombre text
                   )
""")

print("Se crea la tabla Multas")
cursor.execute("""
                  CREATE TABLE IF NOT EXISTS Multas (
                  Codigo_Multa integer primary key AUTOINCREMENT,
                  Codigo_Infraccion integer,
                  Codigo_Infraccionado integer,
                  Codigo_Policia char(6),
                  Dia_Infraccion date,
                  Hora_Infraccion time,
                  FOREIGN KEY (Codigo_Infraccion) REFERENCES Infraccion(Codigo_infraccion),
                  FOREIGN KEY (Codigo_Infraccionado) REFERENCES Infraccionado(Codigo_Infraccionado),
                  FOREIGN KEY (Codigo_Policia) REFERENCES Policia(Codigo_Policia)
                  )
""")
conexion.commit()
conexion.close
print("Base de datos y tablas creadas con exito.")
