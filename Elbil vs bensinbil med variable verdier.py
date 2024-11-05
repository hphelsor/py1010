#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 19:57:29 2024

@author: hanspetter

Programmet kalkulerer og sammenligner kostnadene ved elbil og bensinbil
"""
# Oppgi km pr år, negativt tall tolkes som positivt
km = abs(int(input("Hvor mange kilometer kjører du pr. år?")))

# Ber om data for beregning av kostnader
forsikring_el = int(input("Hva er forsikringspremien for elbil?"))
forsikring_bensin = int(input("Hva er forsikringspremien for bensinbil?"))
forbruk_el = (float(input("Hvor mange kWh bruker elbilen pr. mil?")))/10
pris_el = float(input("Hva er gjennomsnittlig pris pr. kWh?"))
energi_el = float(km*forbruk_el*pris_el)
forbruk_bensin = (float(input("Hva er bensinbilens forbruk i liter pr. mil?")))/10
pris_bensin = float(input("Hva er gjennomsnittlig pris pr. liter bensin?"))
energi_bensin = float(km*forbruk_bensin*pris_bensin)

# Beregner kostnader som avhenger av årlig kjørelengde
bom_el = float(km * 0.1)
bom_bensin = float(km * 0.3)

# Beregner kostnader som er avhengig av lengden på perioden, (et år)
trafikkforsikring_el = float(365*8.38)  # Dager x kostnad pr dag
trafikkforsikring_bensin = float(365*8.38)  # Dager x kostnad pr dag

# Beregner kostnader som påvirkes av opplysningene som er gitt
totalkostnad_el = energi_el+bom_el+forsikring_el+trafikkforsikring_el
totalkostnad_bensin = energi_bensin+bom_bensin+forsikring_bensin+trafikkforsikring_bensin

# Presenterer kostnadsoversikter
print()
print("Elbil:")
print("Trafikkforsikring", ("%.2f" % trafikkforsikring_el), "kr")
print("Forsikring", ("%.2f" % forsikring_el), "kr")
print("Energi", ("%.2f" % energi_el), "kr")
print("Bom", ("%.2f" % bom_el), "kr")
print("---------------------------------------------------------")
print("Totalkostnad for elbil=", ("%.2f" % totalkostnad_el), "kr")
print()
print("Bensinbil:")
print("Trafikkforsikring", ("%.2f" % trafikkforsikring_bensin), "kr")
print("Forsikring", ("%.2f" % forsikring_bensin), "kr")
print("Energi", ("%.2f" % energi_bensin), "kr")
print("Bom", ("%.2f" % bom_bensin), "kr")
print("---------------------------------------------------------")
print("Totalkostnad for bensinbil=", ("%.2f" % totalkostnad_bensin), "kr")
print()

# Sammenligner og presenterer kostnadsforskjell mellom biltypene
if totalkostnad_bensin > totalkostnad_el:
    print("Bensinbil er", ("%.2f" % (totalkostnad_bensin-totalkostnad_el)),"dyrere enn elbil i året")
elif totalkostnad_bensin < totalkostnad_el:
    print("Bensinbil er", ("%.2f" % (totalkostnad_el-totalkostnad_bensin)),"billigere enn elbil i året")
else:
    print("Bensinbil og elbil er like dyrt")
