import psycopg2

conexion = psycopg2.connect(
    user='postgres',
    password='admin',
    host='localhost',
    database='test_db')

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
            valores = ('Carlos', 'Lara', 'clara@mail.com')
            cursor.execute(sentencia,valores)
            # conexion.commit()
            registros_insertados = cursor.rowcount
            print(f'registros insertados: {registros_insertados}')
except Exception as e:
    print(f'Ocurrió un error: {e}')
finally:
    conexion.close()





# cursor = conexion.cursor()
# setencia = 'SELECT * FROM persona'
# cursor.execute(setencia)

# # Solicitar todos los registros
# registros = cursor.fetchall()
# print(registros)

# cursor.close()
# conexion.close()
