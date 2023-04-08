# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 17:45:30 2021

@author: noamb
"""

import sqlite3 as sgbd
import matplotlib.pyplot as plt 

conn= sgbd.connect('villes_france.sqlite')

c2 = conn.cursor()

c2.execute("""SELECT ville_longitude_deg, ville_latitude_deg, ville_population_1999 FROM villes_france_free WHERE LENGTH(ville_departement)=2 """)
tab=c2.fetchall()

X=[]
Y=[]
P=[]
for i in tab:
    X.append(float(i[0]))
    Y.append(float(i[1]))
    P.append(int(i[2])/10000)
def couleurs(t,j):  #Permet d'associer une couleur selon le nombre d'habitants de chaque ville
    colors=['greenyellow','green','goldenrod','darkred','maroon','black']

    #for j in range(len(t)):
    if int(t[j][2])<=100:
        c=colors[0]
    if 100<int(t[j][2])<=1000:
        c=colors[1]
    if 1000<int(t[j][2])<=10000:
        c=colors[2]
    if 10000<int(t[j][2])<=100000:
        c=colors[3]
    if 100000<int(t[j][2])<=1000000:
        c=colors[4]
    if 1000000<int(t[j][2])<=10000000:
        c=colors[5]
    return c

liste=[]
for k in range(len(tab)):
    liste.append([tab[k],couleurs(tab,k)])
print(liste)

L=[]
for m in range(len(liste)):
    L.append(liste[m][1])
    
plt.axis('off')
plt.title("Carte de la France population en 1999 ")
plt.scatter(X,Y,s=10,marker='.',color=L, label='Plus la couleur est foncé plus la ville est peuplée')
plt.legend()
plt.savefig('france(population1999).png')
plt.show()
plt.close()