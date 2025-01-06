# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 15:54:33 2025

@author: hanspetter
"""

import numpy as np
v_grad = float(input('Skriv inn gradtallet:' ))
desimaler = int(input('Hvor mange desimaler ønsker du i svaret?'))
v_rad = round(v_grad*np.pi/180 , desimaler)
print(f"{v_grad} grader tilsvarer {v_rad} radianer")
