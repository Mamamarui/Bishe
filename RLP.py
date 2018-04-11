# -*- coding: utf-8 -*-
import numpy as np
import random

def generateLP():
    order=random.sample(range(1,26),25)
    result=np.zeros((3,25),int)
    counter=np.zeros((1,21))
    F1=[17,19]
    for i in range(25):
        result[0,i]=order[i]                                                   #坐标编号
        if(result[0,i]<=8 or result[0,i]==15 or result[0,i]==20 or \
           result[0,i]==24):                                                   #1/4对称线上
            while(result[1,i]==0):
                n=random.randint(1,21)
                if(n<17):                                                      #旧料
                    if(n==1 or n==2 or n==5 or n==13 or n==16):
                        if(counter[0,n-1]<1):
                            result[1,i]=n
                            result[2,i]=random.randint(1,4)
                            counter[0,n-1]+=1
                    else:
                        if(counter[0,n-1]<2):
                            result[1,i]=n
                            result[2,i]=random.randint(1,4)
                            counter[0,n-1]+=1
                elif(n==17 or n==18 or n==19):
                    if(counter[0,16]+counter[0,17]+counter[0,18]<10):
                        if(n==17 or n==19):
                            if(counter[0,n-1]<3):
                                result[1,i]=n
                                result[2,i]=0
                                counter[0,n-1]+=1
                            else:
                                result[1,i]=18
                                result[2,i]=0
                                counter[0,17]+=1
                        else:
                            if(counter[0,n-1]<6):
                                result[1,i]=n
                                result[2,i]=0
                                counter[0,n-1]+=1
                            else:
                                result[1,i]=random.choice(F1)
                                result[2,i]=0
                                counter[0,result[1,i]-1]+=1
                elif(n==20 or n==21):
                    if(counter[0,19]+counter[0,20]<8):
                        if(n==20 and counter[0,19]<6):
                            result[1,i]=n
                            result[2,i]=0
                            counter[0,n-1]+=1
                        else:
                            result[1,i]=21
                            result[2,i]=0
                            counter[0,20]+=1
        else:                                                                  #1/8对称区域上
            while(result[1,i]==0):
                n=random.randint(1,21)
                if(n<17):                                                      #旧料
                    if(n!=1 and n!=2 and n!=5 and n!=13 and n!=16):
                        if(counter[0,n-1]<1):
                            result[1,i]=n
                            result[2,i]=random.randint(1,4)
                            counter[0,n-1]+=2
                elif(n==17 or n==18 or n==19):
                    if(counter[0,16]+counter[0,17]+counter[0,18]<11):
                        if(n==17 or n==19):
                            if(counter[0,n-1]<3):
                                result[1,i]=n
                                result[2,i]=0
                                counter[0,n-1]+=2
                            else:
                                result[1,i]=18
                                result[2,i]=0
                                counter[0,17]+=2
                        else:
                            if(counter[0,n-1]<6):
                                result[1,i]=n
                                result[2,i]=0
                                counter[0,n-1]+=2
                            else:
                                result[1,i]=random.choice(F1)
                                result[2,i]=0
                                counter[0,result[1,i]-1]+=2
                elif(n==20 or n==21):
                    if(counter[0,19]+counter[0,20]<9):
                        if(n==20 and counter[0,19]<6):
                            result[1,i]=n
                            result[2,i]=0
                            counter[0,n-1]+=2
                        else:
                            result[1,i]=21
                            result[2,i]=0
                            counter[0,20]+=2
    return result

def adjustLP(GLP):
    CLP=np.zeros((2,8,8),int)                                                  #第一个维度表示放置的组件，第二个维度表示旋转编码
    for i in range(25):
        if(GLP[0,i]<=7):
            CLP[0,0,GLP[0,i]]=GLP[1,i]
            CLP[1,0,GLP[0,i]]=GLP[2,i]
        elif(7<GLP[0,i]<=14):
            CLP[0,1,GLP[0,i]-7]=GLP[1,i]
            CLP[1,1,GLP[0,i]-7]=GLP[2,i]
        elif(14<GLP[0,i]<=19):
            CLP[0,2,GLP[0,i]-13]=GLP[1,i]
            CLP[1,2,GLP[0,i]-13]=GLP[2,i]
        elif(19<GLP[0,i]<=23):
            CLP[0,3,GLP[0,i]-17]=GLP[1,i]
            CLP[1,3,GLP[0,i]-17]=GLP[2,i]
        elif(23<GLP[0,i]<=25):
            CLP[0,4,GLP[0,i]-20]=GLP[1,i]
            CLP[1,4,GLP[0,i]-20]=GLP[2,i]
    for i in range(8):
        for j in range(8):
            if(CLP[0,i,j]==0):
                if(i==0 and j==0):
                    CLP[0,i,j]=CLP[0,i,j]
                    CLP[1,i,j]=CLP[1,i,j]
                else:
                    CLP[0,i,j]=CLP[0,j,i]
                    if(j==0):
                        if(CLP[1,j,i]==0):
                            CLP[1,i,j]=0
                        else:
                            if(CLP[1,j,i]==1):
                                CLP[1,i,j]=4
                            else:
                                CLP[1,i,j]=CLP[1,j,i]-1
                    else:
                        CLP[0,i,j]=CLP[0,j,i]
                        CLP[1,i,j]=CLP[1,j,i]
    return CLP

