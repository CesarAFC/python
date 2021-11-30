import tkinter

ventana = tkinter.Tk()
ventana.title("Calculiadora")

i = 0

#Entrada de texto
EntradaDeTexto = tkinter.Entry(ventana, font = ("Calibri 20"))
EntradaDeTexto.grid(row = 0, column = 0, columnspan = 4, padx=5, pady=5)

#Funiones
def click_boton(valor):
    global i
    EntradaDeTexto.insert(i, valor)
    i += 1
    return 

def borrar():
    EntradaDeTexto.delete(-1)

def operacion():
    ecuacion = EntradaDeTexto.get()
    resultado = eval(ecuacion)
    EntradaDeTexto.delete(0, tkinter.END)
    EntradaDeTexto.insert(0, resultado)
    i = 0

#Botones numeros
boton = tkinter.Button(ventana, text = "1", width = 5, height=2, command = lambda: click_boton(1) )
boton1 = tkinter.Button(ventana, text = "2", width = 5, height=2, command = lambda: click_boton(2))
boton2 = tkinter.Button(ventana, text = "3", width = 5, height=2, command = lambda: click_boton(3))
boton3 = tkinter.Button(ventana, text = "4", width = 5, height=2, command = lambda: click_boton(4))
boton4 = tkinter.Button(ventana, text = "5", width = 5, height=2, command = lambda: click_boton(5))
boton5 = tkinter.Button(ventana, text = "6", width = 5, height=2, command = lambda: click_boton(6))
boton6 = tkinter.Button(ventana, text = "7", width = 5, height=2, command = lambda: click_boton(7))
boton7 = tkinter.Button(ventana, text = "8", width = 5, height=2, command = lambda: click_boton(8))
boton8 = tkinter.Button(ventana, text = "9", width = 5, height=2, command = lambda: click_boton(9))
boton9 = tkinter.Button(ventana, text = "0", width = 15, height=2, command = lambda: click_boton(0))

#Botones func
boton_borrar = tkinter.Button(ventana, text = "AC", width = 5, height=2, command = lambda: borrar())
boton_parentesis1 = tkinter.Button(ventana, text = "(", width = 5, height=2, command = lambda: click_boton("("))
boton_parentesis2 = tkinter.Button(ventana, text = ")", width = 5, height=2, command = lambda: click_boton(")"))
boton_punto = tkinter.Button(ventana, text = ".", width = 5, height=2, command = lambda: click_boton("."))

#botones operaciones
boton_div = tkinter.Button(ventana, text = "/", width = 5, height=2, command = lambda: click_boton("/"))
boton_suma = tkinter.Button(ventana, text = "+", width = 5, height=2, command = lambda: click_boton("+"))
boton_mult = tkinter.Button(ventana, text = "X", width = 5, height=2, command = lambda: click_boton("*"))
boton_resta = tkinter.Button(ventana, text = "-", width = 5, height=2, command = lambda: click_boton("-"))
boton_igual = tkinter.Button(ventana, text = "=", width = 5, height=2, command = lambda: operacion())

#grid's
boton_borrar.grid(row=1, column = 0, padx =5, pady=5)
boton_parentesis1.grid(row=1, column =1, padx =5, pady=5)
boton_parentesis2.grid(row=1, column =2 , padx =5, pady=5)
boton_div.grid(row=1, column =3 , padx =5, pady=5)

boton6.grid(row=2, column = 0, padx =5, pady=5)
boton7.grid(row=2, column =1, padx =5, pady=5)
boton8.grid(row=2, column =2 , padx =5, pady=5)
boton_mult.grid(row=2, column =3 , padx =5, pady=5)

boton3.grid(row=3, column = 0, padx =5, pady=5)
boton4.grid(row=3, column =1, padx =5, pady=5)
boton5.grid(row=3, column =2 , padx =5, pady=5)
boton_suma.grid(row=3, column =3 , padx =5, pady=5)

boton.grid(row=4, column = 0, padx =5, pady=5)
boton1.grid(row=4, column =1, padx =5, pady=5)
boton2.grid(row=4, column =2 , padx =5, pady=5)
boton_resta.grid(row=4, column =3 , padx =5, pady=5)

boton9.grid(row=5, column =0 , columnspan= 2, padx =5, pady=5)
boton_punto.grid(row=5, column =2 , padx =5, pady=5)
boton_igual.grid(row=5, column =3 , padx =5, pady=5)


ventana.mainloop()
