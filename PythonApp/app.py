import psycopg2

try:
    coneccion = psycopg2.connect(
        user="postgres",
        password="cesarPSQL",
        host="localhost",
        port="5432",
        database="DBApp"
    )

    cursor = coneccion.cursor()
except (Exception, psycopg2.Error) as error:
    print(f"Error al conectar con PostgreSQL: {error}")

finally:
    if coneccion:
        cursor.close()
        coneccion.close()
        print("Coneccion de PostgresSQL cerrada")