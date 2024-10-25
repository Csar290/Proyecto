import os
import tkinter as tki
from tkinter import messagebox
from dotenv import load_dotenv
import psycopg2
import requests

def obtener_ubicacion():
    response = requests.get("http://ip-api.com/json/")
    data = response.json()
    return data['lat'], data['lon']

def main():
    latitud,longitud = obtener_ubicacion()
    nombres = inputNombres.get()
    apellidos = inputApellidos.get()
    accion = inputAccion.get()

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
        messagebox.showinfo("Asistencia","Te has registrado correctamente")
        inputNombres.delete(0, tki.END)
        inputApellidos.delete(0, tki.END)
        inputAccion.delete(0, tki.END)

    except (Exception, psycopg2.Error) as error:
        messagebox.showerror("Asistencia", f"No se ha podido registrar correctamente: {error}")

    finally:
        if conection:
            cursor.close()
            conection.close()
            print("Coneccion de PostgresSQL cerrada")


ventana = tki.Tk()
ventana.title("Asistencia")

textoNombres = tki.Label(ventana, text="Ingrese sus nombres:")
textoNombres.pack()
inputNombres = tki.Entry(ventana)
inputNombres.pack()

textoApellidos = tki.Label(ventana, text="Ingreses sus apellios:")
textoApellidos.pack()
inputApellidos = tki.Entry(ventana)
inputApellidos.pack()

textoAccion = tki.Label(ventana, text="Accion (Ingreso/Salida):")
textoAccion.pack()
inputAccion = tki.Entry(ventana)
inputAccion.pack()

botonRegistro = tki.Button(ventana, text="Registrar", command=main)
botonRegistro.pack()

ventana.mainloop()