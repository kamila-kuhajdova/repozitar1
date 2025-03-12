import random, tkinter

def hod8():
    n = random.randint(1, 6)
    print('Na kocke8 padla', 2 * n)

def hod9():
    n = random.randint(1, 6)
    print('Na kocke9 padla', 2 * n - 1)

def hod10():
    n = random.randint(1, 6)
    print('Na kocke10 padla', n ** 2)

def predpoved():
    print("Dnes bude", random.randint(-15, 35),"stupňov.")

def pin():
    a = random.randint(0, 9)
    b = random.randint(0, 9)
    c = random.randint(0, 9)
    d = random.randint(0, 9)
    print("Tvoj nový PIN je", a, b, c, d)

canvas = tkinter.Canvas()
canvas.pack()

def nahodny_stvorcek():
    x = random.randint(100, 200)
    y = random.randint(10, 200)
    n = random.randint(20, 60)
    canvas.create_rectangle(x, y, x + n, y + n, fill='orange')

nahodny_stvorcek()
nahodny_stvorcek()

nahodny_stvorcek()

nahodny_stvorcek()

hod8()
hod9()
hod10()
hod10()
hod10()
predpoved()
pin()
