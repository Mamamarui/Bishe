# -*- coding: utf-8 -*-
import RLP
import card

path_input="F:\Bishe\code\input\BAMBOO_AP1000_cycle2.DAT"
path_out="F:\Bishe\code\out"

len_quarter=17
z_mesh=25

file_input=open(path_input,'r')
input_lines=file_input.readlines()
input_len=len(input_lines)
file_input.close()

GLP=RLP.generateLP()
CLP=RLP.adjustLP(GLP)
ALP=RLP.allLP(CLP)
la=card.generatelabels(ALP)
        
out_lines=card.modify_labels(input_lines,la)
out_lines=card.modify_MaterialArr(out_lines,z_mesh,2,1,len_quarter,ALP)
out_lines=card.modify_OrientationArr(out_lines,z_mesh,len_quarter)

file_name=path_out+'\\test'
file_out=open(file_name,'w+')        
file_out.writelines(out_lines)
file_out.close()