def allLP(CLP):
    ALP=np.zeros((2,15,15),int)
    for i in range(8):                                                         #1/2堆芯布置
        if(i==0):
            ALP[:,i+7,7:15]=CLP[:,i,:]
        else:
            ALP[0,7-i,7:15]=CLP[0,i,:]
            ALP[0,7+i,7:15]=CLP[0,i,:]
            ALP[1,i+7,7:15]=CLP[1,i,:]
            for j in range(8):
                if(j==0):
                    if(ALP[1,7,7+i]==0):
                        ALP[1,7-i,7]=0
                    elif(ALP[1,7,7+i]==4):
                        ALP[1,7-i,7]=1
                    else:
                        ALP[1,7-i,7]=ALP[1,7,7+i]+1
                else:
                    if(ALP[1,7+i,7+j]==0):
                        ALP[1,7-i,7+j]=0
                    elif(ALP[1,7+i,7+j]==4):
                        ALP[1,7-i,7+j]=1
                    else:
                        ALP[1,7-i,7+j]=ALP[1,7+i,7+j]+1
    for i in range(8):
        if(i!=0):
            ALP[0,:,7-i]=ALP[0,:,7+i]
    for i in range(15):
        for j in range(8):
            if(j!=0):
                if(i<7):
                    if(ALP[1,i,7+j]==0):
                        ALP[1,i,7-j]=0
                    elif(ALP[1,i,7+j]==4):
                        ALP[1,i,7-j]=1
                    else:
                        ALP[1,i,7-j]=ALP[1,i,7+j]+1
                elif(i>7):
                    if(ALP[1,i,7+j]==0):
                        ALP[1,i,7-j]=0
                    elif(ALP[1,i,7+j]==1):
                        ALP[1,i,7-j]=4
                    else:
                        ALP[1,i,7-j]=ALP[1,i,7+j]-1
                elif(i==7):
                    if(ALP[1,i,7+j]==0):
                        ALP[1,i,7-j]=0
                    elif(ALP[1,i,7+j]==3):
                        ALP[1,i,7-j]=1
                    elif(ALP[1,i,7+j]==4):
                        ALP[1,i,7-j]=2
                    else:
                        ALP[1,i,7-j]=ALP[1,i,7+j]+2
    return ALP
            
def qto(origin,len_quarter):
    if(type(origin)==list):
        qarray=np.zeros((len_quarter,len_quarter))
        for i in range(len_quarter):
            for j in range(len_quarter):
                qarray[i,j]=origin[i][j]
    else:
        qarray=origin
    one_core=np.zeros((len_quarter*2-1,len_quarter*2-1),int)
    one_core[0:len_quarter,len_quarter-1:len_quarter*2-1]=qarray
    for i in range(len_quarter):
        if(i!=0):
            one_core[len_quarter-1+i,:]=one_core[len_quarter-1-i,:]
    for i in range(len_quarter):
        if(i!=0):
            one_core[:,len_quarter-1-i]=one_core[:,len_quarter-1+i]
    return one_core

def qto_ma(origin,len_quarter):
    if(type(origin)==list):
        qarray=np.zeros((len_quarter,len_quarter))
        for i in range(len_quarter):
            for j in range(len_quarter):
                qarray[i,j]=origin[i][j]
    else:
        qarray=origin
    
    one_core=np.zeros((len_quarter*2,len_quarter*2))
    one_core[0:len_quarter,len_quarter:len_quarter*2]=qarray
    for i in range(len_quarter):
        one_core[2*len_quarter-1-i,:]=one_core[i,:]
    for i in range(len_quarter):
        one_core[:,i]=one_core[:,2*len_quarter-1-i]
    return one_core

def whirl(origin,len_quarter):
    if(type(origin)==list):
        qarray=np.zeros((len_quarter,len_quarter))
        for i in range(len_quarter):
            for j in range(len_quarter):
                qarray[i,j]=origin[i][j]
    else:
        qarray=origin
        
    one_core=np.zeros((len_quarter*2,len_quarter*2))
    one_core[0:len_quarter,len_quarter:len_quarter*2]=qarray
    for i in range(2*len_quarter):
        for j in range(2*len_quarter):
            if(i<17 and j<17):
                if(one_core[j,33-i]==0):
                    one_core[i,j]=0
                else:
                    one_core[i,j]=one_core[j,33-i]+1
                    if(one_core[i,j]==5):
                        one_core[i,j]=1
            elif(i>=17 and j<17):
                if(one_core[j,33-i]==0):
                    one_core[i,j]=0
                else:
                    one_core[i,j]=one_core[j,33-i]+1
                    if(one_core[i,j]==5):
                        one_core[i,j]=1
            elif(i>=17 and j>=17):
                if(one_core[33-j,i]==0):
                    one_core[i,j]=0
                else:
                    one_core[i,j]=one_core[33-j,i]-1
                    if(one_core[i,j]==0):
                        one_core[i,j]=4
    return one_core
    




                        
                    