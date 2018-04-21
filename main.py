# -*- coding: utf-8 -*-
import RLP
import card
import encodeanddecode
import numpy as np
import os

path_input="F:\Bishe\code\input\BAMBOO_AP1000_cycle2.DAT"
path_out="F:\Bishe\code\out"

len_quarter=17
z_mesh=25

#GLP=RLP.generateLP()
#CLP=RLP.adjustLP(GLP)
#ALP=RLP.allLP(CLP)

#print(GLP)
#print(CLP)
#print(ALP)

onehot=encodeanddecode.readonehot(r'F:\Bishe\code\out\train1\labels')
LP=encodeanddecode.decoder(onehot)
ALP=RLP.allLP(LP)
labels=card.generatelabels(ALP)
print(labels)
#for i in range(1):
#    file_input=open(path_input,'r')
#    input_lines=file_input.readlines()
#    input_len=len(input_lines)
#    file_input.close()
#    
#    GLP=RLP.generateLP()
#    CLP=RLP.adjustLP(GLP)
#    ALP=RLP.allLP(CLP)
#    la=card.generatelabels(ALP)
#    print(CLP)
#            
#    out_lines=card.modify_labels(input_lines,la)
#    out_lines=card.modify_MaterialArr(out_lines,z_mesh,2,1,len_quarter,ALP)
#    out_lines=card.modify_OrientationArr(out_lines,z_mesh,len_quarter)
#    
#    file_name='train'+str(i+1)
#    if not os.path.exists(os.path.join(path_out,file_name)):
#        os.makedirs(os.path.join(path_out,file_name))
#    
#    with open(os.path.join(path_out,file_name,'BAMBOO.DAT'),'w+') as file_out:
#        file_out.writelines(out_lines)
#    onehot=encodeanddecode.encoder(CLP)
#    encodeanddecode.output(os.path.join(path_out,file_name,'labels'),onehot)
        

