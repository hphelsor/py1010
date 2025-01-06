# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 19:42:54 2025

@author: hanspetter
"""

import numpy as np

def tegning():
    print("\n\n                 ..")
    print("              .      .")
    print("             .        .")
    print("            .     a    .")
    print("           ..............")
    print("           .__|        .")
    print("           .          .")
    print("           .         .")
    print("           .        .")
    print("           .       .")
    print("         b .      .")
    print("           .     .")
    print("           .    .")
    print("           .   .")
    print("           .  .")
    print("           . .")
    print("           . \n")
    
def linje():
    print("----------------------------------------------------------------------")

def sjekk_tall(variabel):
    if variabel.isnumeric() == False:
        global variabelfeil
        variabelfeil = True
    return

variabelfeil = False
desimaler = int(input("Hvor mange desimaler ønsker du å regne med? "))

while True:
    tegning()    
    variabelfeil = False
    diameter = input("Hva er sirkelens diameter? (a) ")
    lengde_b = input("Hva er trekantens side? (b) ")
    sjekk_tall(diameter)
    sjekk_tall(lengde_b)
    if variabelfeil == False:
        diameter = float(diameter)
        radius = diameter/2
        lengde_b = float(lengde_b)
        areal_halvsirkel = np.pi * radius**2 / 2
        areal_trekant = radius * lengde_b
        areal = areal_halvsirkel + areal_trekant
        print(f"\nArealet av halvsirkelen er {round(areal_halvsirkel, desimaler)}")
        print(f"Arealet av trekanten er {round(areal_trekant, desimaler)}")
        linje()
        print(f"Samlet areal er {round(areal, desimaler)}\n")
        omkrets_halvsirkel = np.pi*diameter
        lengde_ukjent = np.sqrt(lengde_b**2 + diameter**2)
        omkrets = omkrets_halvsirkel + lengde_b + lengde_ukjent
        print(f"Lengden av halvsirkelen er {round(omkrets_halvsirkel, desimaler)}")
        print(f"Lengden av siden b i trekanten er {round(lengde_b, desimaler)}")
        print(f"Lengden av den ukjente siden (motstående b) i trekanten er {round(lengde_ukjent, desimaler)}")
        linje()
        print(f"Samlet omkrets er {round(omkrets, desimaler)}\n\n")
    else:
        print("\nVennligst legg inn tallverdier for a og b\n")
    input("Trykk enter for ny beregning. Ctrl+C for å avslutte.")
        
        
        
    
