
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


df_kep = pd.read_csv('kplr010666592-2011240104155_slc.csv')

print('Nome delle colonne')
print(df_kep.columns)

arx = df_kep['TIME']
ary = df_kep['PDCSAP_FLUX']
ery = df_kep['PDCSAP_FLUX_ERR']
fig, ax = plt.subplots(figsize=(12,6))
ax.errorbar(arx,ary, yerr=ery, label='Grafico principale', fmt='.-')
ins_ax = ax.inset_axes([0.7, 0.1, 0.25, 0.25]) 
ins_ax.errorbar( arx[:4000], ary[:4000], yerr=ery[:4000],fmt='.-',color='limegreen' )
ax.set_title('Grafico flusso/tempo')
ax.set_xlabel('tempo')
ax.set_ylabel('flusso')
plt.savefig('grafico_tutto_minimo.png')
plt.xlabel('Tempo')
plt.ylabel('Flusso')
plt.show()
