import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df_exop = pd.read_csv('ExoplanetsPars_2024.csv', comment='#')
print('Le colonne sono')
print(df_exop.columns)
print(df_exop.head)
df_transradial= df_exop.loc[(df_exop['discoverymethod']=='Transit') | (df_exop['discoverymethod']=='Radial Velocity')]
alx = df_transradial['pl_orbper']
aly = df_transradial['pl_bmassj']
plt.hist(aly,bins=50, range=(0, 2), color='gold', alpha=0.7)
plt.xlabel('Periodo orbitale')
plt.ylabel('Massa')
plt.savefig('grafico_esopianeti_scopertaisto.png')
plt.show()
