# -*- coding: utf-8 -*-
import numpy as np
import random

def generateLP():
    order=random.sample(range(1,26),25)
    result=np.zeros((2,25),int)
    counter=np.zeros((1,18))
    for i in range(25):
        result[0,i]=order[i]
        if(result[0,i]<12):                    #1/4对称线上
            while(result[1,i]==0):
                n=random.randint(1,21)
                if(n<17):                      #旧料
                    if(n==1 or n==2 or n==5 or n==13 or n==16):
                        if(counter[0,n-1]<1):
                            result[1,i]=n
                            counter[0,n-1]+=1
                    else:
                        if(counter[0,n-1]<2):
                            result[1,i]=n
                            counter[0,n-1]+=1
                else:
                    if(n==17):
                        if(counter[0,n-1]<=6):
                            result[1,i]=n
                            counter[0,n]+=1
                    elif(n==18):
                        if(counter[0,n-1]<=5):
                            result[1,i]=n
                            counter[0,n-1]+=1
        else:
            while(result[1,i]==0):
                n=random.randint(1,21)
                if(n<17):                      #旧料
                    if(n==1 or n==2 or n==5 or n==13 or n==16):
                        if(counter[0,n-1]<1):
                            result[1,i]=n
                            counter[0,n-1]+=1
                    else:
                        if(counter[0,n-1]<1):
                            result[1,i]=n
                            counter[0,n-1]+=1
                else:
                    if(n==17):
                        if(counter[0,n-1]<=6):
                            result[1,i]=n
                            counter[0,n-1]+=1
                    elif(n==18):
                        if(counter[0,n-1]<=5):
                            result[1,i]=n
                            counter[0,n-1]+=1
    return result

LP=np.zeros((7,5))
tempLP=generateLP()

                        
                    