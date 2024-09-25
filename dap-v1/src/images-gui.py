import tkinter
from tkinter import *
from PIL import Image, ImageTk

frm = Tk()

frm.title("RPA Python")
frm.geometry("900x750")

pathImgFondo = Image.open(r"dap-v1\img\programming_python_1.jpg")
img = ImageTk.PhotoImage(pathImgFondo)

lblFondo = tkinter.Label(image=img)
lblFondo.place(x=0, y=0)

Label(frm, text="Imagen hecha por IA.", font=("Arial", 20)).pack(side=TOP)

pathImgBtn = ImageTk.PhotoImage(Image.open(r"dap-v1\img\btnSalir.jpg"))

btnImg = Button(image=pathImgBtn, command=frm.destroy).pack(side=LEFT)

frm.mainloop()