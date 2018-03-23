# -*- coding: utf-8 -*-
import numpy as np
import random

def generateLP():
    order=random.sample(range(1,26),25)
    result=np.zeros((3,25),int)
    counter=np.zeros((1,18))
    for i in range(25):
        result[0,i]=order[i]                                                   #坐标编号
        if(result[0,i]<=8 or result[0,i]==15 or result[0,i]==20 or \
           result[0,i]==24):                                                    #1/4对称线上
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
                else:                                                          #新料
                    if(n==17):
                        if(counter[0,n-1]<=6):
                            result[1,i]=n
                            result[2,i]=0
                            counter[0,n]+=1
                    elif(n==18):
                        if(counter[0,n-1]<=5):
                            result[1,i]=n
                            result[2,i]=0
                            counter[0,n-1]+=1
        else:                                                                  #1/8对称区域上
            while(result[1,i]==0):
                n=random.randint(1,21)
                if(n<17):                                                      #旧料
                    if(n!=1 and n!=2 and n!=5 and n!=13 and n!=16):
                        if(counter[0,n-1]<1):
                            result[1,i]=n
                            result[2,i]=random.randint(1,4)
                            counter[0,n-1]+=1
                else:                                                          #新料
                    if(n==17):
                        if(counter[0,n-1]<=6):
                            result[1,i]=n
                            result[2,i]=0
                            counter[0,n-1]+=1
                    elif(n==18):
                        if(counter[0,n-1]<=5):
                            result[1,i]=n
                            result[2,i]=0
                            counter[0,n-1]+=1
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
                        CLP[0,i,j]=CLP[0,j,i]+1
                        if(CLP[0,i,j]==5):
                            CLP[0,i,j]=1
                    else:
                        CLP[0,i,j]=CLP[0,j,i]
        
    return CLP
            


GLP=generateLP()
print("glp:")
print(GLP)
CLP=adjustLP(GLP)
print("clp:")
print(CLP)


                        
                    