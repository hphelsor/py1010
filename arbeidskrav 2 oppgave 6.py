# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 21:23:44 2025

@author: hanspetter
"""

import matplotlib.pyplot as plt
import numpy as np

print("--------------------------------------------------------------")
print("|||||    Programmet plotter funksjonen y = - x**n - a    |||||")
print("--------------------------------------------------------------\n")

while True:
    power = int(input("Hva er potensverdien n? "))
    constant = int(input("Hva er konstantverdien a? "))
    lower = int(input("Hva er minste verdi for x? "))
    upper = int(input("Hva er største verdi for x? "))
    
    if lower < 0:
        points = (upper+abs(lower))*10
    else:
        points = (upper-lower)*10
    x = np.linspace(lower, upper, points)
    y = - x**power - constant
    
    fig, ax = plt.subplots()
    ax.plot(x, y)
    plt.axhline(0, color='black', linewidth=.5)
    plt.show()
    input("Trykk enter for ny beregning. Ctrl+C for å avslutte.")