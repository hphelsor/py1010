# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

year_of_birth = int(input("Hvilket år ble du født? "))
age = int(2024 - year_of_birth)
print(f"Da fylte du {age} år i 2024, og blir {age+1} i 2025.")
if age % 10 == 0:
    print(f"Gratulerer med {age}-årsjubileet i 2024!")
if (age+1) % 10 == 0:
    print(f"Gratulerer med {age+1}-årsjubileet i 2025!")
if age < 67:
    print(f"Du blir pensjonist i {year_of_birth + 67}.")
else:
    print(f"Du ble pensjonist i {year_of_birth + 67}.")
print(f"Det er {age - 18} år siden du ble myndig.")
print(f"I år 2000 var du {2000 - year_of_birth} år gammel.\n")
print(f"{age} år tilsvarer {age*365} dager. Du har levd lenger enn det...")