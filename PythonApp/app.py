import os
from dotenv import load_dotenv
import psycopg2
import requests

def obtener_ubicacion():
    response = requests.get("http://ip-api.com/json/")
    data = response.json()
    return data['lat'], data['lon']

def main():
    latitud,longitud = obtener_ubicacion()
    nombres = input("Ingrese su nombre: ")
    apellidos = input("Ingrese su apellido: ")
    accion = input("Accion(Ingreso o Salida): ")

    load_dotenv()
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')
    host = os.getenv('DB_HOST')
    port = os.getenv('DB_PORT')
    database = os.getenv('DB_NAME')


    try:
        conection = psycopg2.connect(
            user=user,
            password=password,
            host=host,
            port=port,
            database=database
    )

        cursor = conection.cursor()
        query = f"insert into Asistencia (nombres, apellidos, latitud, longitud, accion) values (%s, %s, %s, %s, %s)"
        values = (nombres, apellidos, latitud, longitud, accion)
        cursor.execute(query, values)
        conection.commit()

    except (Exception, psycopg2.Error) as error:
        print(f"Error al conectar con PostgreSQL: {error}")

    finally:
        if conection:
            cursor.close()
            conection.close()
            print("Coneccion de PostgresSQL cerrada")

if __name__ == "__main__":
    main()