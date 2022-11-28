from tkinter import * # librería

raiz =Tk()

raiz.title("Ventana de prueba")

#Cambio de icono  ( conversor.icon)
# raiz.iconbimap ("gato.ico")

raiz.resizable(0,0) # inhabilita redimensionar la ventana
# cambiar tamaño de ventana
raiz.config(bg="pink")
raiz.geometry("350x350") # 

raiz.title("Aplicación gráfica en Phyton")
etiqueta=Label(raiz,text="Hola mundo con python")

boton=Button(raiz,text="OK")

etiqueta.pack()

boton.pack()

raiz.mainloop()
