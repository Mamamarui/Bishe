# -*- coding: utf-8 -*-
import numpy as np
import copy
import RLP

path_cycle1="F:\Bishe\code\input\LP"


#print("CYCLE1LP:")
#print(CYCLE1LP)

def generatelabels(ALP):
    '''
    根据全堆芯布置生成labels
    '''
# read cycle1 fuels assembly labels
    file=open(path_cycle1,'r')
    CYCLE1LABELS=[[]]*15
    temp=file.readlines()
    for i in range(15):
        CYCLE1LABELS[i]=temp[i].split()
    file.close()
        
    #CYCLE1 assembly number
    qcore=np.array([[1,0,0,0,0,0,0,0],                                         #     编号自己编的                                  
           [2,3,4,0,0,0,0,0],
           [5,6,7,8,9,0,0,0],
           [0,10,11,12,0,9,0,0],
           [13,0,14,0,12,8,0,0],
           [0,15,0,14,11,7,4,0],
           [16,0,15,0,10,6,3,0],
           [0,16,0,13,0,5,2,1]])
    hcore=np.zeros((15,15))
    hcore[0:8,7:15]=qcore
    for i in range(8):
        if(i!=0):
            hcore[7+i,:]=hcore[7-i]
    for i in range(8):
        if(i!=0):
            hcore[:,7-i]=hcore[:,7+i]
    location=np.zeros((17,4),int)
    for i in range(8):
        for j in range(8):
            if(qcore[i,j]!=0):
                if (location[qcore[i,j],1]==0):
                    location[qcore[i,j],0]=i
                    location[qcore[i,j],1]=j
                else:
                    location[qcore[i,j],2]=i
                    location[qcore[i,j],3]=j
                    
    labels=copy.deepcopy(CYCLE1LABELS)
    count=1
    use=np.zeros((4,17,2),int)
    for i in range(15):
        for j in range(15):
            if(ALP[0,i,j]==0):
                labels[i][j]="   "
            else:
                if(ALP[0,i,j]>16):
                    if(count<10):
                        temp_str='F0'+str(count)
                        labels[i][j]=temp_str
                        count+=1
                    else:
                        temp_str='F'+str(count)
                        labels[i][j]=temp_str
                        count+=1
                elif(ALP[1,i,j]==1):
                    if(use[ALP[1,i,j]-1,ALP[0,i,j],0]==0):
                        labels[i][j]=CYCLE1LABELS[location[ALP[0,i,j],0\
                                  ]][location[ALP[0,i,j],1]+7]
                        use[ALP[1,i,j]-1,ALP[0,i,j],0]+=1
                    else:
                        labels[i][j]=CYCLE1LABELS[location[ALP[0,i,j],2\
                                  ]][location[ALP[0,i,j],3]+7]
                        use[ALP[1,i,j]-1,ALP[0,i,j],1]+=1
                elif(ALP[1,i,j]==2):
                    if(location[ALP[0,i,j],0]!=7):
                        if(use[ALP[1,i,j]-1,ALP[0,i,j],0]==0):
                            labels[i][j]=CYCLE1LABELS[location[ALP[0,i,j],0\
                                      ]][7-location[ALP[0,i,j],1]]
                            use[ALP[1,i,j]-1,ALP[0,i,j],0]+=1
                        else:
                            labels[i][j]=CYCLE1LABELS[location[ALP[0,i,j],2\
                                      ]][7-location[ALP[0,i,j],3]]
                            use[ALP[1,i,j]-1,ALP[0,i,j],1]+=1
                    else:
                        if(use[ALP[1,i,j]-1,ALP[0,i,j],0]==0):
                            labels[i][j]=CYCLE1LABELS[7-location[ALP[0,i,j],1\
                                      ]][location[ALP[0,i,j],0]]
                            use[ALP[1,i,j]-1,ALP[0,i,j],0]+=1
                        else:
                            labels[i][j]=CYCLE1LABELS[7-location[ALP[0,i,j],3\
                                      ]][location[ALP[0,i,j],2]]
                            use[ALP[1,i,j]-1,ALP[0,i,j],1]+=1
                elif(ALP[1,i,j]==3):
                    if(use[ALP[1,i,j]-1,ALP[0,i,j],0]==0):
                        labels[i][j]=CYCLE1LABELS[14-location[ALP[0,i,j],0\
                                  ]][7-location[ALP[0,i,j],1]]
                        use[ALP[1,i,j]-1,ALP[0,i,j],0]+=1
                    else:
                        labels[i][j]=CYCLE1LABELS[14-location[ALP[0,i,j],2\
                                  ]][7-location[ALP[0,i,j],3]]
                        use[ALP[1,i,j]-1,ALP[0,i,j],1]+=1
                elif(ALP[1,i,j]==4):
                    if(location[ALP[0,i,j],0]!=7):
                        if(use[ALP[1,i,j]-1,ALP[0,i,j],0]==0):
                            labels[i][j]=CYCLE1LABELS[14-location[ALP[0,i,j],0\
                                      ]][location[ALP[0,i,j],1]+7]
                            use[ALP[1,i,j]-1,ALP[0,i,j],0]+=1
                        else:
                            labels[i][j]=CYCLE1LABELS[14-location[ALP[0,i,j],2\
                                      ]][location[ALP[0,i,j],3]+7]
                            use[ALP[1,i,j]-1,ALP[0,i,j],1]+=1
                    else:
                        if(use[ALP[1,i,j]-1,ALP[0,i,j],0]==0):
                            labels[i][j]=CYCLE1LABELS[7+location[ALP[0,i,j],1\
                                      ]][location[ALP[0,i,j],0]]
                            use[ALP[1,i,j]-1,ALP[0,i,j],0]+=1
                        else:
                            labels[i][j]=CYCLE1LABELS[7+location[ALP[0,i,j],3\
                                      ]][location[ALP[0,i,j],2]]
                            use[ALP[1,i,j]-1,ALP[0,i,j],1]+=1
    labels[7][7]='B47'
    return labels

