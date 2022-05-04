import tkinter as tk
from math import pi

first = tk.Tk()
tk.Label(first, text="h(km):").grid(row=0, column=2)
h = tk.DoubleVar()
v2 = tk.Entry(first, textvariable=h)

v2.grid(row=0, column=3)
V = tk.StringVar()
T = tk.StringVar()
geo = tk.StringVar()
mars_geo = tk.StringVar()
V.set('Result will be here')


def calc_value():
    H = h.get() * 1000
    g = 9.8
    Rz = 6371 * 1000
    R = Rz + H
    V.set(f'V = {round(((R * g) ** 0.5), 2)} m/s')
    T.set(f'T = {round(2 * pi * (R / g) ** 0.5, 2)}')

    t = 24 * 3600
    t_m = 88642
    Rm = 3389.5 * 1000
    gm = 3.721
    geo_R = (t * Rz * g ** 0.5 / (2 * pi)) ** (2 / 3)
    geo.set(f'h(Earth) = {round(geo_R - Rz, 2)} meters')

    mars_R = (t_m * Rm * gm ** 0.5 / (2 * pi)) ** (2 / 3)
    mars_geo.set(f'h(Mars) = {round(mars_R - Rm, 2)} meters')


r1 = tk.Label(first, textvariable=V)
r2 = tk.Label(first, textvariable=T)
r3 = tk.Label(first, textvariable=geo)
r4 = tk.Label(first, textvariable=mars_geo)

r1.grid(row=2, column=1)
r2.grid(row=3, column=1)
r3.grid(row=4, column=1)
r4.grid(row=5, column=1)

b1 = tk.Button(first, text="Submit", command=calc_value)
b1.grid(row=2, column=0)
first.mainloop()
