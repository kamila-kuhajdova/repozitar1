import tkinter, random

sirka_c = 800
vyska_c = 500

canvas = tkinter.Canvas(width = sirka_c, height = vyska_c)
canvas.pack()

"""
podprogram, ktorý na pozíciu x, y vypíše 2 texty (fonty, veľkosti, farba)
podprogram, ktorý nakreslí náhodne dlhú žížalku na pozíciu x, y
"""
def napis_text():
    
    canvas.create_text(x, y, text='farebná dážďovka', font = "Times 50", fill = "purple")
    canvas.create_text(x, y + 100, text="Ahoj!", font='arial 30', fill = "blue")

def zizala():

    v1 = random.randint(10, 100)    #náhodná dĺžka pre 3 časti
    v2 = random.randint(10, 60)
    v3 = random.randint(10, 100)
    
    vyska = 20  #výška žížaly

    zx = x
    zy = y
    
    canvas.create_rectangle(zx, zy, zx + v1, zy + vyska, fill = "pink")
    zx = zx + v1
    canvas.create_rectangle(zx, zy - 5, zx + v2, zy + 5 + vyska, fill = "purple")
    zx = zx + v2
    canvas.create_rectangle(zx, zy, zx + v3, zy + vyska, fill = "pink")

#nastavenie x, y pre text a výpis textu
x = sirka_c / 2
y = 50
napis_text()

#10x nastavenie x, y pre žížalku a nakreslenie žížaly
for i in range(10):
    x = random.randint(50, sirka_c - 200)
    y = random.randint(200, vyska_c - 20)    
    zizala()                       
