# -*- coding: utf-8 -*-
import numpy as np

path_cycle1="F:\Bishe\LP"


#print("CYCLE1LP:")
#print(CYCLE1LP)

def generatelabels(ALP):
    #read cycle1 fuels assembly labels
    file=open(path_cycle1,'r')
    CYCLE1LABELS=[[]]*15
    temp=file.readlines()
    for i in range(15):
        CYCLE1LABELS[i]=temp[i].split()
        
    #CYCLE1 assembly number
    qcore=np.array([[1,0,0,0,0,0,0,0],                                         
           [2,3,4,0,0,0,0,0],
           [5,6,7,8,9,0,0,0],
           [0,10,11,12,0,9,0,0],
           [13,0,14,0,12,8,0,0],
           [0,15,0,14,11,7,4,0],
           [16,0,15,0,10,6,3,0],
           [0,16,0,13,0,5,2,1]])
    hcore=np.zeros((15,15))
    hcore[0:8,7:15]=qcore
    for i in range(8):
        if(i!=0):
            hcore[7+i,:]=hcore[7-i]
    for i in range(8):
        if(i!=0):
            hcore[:,7-i]=hcore[:,7+i]
    
    labels=[[]]*15
    for i in range(15):
        for j in range(15):
            if(ALP[0,i,j]==0):
                if(ALP[1,i,j]!=0):
                    labels[i][j]=
    
print(hcore)
