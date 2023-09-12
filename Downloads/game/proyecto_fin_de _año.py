import tkinter as tk
from tkinter import *
from PIL import Image,ImageTk
       
vent= tk.Tk()
vent = vent
vent.title("MundiPreguntas")
vent.geometry("500x500")

#Fondo de imagen y el inicio = Jugar o Salir

imagen = PhotoImage(file="img/xa.png")
fondo = Label(vent,image= imagen).place (x=0, y=0)
boton = tk.Button(vent, text="JUGAR", height= 4, width= 30)
boton.place(x=500, y= 390)
boton2 = tk.Button(vent, text="SALIR ", height= 4, width= 30)
boton2.place(x=500, y= 500)

#imagenes para jugar 
imagenJ = PhotoImage(file="img/rappi.png")
labelimg = Label(vent, image= imagenJ).place (x=130, y=100)
imagenJ2 = PhotoImage(file="img/brainl.png")
labelimg = Label(vent, image= imagenJ2).place (x=830, y=100)

#para mostrar las imagenes en la ventana 
def imagenes():
    apli1 = Image.open("Drive.png")
    new_apli1 = apli1.rezise((250,300))
    render = ImageTk.PhotoImage(new_apli1)
    img1= Label(vent, Image = render)
    img1.image = render
    img1.place(x=10, y=30)


#botones para poner si A. o B. la verdadera
boton = tk.Button(vent, text="A.", height= 4, width= 30)
boton.place(x=150, y= 300)


boton3 = tk.Button(vent, text="B.", height= 4, width= 30)
boton3.place(x=850, y= 300)


vent.mainloop()
