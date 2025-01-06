# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 16:05:05 2025

@author: hanspetter

Programmet lar brukeren spørre om hovedstad og antall innbyggere i den for landene som ligger i en dictionary.
Dersom landet ikke ligger inne får han mulighet til å legge til informasjon om det.

"""
def stor_bokstav(renskrive): #Formaterer til første bokstav stor, resten små
    renskrive = renskrive.lower()
    renskrive = renskrive.capitalize()
    return(renskrive)

data = {
        "Norge": ["Oslo", 0.634],
        "England": ["London", 8.982],
        "Frankrike": ["Paris", 2.161],
        "Italia": ["Roma", 2.873]
        }
while True: #Lar brukeren spørre gjentatte ganger
    land_info = input("\nHvilket land vil du vite hovedstaden til?")
    land_info = stor_bokstav(land_info)

    fant_info = False #Setter en variabel som endres dersom landet finnes i lista
    
    #Looper gjennom og leter etter ønsket land og viser hovedstad og innbyggere dersom landet finnes i lista
    for land in data.keys():
        if land == land_info:
            print(f"Hovedstaden i {land} er {data[land][0]} med {data[land][1]} millioner innbyggere")
            fant_info = True 
            
    #Hvis landet ikke finnes i lista kan brukeren velge å legge det til
    if fant_info == False:
        print(f"{land_info} har jeg dessverre ikke informasjon om.")
        registrere_info = input(f"Vil du legge til {land_info}? (J/N)") #Svar som begynner med j/J eller n/N tolkes som Ja eller Nei 
        registrere_info = registrere_info[0]
        registrere_info = stor_bokstav(registrere_info)
        if registrere_info == "J":
            hovedstad = input(f"Hva heter hovedstaden i {land_info}?")
            hovedstad = stor_bokstav(hovedstad)
            antall_innbyggere = (input(f"Hvor mange millioner innbyggere har {hovedstad}?"))
            if antall_innbyggere.isnumeric(): #Kun tall er tillatt
                antall_innbyggere = float(antall_innbyggere)
            else:
                antall_innbyggere = "ukjent antall" #Dersom noe annet enn et tall legges inn for antall innbyggere
            data.update({land_info: [hovedstad, antall_innbyggere]})
        elif registrere_info != "N": #Avslutter dersom det svares noe som hverken begynner med J eller N
            print("Programmet avsluttes. Takk for nå!")
            break
    
        
       