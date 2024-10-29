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
    accionIS = AccionSeleccionada.get()
    nombres = inputNombres.get()
    apellidos = inputApellidos.get()

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
        values = (nombres, apellidos, latitud, longitud, accionIS)
        cursor.execute(query, values)
        conection.commit()
        messagebox.showinfo("Asistencia","Te has registrado correctamente")
        inputNombres.delete(0, tki.END)
        inputApellidos.delete(0, tki.END)
        AccionSeleccionada.set(None)

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

textoApellidos = tki.Label(ventana, text="Ingrese sus apellios:")
textoApellidos.pack()
inputApellidos = tki.Entry(ventana)
inputApellidos.pack()

textoAccionRB = tki.Label(ventana, text="Accion")
textoAccionRB.pack()
AccionSeleccionada = tki.StringVar()
AccionSeleccionada.set(None)

acciones = ["Ingreso", "Salida"]
for accion in acciones:
    RBotonAccion = tki.Radiobutton(ventana, text=accion, variable=AccionSeleccionada, value=accion)
    RBotonAccion.pack()

botonRegistro = tki.Button(ventana, text="Registrar", command=main)
botonRegistro.pack()

ventana.mainloop()