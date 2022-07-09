from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3

conexion = sqlite3.connect("dbgp.db")

ventana = Tk()
ventana.title("Programa 2")
ventana.config(bg="bisque2")
ventana.geometry("1100x700")

# IMAGEN

#imagen = PhotoImage (file="imagen1.png")
#fondo = Label(ventana,image=imagen)
#fondo.place(x=0,y=0)

# TITULO

titulo = Label( ventana, text = "Registro de pacientes", bg="bisque2", fg="#112731", font=("calibri",40))
titulo.place(x=80,y=17)

# CONTENEDOR 1

contenedor1 = Frame(ventana)
contenedor1.config(width=250,height=550, bg="linen")
contenedor1.place(x=50,y=100)


# CONTENEDOR 2

contenedor2 = Frame(ventana)
contenedor2.config(width=700,height=550,bg="peachpuff2")
contenedor2.place(x=350,y=100)


registro= Label(contenedor2, text="Registro",bg="peachpuff2", font=("calibri",20))
registro.place(x=250,y=10)

nombre = Label(contenedor2, text="Nombre y apellido",bg="peachpuff2", font=("calibri",18))
nombre.place(x=30,y=60)

enombre=Entry(contenedor2,width=31,font=("calibri",18))
enombre.place(x=300,y=60)

edad=Label(contenedor2, text="Edad",bg="peachpuff2", font=("calibri",18))
edad.place(x=30,y=110)

eedad=Entry(contenedor2,width=31,font=("calibri",18))
eedad.place(x=300,y=110)

dni=Label(contenedor2, text="DNI",bg="peachpuff2", font=("calibri",18))
dni.place(x=30,y=160)

edni=Entry(contenedor2,width=31,font=("calibri",18))
edni.place(x=300,y=160)

provincia=Label(contenedor2, text="Provincia de residencia",bg="peachpuff2", font=("calibri",18))
provincia.place(x=30,y=210)

lista =["Mendoza","San Juan","San Luis", "Neuquen"]
combo= ttk.Combobox(contenedor2,width=30,font=("calibri",18))
combo.place(x=300,y=210)
combo["values"]=lista

observaciones = Label(contenedor2, text="Observaciones:",bg="peachpuff2", font=("calibri",18))
observaciones.place(x=30,y=260)

eobservaciones = Entry(contenedor2,width=31,font=("calibri",18))
eobservaciones.place(x=30,y=310)

def guardar():
    print("guardando")
    datos = (enombre.get(),eedad.get(),edni.get(),eobservaciones.get())
    tabla = conexion.cursor()
    tabla.execute("INSERT INTO pacientes(nombre, edad, dni, observaciones) VALUES(?,?,?,?)", datos)
    conexion.commit()
    tabla.close()
    messagebox.showinfo("Registro de pacientes","Paciente guardado exitosamente.")
    

bGuardar=Button(contenedor2, text="Guardar", font=("calibri",16), command=guardar)
bGuardar.place(x=565,y=490)


# CONTENEDOR 3

contenedor3 = Frame(ventana)
contenedor3.config(width=700,height=500,bg="rosybrown2")
#contenedor3.place(x=350,y=150)

contactanos=Label(contenedor3, text="Contactanos", font=("calibri",23),bg="rosybrown2")
contactanos.place(x=100,y=50)

mail= Text(contenedor3, width=45, height=10,font=("calibri",18))
mail.place(x=100,y=100)

enviarmail= Button(contenedor3, text="Enviar Mail",font=("calibri",18))
enviarmail.place(x=520,y=410)

# CONTENEDOR 4

contenedor4 = Frame(ventana)
contenedor4.config(width=700,height=500,bg="lightpink2")
#contenedor4.place(x=350,y=150)

# FUNCIONES

def fboton1():
    contenedor2.place(x=350,y=100)
    contenedor3.place_forget()
    contenedor4.place_forget()

def fboton2():
    contenedor3.place(x=350,y=100)
    contenedor2.place_forget()
    contenedor4.place_forget()

def fboton3():
    contenedor4.place(x=350,y=100)
    contenedor2.place_forget()
    contenedor3.place_forget()

# BOTONES

boton1=Button(contenedor1, text="Registros", width=10,height=2, bg="floral white", font=("calibri", 20), command=fboton1)
boton1.place(x=50,y=50)

boton2=Button(contenedor1, text="Contactanos", width=10,height=2, bg="floral white", font=("calibri", 20), command=fboton2)
boton2.place(x=50,y=350)

boton3=Button(contenedor1, text="Buscar", width=10,height=2, bg="floral white", font=("calibri", 20), command=fboton3)
boton3.place(x=50,y=200)






ventana.mainloop()
