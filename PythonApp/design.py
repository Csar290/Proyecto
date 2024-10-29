import tkinter as tki
from tkinter import messagebox
import location
import database

def main():
    nombres = inputNombres.get()
    apellidos = inputApellidos.get()
    accionIS = AccionSeleccionada.get()
    latitud, longitud = location.obtener_ubicacion()

    if latitud is None or longitud is None:
        messagebox.showerror("Error", "No se pudo obtener la ubicación.")
        return
    if database.add_record(nombres, apellidos, latitud, longitud, accionIS):
        messagebox.showinfo("Asistencia", "Te has registrado correctamente")
        inputNombres.delete(0, tki.END)
        inputApellidos.delete(0, tki.END)
        AccionSeleccionada.set(None)
    else:
        messagebox.showerror("Asistencia", "No se ha podido registrar correctamente")


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