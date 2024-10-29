import os
from dotenv import load_dotenv
import psycopg2

#Cargar .env
load_dotenv()

def connection():
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')
    host = os.getenv('DB_HOST')
    port = os.getenv('DB_PORT')
    database = os.getenv('DB_NAME')
    return psycopg2.connect(
        user=user,
        password=password,
        host=host,
        port=port,
        database=database
    )

def add_record(nombres, apellidos, latitud, longitud, accionIS):
    try:
        conect = connection()
        cursor = conect.cursor()
        query = f"insert into Asistencia (nombres, apellidos, latitud, longitud, accion) values (%s, %s, %s, %s, %s)"
        values = (nombres, apellidos, latitud, longitud, accionIS)
        cursor.execute(query, values)
        conect.commit()
        return True
    except (Exception, psycopg2.Error) as error:
        print("Error al registrar asistencia:", error)
        return False
    finally:
        if conect:
            cursor.close()
            conect.close()
            print("Coneccion de PostgresSQL cerrada")