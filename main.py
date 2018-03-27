import RLP
import card
#import numpy as np

path_out="F:\Bishe\out"

GLP=RLP.generateLP()
CLP=RLP.adjustLP(GLP)
print("clp:")
print(CLP)
ALP=RLP.allLP(CLP)
print("ALP:")
print(ALP)
la=card.generatelabels(ALP)

file_out=open(path_out,'w+')
for i in range(15):
    for j in range(15):
        if(j!=14):
            temp=la[i][j]+' '
            file_out.write(temp)
        else:
            temp=la[i][j]+'\n'
            file_out.write(temp)
file_out.close()
