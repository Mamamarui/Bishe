import RLP
#import numpy as np

path_cycle1="F:\Bishe\LP"

file=open(path_cycle1,'r')
CYCLE1LP=[[]]*15
temp=file.readlines()
for i in range(15):
    CYCLE1LP[i]=temp[i].split()
#print("CYCLE1LP:")
#print(CYCLE1LP)


GLP=RLP.generateLP()
print("glp:")
print(GLP)
CLP=RLP.adjustLP(GLP)
print("clp:")
print(CLP)
ALP=RLP.allLP(CLP)
print("ALP:")
print(ALP)