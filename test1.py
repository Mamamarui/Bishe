import RLP
import numpy as np

path_input="E:\Bishe\code\quarter"
path_out="E:\Bishe\code\onecore"

len_quarter=17

file=open(path_input,'r')
quarter=[[]]*len_quarter
temp=file.readlines()
for i in range(len_quarter):
    quarter[i]=temp[i].split()
file.close()

#onecore=RLP.qto(quarter,len_quarter)
onecore=RLP.whirl(quarter,len_quarter)

file_out=open(path_out,'w+')
for i in range(len_quarter*2):
    for j in range(len_quarter*2):
        if(j!=len_quarter*2-1):
            file_out.write("%1d  " %(onecore[i,j]))
        else:
            file_out.write("%01d  \n" %(onecore[i,j]))
file_out.close()


#cycle1_conum=np.array([13,47,38,13,27,7,58,13,13,27,7,58,27,27,27,27,\
#                       101,102,103,104,105])
#
#file=open(path_input,'r')
#quarter=[[]]*len_quarter
#temp=file.readlines()
#for i in range(len_quarter):
#    quarter[i]=temp[i].split()
#file.close()
#cycle2_ma=RLP.qto_ma(quarter,len_quarter)
#
#for i in range(17):
#    for j in range(17):
#        if(0<i<16 and 0<j<16):
#            if(ALP[0,i-1,j-1]!=0):
#                cycle2_ma[2*i,2*j]=cycle2_ma[2*i+1,2*j]=cycle2_ma[2*i,2*j+1]\
#                    =cycle2_ma[2*i+1,2*j+1]=cycle1_conum[ALP[0,i-1,j-1]-1]
#            elif(i==8 and j==8):
#                cycle2_ma[2*i,2*j]=cycle2_ma[2*i+1,2*j]=cycle2_ma[2*i,2*j+1]\
#                    =cycle2_ma[2*i+1,2*j+1]=0
#cycle2_ma[16,16]=cycle2_ma[16,17]=cycle2_ma[17,16]=cycle2_ma[17,17]=5                    
#print(cycle2_ma)

#file_out=open(path_out,'w+')
#for i in range(15):
#    for j in range(15):
#        if(j!=14):
#            file_out.write("%3s " %la[i][j])
#        elif(i!=14):
#            file_out.write("%3s \n" %la[i][j])
#        else:
#            file_out.write("%3s " %la[i][j])
#file_out.close()