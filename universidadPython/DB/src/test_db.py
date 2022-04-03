import psycopg2

try:
    connection=psycopg2.connect(
        user='postgres',
        password="admin",
        host='localhost',
        database='test_db',
    )
    
    print('exito')
    cursor=connection.cursor()
    cursor.execute("SELECT version()")
    row=cursor.fetchone()
    print(row)
    cursor.execute("SELECT * from persona")
    rows=cursor.fetchall()
    for row in rows:
        print(row)
except Exception as ex:
    print(ex)
