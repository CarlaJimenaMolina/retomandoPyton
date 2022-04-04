from tkinter import *
from tkinter import ttk

ventana = Tk()
ventana.title("Programa 2")
ventana.config(bg="bisque2")
ventana.geometry("1100x700")

# IMAGEN

imagen = PhotoImage (file="imagen1.png")
fondo = Label(ventana,image=imagen)
fondo.place(x=0,y=0)

# TITULO

titulo = Label( ventana, text = "Sistema", bg="bisque2", fg="#112731", font=("calibri",45))
titulo.place(x=80,y=25)

# CONTENEDOR 1

contenedor1 = Frame(ventana)
contenedor1.config(width=250,height=500, bg="linen")
contenedor1.place(x=50,y=150)


# CONTENEDOR 2

contenedor2 = Frame(ventana)
contenedor2.config(width=700,height=500,bg="peachpuff2")
contenedor2.place(x=350,y=150)


registro= Label(contenedor2, text="Registro",bg="peachpuff2", font=("calibri",23))
registro.place(x=300,y=30)

nombre = Label(contenedor2, text="Nombre y apellido",bg="peachpuff2", font=("calibri",23))
nombre.place(x=30,y=110)

enombre=Entry(contenedor2,width=18,font=("calibri",23))
enombre.place(x=390,y=110)

edad=Label(contenedor2, text="Edad",bg="peachpuff2", font=("calibri",23))
edad.place(x=30,y=190)

eedad=Entry(contenedor2,width=18,font=("calibri",23))
eedad.place(x=390,y=190)

dni=Label(contenedor2, text="DNI",bg="peachpuff2", font=("calibri",23))
dni.place(x=30,y=270)

edni=Entry(contenedor2,width=18,font=("calibri",23))
edni.place(x=390,y=270)

provincia=Label(contenedor2, text="Provincia de residencia",bg="peachpuff2", font=("calibri",23))
provincia.place(x=30,y=350)

enviar=Button(contenedor2, text="Enviar", font=("calibri",23))
enviar.place(x=515,y=430)

lista =["Mendoza","San Juan","San Luis", "Neuquen"]
combo= ttk.Combobox(contenedor2,width=17,font=("calibri",23))
combo.place(x=390,y=350)
combo["values"]=lista


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
    contenedor2.place(x=350,y=150)
    contenedor3.place_forget()
    contenedor4.place_forget()

def fboton2():
    contenedor3.place(x=350,y=150)
    contenedor2.place_forget()
    contenedor4.place_forget()

def fboton3():
    contenedor4.place(x=350,y=150)
    contenedor2.place_forget()
    contenedor3.place_forget()

# BOTONES

boton1=Button(contenedor1, text="Registro", width=10,height=2, bg="floral white", font=("calibri", 20), command=fboton1)
boton1.place(x=50,y=50)

boton2=Button(contenedor1, text="Contactanos", width=10,height=2, bg="floral white", font=("calibri", 20), command=fboton2)
boton2.place(x=50,y=200)

boton3=Button(contenedor1, text="Boton 3", width=10,height=2, bg="floral white", font=("calibri", 20), command=fboton3)
boton3.place(x=50,y=350)






ventana.mainloop()
