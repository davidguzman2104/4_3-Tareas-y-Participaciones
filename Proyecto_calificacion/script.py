import sqlite3
# Conectar o crear la base de datos "db_alumno"
conn = sqlite3.connect('db_alumno.db')
cursor = conn.cursor()
# Crear la tabla "calificacion"
cursor.execute('''
CREATE TABLE IF NOT EXISTS calificacion (
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 nombre TEXT NOT NULL,
 correo_electronico TEXT NOT NULL,
 calificacion1 REAL NOT NULL,
 calificacion2 REAL NOT NULL,
 calificacion3 REAL NOT NULL,
 promedio REAL NOT NULL
)
''')
conn.commit()
conn.close()
