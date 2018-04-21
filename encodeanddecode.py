# -*- coding: utf-8 -*-
from sklearn import preprocessing
import numpy as np
import RLP

#one hot samples
enc = preprocessing.OneHotEncoder()
enc.fit([[1,1],[2,2],[3,3],[4,4],[5,0],[6,4],[7,4],[8,4],[9,4],[10,4],\
         [11,4],[12,4],[13,4],[14,4],[15,4],[16,4],[17,4],[18,4],[19,4],[20,4],[21,4]])

def encoder(CLP):
    '''
    编码
    '''
    onehot=np.zeros((25,26))
    counter=0
    for i in range(8):
        for j in range(8):
            if (CLP[0,i,j]!=0 and i<=j):
                onehot[counter,:]=enc.transform([[CLP[0,i,j],CLP[1,i,j]]]).toarray()
                counter+=1
    return onehot

def output(path_out,onehot):
    '''
    将编码输出
    '''
    m,n=onehot.shape
    with open(path_out,'w+') as f:
        for i in range(m):
            tempstr=''
            for j in range(n):
                if (j==n-1):
                    tempstr=tempstr+'%2s \n' %str(int(onehot[i,j]))
                else:
                    tempstr=tempstr+'%2s' %str(int(onehot[i,j]))
            f.write(tempstr)

def decoder(onehot):
    '''
    解码
    '''
    LP=np.zeros((2,8,8))
    temp=np.zeros((3,25),int)
    m,n=onehot.shape
    for i in range(m):
        for j in range(n):
            if (onehot[i,j]==1):
                if (temp[1,i]==0):
                    temp[1,i]=j+1
                else:
                    temp[2,i]=j-21
    for i in range(25):
        temp[0,i]=i+1
    LP=RLP.adjustLP(temp)
    return LP
    
def readonehot(path):
    '''
    对指定文件解码
    '''
    with open(path) as f:
        lines=f.readlines()
        onehot=np.zeros((25,26))
        for i in range(len(lines)):
            temp=lines[i].split()
            for j in range(26):
                onehot[i,j]=int(temp[j])
    return onehot
        