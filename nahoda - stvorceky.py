import tkinter
import random

canvas = tkinter.Canvas()
canvas.pack()

def nahodny_stvorcek():
    x = random.randint(10, 300)
    y = random.randint(10, 200)
    v = random.randint(10, 100)
    canvas.create_rectangle(x, y, x + v, y + v, fill = "green")

def nahodny_obdlznik():
    x = random.randint(10, 300)
    y = random.randint(10, 200)
    #v = random.randint(10, 100)
    canvas.create_rectangle(x, y, x + random.randint(10, 100), y + random.randint(10, 100), fill='orange')

nahodny_stvorcek()
nahodny_obdlznik()
nahodny_stvorcek()
nahodny_stvorcek()
nahodny_stvorcek()
nahodny_stvorcek()
