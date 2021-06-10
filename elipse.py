from turtle import *
from random import randrange
barvy = ["red", "yellow", "cyan", "DarkOrange", "DeepPink", "DarkGreen", "chartreuse", "gold", "green", "pink", "OliveDrab", "orchid", "purple", "coral", "Tomato", "YellowGreen", "Indigo", "Brown", "MediumVioletRed", "Navy", "HotPink", "SkyBlue", "MidnightBlue", "DarkBlue", "DarkKhaki", "GreenYellow", "DarkSeaGreen", "Lavender", "RoyalBlue", "DarkViolet", "DarkRed"]
cislo = 0
stupne = 0
kolikrat = 0
while True:
    for i in range(4):
        forward(200)
        left(90)
    pencolor(barvy[cislo])
    left(1)
    cislo = cislo + 1
    if cislo == 30:
        cislo = 0
    kolikrat = kolikrat+1
    print(kolikrat)
