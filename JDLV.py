#faire \venv\Scripts\activate.psa1
import os
import time
import copy
import numpy as np
import matplotlib.pyplot as plt

def genTab(dim):
    line = [0 for i in range(dim)]
    tableau = [line for i in range(dim)]
    return tableau


class JeuDeLaVie :
    def __init__(self,tableau):
        "tableau a deux dimensions"
        assert np.ndim(tableau)==2
        self.tab = tableau
        self.dim = np.shape(tableau)[0]
        self.fig,self.ax = plt.subplots()
        
    
    def affiche(self):
        img_handle = self.ax.imshow(np.array(self.tab), cmap='binary')
        plt.axis('off')
        plt.pause(0.001) 


    def val_case(self,i,j):
        if i<self.dim and j<self.dim:
            return self.tab[i][j]
        else:
            return 0
    
    def total_voiz(self,i,j):
        return self.tab[i-1][j-1]+self.tab[i-1][j]+self.tab[i-1][j+1]+self.tab[i][j-1]+self.tab[i][j+1]+self.tab[i+1][j-1]+self.tab[i+1][j]+self.tab[i+1][j+1]

    def opex(self, val_ca, sum_n):
        if val_ca == 0 and sum_n==3:
            return 1
        elif val_ca == 1 :
            if sum_n == 2 or sum_n == 3 :
                return val_ca
            else :
                return 0
        else : 
            return val_ca
            

    def tour(self):
        stock = copy.deepcopy(self.tab)
        for i in range(1,self.dim-1):
            for j in range(1,self.dim-1):
                val = self.val_case(i,j)
                tot = self.total_voiz(i,j)
                stock[i][j] = self.opex(val,tot)
        self.tab = stock
        
    
    def run(self, nb_tours,delay):
        plt.ion()
        for i in range(nb_tours):
            self.affiche()
            self.tour()
            time.sleep(delay)
        plt.ioff()
        plt.show()


tableau =  [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
mon_jeu = JeuDeLaVie(tableau)
#mon_jeu.affiche()
mon_jeu.run(100, 0.1)