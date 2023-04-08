# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 11:22:45 2021

@author: nboulze
"""
import sqlite3 as sgbd
import matplotlib.pyplot as plt 
import numpy as np

conn= sgbd.connect('villes_france.sqlite')

c1 = conn.cursor()

c1.execute("""SELECT ville_longitude_deg, ville_latitude_deg  FROM villes_france_free WHERE LENGTH(ville_departement)=2 """)
tab=c1.fetchall()
print(tab)


X=[]
Y=[]
for i in tab:
    X.append(float(i[0]))
    Y.append(float(i[1])/10)
    
plt.axis('off')    
plt.title("Carte de la France ")
plt.scatter(X,Y,s=50, c='b')
plt.savefig('france.png')
plt.show()
plt.close()
