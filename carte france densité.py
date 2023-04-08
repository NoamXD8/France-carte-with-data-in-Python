# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 14:48:25 2021

@author: noamb
"""
import sqlite3 as sgbd
import matplotlib.pyplot as plt 

conn= sgbd.connect('villes_france.sqlite')

c2 = conn.cursor()

c2.execute("""SELECT ville_longitude_deg, ville_latitude_deg, ville_densite_2010 FROM villes_france_free WHERE LENGTH(ville_departement)=2 """)
tab1=c2.fetchall()
print(tab1)

X=[]
Y=[]
D=[]
for i in tab1:
    X.append(float(i[0]))
    Y.append(float(i[1]))
    D.append(int(i[2])/1000)

plt.axis('off')
plt.title("Carte de la France densité ")
plt.scatter(X,Y,D, c='red',label='Forte densité')
plt.legend()
plt.savefig('france(densité).png')
plt.show()
plt.close()