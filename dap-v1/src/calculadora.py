from tkinter import *

frm = Tk()
frm.title("Calculadora")

def enviarNumeroPara(char):
    global calculoOperaciones
    calculoOperaciones += str(char)
    valoresDeEntrada.set(calculoOperaciones)

def deleteNumbero():
    global calculoOperaciones
    eliminarUltimoNumero = calculoOperaciones[:-1]
    calculoOperaciones = eliminarUltimoNumero
    valoresDeEntrada.set(calculoOperaciones)
    
def LimpiarTodo():
    global calculoOperaciones
    calculoOperaciones = ""
    valoresDeEntrada.set(calculoOperaciones)

def funcionIgual():
    global calculoOperaciones
    resultadoCalculo = str(eval(calculoOperaciones))
    valoresDeEntrada.set(resultadoCalculo)
    calculoOperaciones = resultadoCalculo
    
calculoOperaciones = ""
valoresDeEntrada = StringVar()

txtResultado = Entry(frm, font=("Arial 20 bold"), 
                     textvariable=valoresDeEntrada,
                     border=5, bg="#BBB", fg="black"
                     ).grid(row=1, columnspan=5, padx=10, pady=15)


btnNumbero7 = Button(frm, text="7", font=("Arial 16 bold"),
                    border=5, bg="#BBB", fg="black",
                    command=lambda: enviarNumeroPara("7")).grid(row=2, column=0, sticky="nsew")

btnNumbero8 = Button(frm, text="8", font=("Arial 16 bold"),
                    border=5, bg="#BBB", fg="black",
                    command=lambda: enviarNumeroPara("8")).grid(row=2, column=1, sticky="nsew")

btnNumbero9 = Button(frm, text="9", font=("Arial 16 bold"),
                    border=5, bg="#BBB", fg="black",
                    command=lambda: enviarNumeroPara("9")).grid(row=2, column=2, sticky="nsew")

btnEliminar = Button(frm, text="DEL", font=("Arial 16 bold"),
                    border=5, bg="#DB701F", fg="#000",
                    command=deleteNumbero).grid(row=2, column=3, sticky="nsew")

btnEliminarTodo = Button(frm, text="AC", font=("Arial 16 bold"),
                    border=5, bg="#DB701F", fg="#000",
                    command=LimpiarTodo).grid(row=2, column=4, sticky="nsew")

btnNumbero4 = Button(frm, text="4", font=("Arial 16 bold"),
                    border=5, bg="#BBB", fg="black",
                    command=lambda: enviarNumeroPara("4")).grid(row=3, column=0, sticky="nsew")

btnNumbero5 = Button(frm, text="5", font=("Arial 16 bold"),
                    border=5, bg="#BBB", fg="black",
                    command=lambda: enviarNumeroPara("5")).grid(row=3, column=1, sticky="nsew")

btnNumbero6 = Button(frm, text="6", font=("Arial 16 bold"),
                    border=5, bg="#BBB", fg="black",
                    command=lambda: enviarNumeroPara("6")).grid(row=3, column=2, sticky="nsew")

btnMultiplicacion = Button(frm, text="*", font=("Arial 16 bold"),
                    border=5, bg="#BBB", fg="black",
                    command=lambda: enviarNumeroPara("*")).grid(row=3, column=3, sticky="nsew")

btnDivision = Button(frm, text="/", font=("Arial 16 bold"),
                    border=5, bg="#BBB", fg="black",
                    command=lambda: enviarNumeroPara("/")).grid(row=3, column=4, sticky="nsew")

btnNumbero1 = Button(frm, text="1", font=("Arial 16 bold"),
                    border=5, bg="#BBB", fg="black",
                    command=lambda: enviarNumeroPara("1")).grid(row=4, column=0, sticky="nsew")

btnNumbero2 = Button(frm, text="2", font=("Arial 16 bold"),
                    border=5, bg="#BBB", fg="black",
                    command=lambda: enviarNumeroPara("2")).grid(row=4, column=1, sticky="nsew")

btnNumbero3 = Button(frm, text="3", font=("Arial 16 bold"),
                    border=5, bg="#BBB", fg="black",
                    command=lambda: enviarNumeroPara("3")).grid(row=4, column=2, sticky="nsew")

btnSuma = Button(frm, text="+", font=("Arial 16 bold"),
                    border=5, bg="#BBB", fg="black",
                    command=lambda: enviarNumeroPara("+")).grid(row=4, column=3, sticky="nsew")

btnResta = Button(frm, text="-", font=("Arial 16 bold"),
                    border=5, bg="#BBB", fg="black",
                    command=lambda: enviarNumeroPara("-")).grid(row=4, column=4, sticky="nsew")

btnNumbero0 = Button(frm, text="0", font=("Arial 16 bold"),
                    border=5, bg="#BBB", fg="black",
                    command=lambda: enviarNumeroPara("0")).grid(row=5, column=0, sticky="nsew")

btnPunto = Button(frm, text=".", font=("Arial 16 bold"),
                    border=5, bg="#BBB", fg="black",
                    command=lambda: enviarNumeroPara(".")).grid(row=5, column=1, sticky="nsew")

btnIgual = Button(frm, text="=", font=("Arial 16 bold"),
                    border=5, bg="#BBB", fg="black",
                    command=funcionIgual).grid(row=5, column=2, columnspan=3, sticky="nsew")


frm.mainloop()
