import tkinter as tk
from math import pi

first = tk.Tk()
tk.Label(first, text="V:").grid(row=0, column=0)
tk.Label(first, text="M:").grid(row=0, column=2)
tk.Label(first, text="S:").grid(row=1, column=0)
tk.Label(first, text="Alpha:").grid(row=1, column=2)

V = tk.DoubleVar()
M = tk.DoubleVar()
S = tk.DoubleVar()
Alpha = tk.DoubleVar()

v1 = tk.Entry(first, textvariable=V)
v2 = tk.Entry(first, textvariable=M)
v3 = tk.Entry(first, textvariable=S)
v4 = tk.Entry(first, textvariable=Alpha)

v1.grid(row=0, column=1)
v2.grid(row=0, column=3)
v3.grid(row=1, column=1)
v4.grid(row=1, column=3)
res = tk.StringVar()
res.set('Result will be here')


def calc_value():
    v = V.get()
    m = M.get()
    s = S.get()
    alpha = Alpha.get() * pi / 180
    ro = 0.5
    g = 9.8

    if v == 0:
        res.set(f'V = {round((m * g / (2 * ro * s * alpha ** 2)) ** 0.5, 2)}')
    elif m == 0:
        res.set(f'M = {round(s * 2 * ro * v ** 2 * alpha ** 2 / g, 2)}')
    elif s == 0:
        res.set(f'S = {m * g / (2 * ro * v ** 2 * alpha ** 2)}')
    elif alpha == 0:
        res.set(f'Alpha = {round((m * g / (2 * ro * s * v ** 2)) ** 0.5, 2)}')
    else:
        res.set('Error: keep one value zero')
    print("ENTRANCE BTN")


r = tk.Label(first, textvariable=res)
r.grid(row=2, column=1)

b1 = tk.Button(first, text="Submit", command=calc_value)
b1.grid(row=2, column=0)
first.mainloop()

"""
v = 100
m = 1000
alpha = 2
--> S = 804.28
"""