def search(tstr,input_lines):
    '''
    在指定的list中搜索字符串，返回该字符串的行数
    '''
    target_line=-1
    for i in range(len(input_lines)):
        if tstr in input_lines[i]:
            target_line=i
            break
    if(target_line<0):
        print("The string '%s' is not found." %tstr)
    else:
        return target_line

def modify_labels(input_lines,labels):
    '''
    修改给定card中的标签
    '''
    tline=search('#   FUEL ASSEMBLY LABELS (NAXL*NAYL)',input_lines)
    del input_lines[tline+2:tline+17]
    for i in range(15):
        temp=' '
        for j in range(15):
            if(j!=14):
                temp=temp+labels[i][j]+' '
            else:
                temp=temp+labels[i][j]+'\n'
        input_lines.insert(tline+2+i,temp)
    
    return input_lines

def modify_OrientationArr(input_lines,z_mesh,len_quarter):
    '''
    修改给定CARD中的旋转编码
    '''
    quarter=[[]]*len_quarter
    temp=np.zeros((z_mesh,2*len_quarter,2*len_quarter))
    tline=search('#   MATERIAL ORIENTATION ARRANGEMENT:UPPER->BOTTOM',\
                 input_lines)
    for i in range(z_mesh):
        for j in range(len_quarter):
            quarter[j]=input_lines[tline+1+j+i*len_quarter].split()
        onecore=RLP.whirl(quarter,len_quarter)
        temp[i,:,:]=onecore
    del input_lines[tline+1:tline+1+z_mesh*len_quarter]
    for i in range(z_mesh):
        for j in range(2*len_quarter):
            temp_str=' '
            for k in range(2*len_quarter):
                if(k!=2*len_quarter-1):
                    temp_str=temp_str+str(int(temp[i,j,k]))+' '
                else:
                    temp_str=temp_str+str(int(temp[i,j,k]))+'\n'
            input_lines.insert(tline+1+j+i*len_quarter*2,temp_str)
    return input_lines
        
def modify_MaterialArr(input_lines,z_mesh,top_ref,bottom_ref,len_quarter,ALP):
    '''
    修改给定card中的材料区编码
    '''
    start_line=search('#   MATERIAL ARRANGEMENT:UPPER->BOTTOM',input_lines)
    qcore=np.array([[1,0,0,0,0,0,0,0],                                         
           [2,3,4,0,0,0,0,0],
           [5,6,7,8,9,0,0,0],
           [0,10,11,12,0,9,0,0],
           [13,0,14,0,12,8,0,0],
           [0,15,0,14,11,7,4,0],
           [16,0,15,0,10,6,3,0],
           [0,16,0,13,0,5,2,1]])
    z_ass=np.zeros((z_mesh,21))
    temp_array=np.zeros((z_mesh,17,17))
    for i in range(z_mesh):
        for j in range(len_quarter):
            temp_list=input_lines[start_line+1+j+i*len_quarter].split()
            temp_array[i,j,:]=temp_list[:]
    
    for i in range(z_mesh):
        if(top_ref<=i<z_mesh-bottom_ref):
            for j in range(8):
                for k in range(8):
                    if(j+k<7):
                        if(qcore[j,k]!=0):
                            z_ass[i,qcore[j,k]-1]=temp_array[i,2*j+2,2*k]
    
    for i in range(z_mesh):
        if(i==2 or i==23):
            z_ass[i,16:21]=[88,91,94,97,100]
        elif(i==3 or i==22):
            z_ass[i,16:21]=[89,92,95,98,101]
        elif(3<i<22):
            z_ass[i,16:21]=[87,90,93,96,99]
                              
    for i in range(z_mesh):
        cycle2_ma=RLP.qto_ma(temp_array[i,:,:],len_quarter)
        del input_lines[start_line+1+i*2*len_quarter:start_line+1+(2*i+1)*\
                            len_quarter]
        if(top_ref-1<i<z_mesh-bottom_ref):
            for j in range(len_quarter):
                for k in range(len_quarter):
                    if(0<j<16 and 0<k<16):
                        if(ALP[0,j-1,k-1]!=0):
                            cycle2_ma[2*j,2*k]=cycle2_ma[2*j+1,2*k]=cycle2_ma[\
                                     2*j,2*k+1]=cycle2_ma[2*j+1,2*k+1\
                                              ]=z_ass[i,ALP[0,j-1,k-1]-1]
                        elif(j==8 and k==8):
                            cycle2_ma[2*j,2*k]=cycle2_ma[2*j+1,2*k]=cycle2_ma[\
                                     2*j,2*k+1]=cycle2_ma[2*j+1,2*k+1\
                                              ]=z_ass[i,5]
            #将cycle2——ma转换为字符串输出
        for j in range(2*len_quarter):
            temp_str=' '
            for k in range(2*len_quarter):
                if(k!=2*len_quarter-1):
                    temp_str=temp_str+'%3s ' %str(int(cycle2_ma[j,k]))
                else:
                    temp_str=temp_str+'%3s \n' %str(int(cycle2_ma[j,k]))
            input_lines.insert(start_line+1+j+i*len_quarter*2,temp_str)
    
    return input_lines