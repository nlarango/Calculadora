from tkinter import *
from tkinter import ttk


def sumar():
    x=int(input('Escriba un numero:'))
    y=int(input('Escriba un numero:'))
    print(x+y)

def imprimir():
    print('Buenos dias')


# Tk es mi clase, main es un obejto. Al guardarlo así, estoy haciendo
# una instanciacion de la clase

# Esto me crea una interfaz grafica sencilla
main = Tk()
# Defino el tamaño de la ventana
main.geometry('500x400')
main.title('La calculadora de Franz')
# Aqui estoy creando un boton, eso se hace con ttk
ttk.Label(main, text='calculadora').pack(side=TOP)
pantalla=ttk.Entry(main).pack(side=TOP)

# TAREA: HACER LOS BOTONES DE LOS NUMEROS, PONER LA MISMA FUNCION
# A TODOS.


ttk.Button(main, text='Salida',command=quit).pack(side=BOTTOM)
ttk.Button(main, text='Sumar',command=sumar).pack(side=TOP)
ttk.Button(main, text='Print',command=imprimir).pack(side=TOP)
main.mainloop()
