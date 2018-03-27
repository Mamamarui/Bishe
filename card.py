# -*- coding: utf-8 -*-
import numpy as np
import copy


path_cycle1="F:\Bishe\LP"


#print("CYCLE1LP:")
#print(CYCLE1LP)

def generatelabels(ALP):
# read cycle1 fuels assembly labels
    file=open(path_cycle1,'r')
    CYCLE1LABELS=[[]]*15
    temp=file.readlines()
    for i in range(15):
        CYCLE1LABELS[i]=temp[i].split()
    file.close()
        
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
    location=np.zeros((17,4),int)
    for i in range(8):
        for j in range(8):
            if(qcore[i,j]!=0):
                if (location[qcore[i,j],1]==0):
                    location[qcore[i,j],0]=i
                    location[qcore[i,j],1]=j
                else:
                    location[qcore[i,j],2]=i
                    location[qcore[i,j],3]=j
                    
    labels=copy.deepcopy(CYCLE1LABELS)
    count=1
    use=np.zeros((4,17,2),int)
    for i in range(15):
        for j in range(15):
            if(ALP[0,i,j]==0):
                labels[i][j]="   "
            else:
                if(ALP[0,i,j]>16):
                    if(count<10):
                        temp_str='F0'+str(count)
                        labels[i][j]=temp_str
                        count+=1
                    else:
                        temp_str='F'+str(count)
                        labels[i][j]=temp_str
                        count+=1
                elif(ALP[1,i,j]==1):
                    if(use[ALP[1,i,j]-1,ALP[0,i,j],0]==0):
                        labels[i][j]=CYCLE1LABELS[location[ALP[0,i,j],0\
                                  ]][location[ALP[0,i,j],1]+7]
                        use[ALP[1,i,j]-1,ALP[0,i,j],0]+=1
                    else:
                        labels[i][j]=CYCLE1LABELS[location[ALP[0,i,j],2\
                                  ]][location[ALP[0,i,j],3]+7]
                        use[ALP[1,i,j]-1,ALP[0,i,j],1]+=1
                elif(ALP[1,i,j]==2):
                    if(location[ALP[0,i,j],0]!=7):
                        if(use[ALP[1,i,j]-1,ALP[0,i,j],0]==0):
                            labels[i][j]=CYCLE1LABELS[location[ALP[0,i,j],0\
                                      ]][7-location[ALP[0,i,j],1]]
                            use[ALP[1,i,j]-1,ALP[0,i,j],0]+=1
                        else:
                            labels[i][j]=CYCLE1LABELS[location[ALP[0,i,j],2\
                                      ]][7-location[ALP[0,i,j],3]]
                            use[ALP[1,i,j]-1,ALP[0,i,j],1]+=1
                    else:
                        if(use[ALP[1,i,j]-1,ALP[0,i,j],0]==0):
                            labels[i][j]=CYCLE1LABELS[7-location[ALP[0,i,j],1\
                                      ]][location[ALP[0,i,j],0]]
                            use[ALP[1,i,j]-1,ALP[0,i,j],0]+=1
                        else:
                            labels[i][j]=CYCLE1LABELS[7-location[ALP[0,i,j],3\
                                      ]][location[ALP[0,i,j],2]]
                            use[ALP[1,i,j]-1,ALP[0,i,j],1]+=1
                elif(ALP[1,i,j]==3):
                    if(use[ALP[1,i,j]-1,ALP[0,i,j],0]==0):
                        labels[i][j]=CYCLE1LABELS[14-location[ALP[0,i,j],0\
                                  ]][7-location[ALP[0,i,j],1]]
                        use[ALP[1,i,j]-1,ALP[0,i,j],0]+=1
                    else:
                        labels[i][j]=CYCLE1LABELS[14-location[ALP[0,i,j],2\
                                  ]][7-location[ALP[0,i,j],3]]
                        use[ALP[1,i,j]-1,ALP[0,i,j],1]+=1
                elif(ALP[1,i,j]==4):
                    if(location[ALP[0,i,j],0]!=7):
                        if(use[ALP[1,i,j]-1,ALP[0,i,j],0]==0):
                            labels[i][j]=CYCLE1LABELS[14-location[ALP[0,i,j],0\
                                      ]][location[ALP[0,i,j],1]+7]
                            use[ALP[1,i,j]-1,ALP[0,i,j],0]+=1
                        else:
                            labels[i][j]=CYCLE1LABELS[14-location[ALP[0,i,j],2\
                                      ]][location[ALP[0,i,j],3]+7]
                            use[ALP[1,i,j]-1,ALP[0,i,j],1]+=1
                    else:
                        if(use[ALP[1,i,j]-1,ALP[0,i,j],0]==0):
                            labels[i][j]=CYCLE1LABELS[7+location[ALP[0,i,j],1\
                                      ]][location[ALP[0,i,j],0]]
                            use[ALP[1,i,j]-1,ALP[0,i,j],0]+=1
                        else:
                            labels[i][j]=CYCLE1LABELS[7+location[ALP[0,i,j],3\
                                      ]][location[ALP[0,i,j],2]]
                            use[ALP[1,i,j]-1,ALP[0,i,j],1]+=1
    
    return labels