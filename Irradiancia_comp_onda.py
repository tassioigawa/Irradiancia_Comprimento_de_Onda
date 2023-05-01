import math as m
import pandas as pd
import numpy as np

# Input
Irrad_ass = pd.read_csv("C:\Tassio\AGG\Dados_Irrad.csv", sep=";")
F = abs(Irrad_ass['Fator']) ### Fonte: ASTM,2000 (link:https://www.nrel.gov/grid/solar-resource/spectra-astm-e490.html)
Comp_Ond = abs(Irrad_ass['Wavelength'])
dj = int(input("Insira o Dia Juliano: "))
Coleta = float(input("Insira o Horario de Coleta (Hora decimal): "))
lat = -23.20077 * m.pi/180
long = -45.89085
Es = 1366.1 * 3.6
GMT = -3

###############################################Irradiância Topo da Atmosfera ############################################
# Ângulo Solar (Dia Juliano= 22/03 - dia juliano: 81, 13/04 - dia juliano: 103)
t = (2 * m.pi * (dj - 1)) / 365

# Equação do tempo
Et = 0.000075 + 0.001868 * m.cos(t)-0.032077*m.sin(t)-0.014615*m.cos(2*t)-0.04089*m.sin(2*t)*(229.18)
teste = 4*(abs(GMT*15)-(abs(long)))

# Horario Local Aparente(LAT - Local Aparent Time)
h = Coleta + (((4*(-45-(long))) + Et)/60)
dif = h - 12

# Declinação Solar
g = (0.006918 - 0.399912 * (m.cos(t)) + 0.070257 * (m.sin(t)) - 0.006758 * (m.cos(2 * t)) + 0.000907 * (m.sin(2 * t)) -
     0.002697 * (m.cos(3 * t)) + 0.00148 * (m.sin(3 * t)))

# E0
Eo = 1.000110 + (0.034221 * m.cos(t)) + (0.001280 * m.sin(t)) + (0.000719 * m.cos(2 * t)) + (0.000077 * m.sin(2 * t))

#Ângulo horário Solar
w = ((m.pi / 12) * dif * (180 / m.pi)) * m.pi / 180
#Irradiância Solar
Irradiancia = ((Es * Eo * (m.sin(g) * m.sin(lat) + m.cos(g) * m.cos(lat) * m.cos(w)))*1000)/3600
#Irradiação
Irradiacao = ((Es * Eo * (m.sin(g) * m.sin(lat) + (24/m.pi) * m.sin(m.pi/24) * m.cos(g) * m.cos(lat) * m.cos(w)))*1000)/3600

print(f"Irradiância do TOA: {round(Irradiancia,2)}W/m²")
print(f"Irradiação do TOA: {round(Irradiacao,2)}J/m²(s)")

################################################# Data frame (Comp Onda(nm) x Irradiância)  ##############################

Ond = [(y * 1000) for y in Comp_Ond]
Irrad_comp_onda = [(x * Irradiancia) for x in F]

df = pd.DataFrame(zip(Ond,Irrad_comp_onda), columns=['Comprimento de Onda', 'Irradiância'])
print(df)

df.to_csv('dados_final.csv') ##Exportar o data.frame em .csv



