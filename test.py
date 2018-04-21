# -*- coding: utf-8 -*-
import RLP
import card
import numpy as np

path_input="F:\Bishe\code\input\BAMBOO_AP1000_cycle2.DAT"
path_out="F:\Bishe\code\out"

file_input=open(path_input,'r')
input_lines=file_input.readlines()
input_len=len(input_lines)



GLP=RLP.generateLP()
CLP=RLP.adjustLP(GLP)
ALP=RLP.allLP(CLP)
la=card.generatelabels(ALP)

#
file_name=path_out+'\\test'
file_out=open(file_name,'w+')
#        
#temp=card.modify_labels(input_lines,la)
out_lines=card.modify_MaterialArr(input_lines,25,2,1,17,ALP)
#        
file_out.writelines(out_lines)
#
file_input.close()
file_out.close()