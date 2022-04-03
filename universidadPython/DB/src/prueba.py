import psycopg2

conexion = psycopg2.connect(
    user = 'postgres',
    password = 'admin',
    host = 'localhost',
    port = '5432',
    database = 'test_db'
)


cursor = conexion.cursor()
setencia = 'SELECT * FROM persona'
cursor.execute(setencia)

# Solicitar todos los registros
registros = cursor.fetchall()
print(registros)

cursor.close()
conexion.close()