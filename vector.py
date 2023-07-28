"""
@author: Asfahan
"""

import csv
import numpy as np
import pandas as pd



def AverageRead(readpath,initial_i,initial_i_tw,td,tw):
    fileread=open(readpath)
    readfile=csv.reader(fileread)
    read=0
    for i in readfile:
        if int(i[0])+int(i[1])/1000000>=initial_i and int(i[0])+int(i[1])/1000000<initial_i_tw:
            read=read+int(i[3])
    fileread.close()
    return read/tw
  
def AverageWrite(writepath,initial_i,initial_i_tw,td,tw):
    filewrite=open(writepath)
    writefile=csv.reader(filewrite)
    write=0
    for i in writefile:
        if int(i[0])+int(i[1])/1000000>=initial_i and int(i[0])+int(i[1])/1000000<initial_i_tw:
            write=write+int(i[3])
    filewrite.close()
    return write/tw
  
    
def VarianceWrite(writepath,initial_i,initial_i_tw,td,tw):
    file=pd.read_csv(writepath).values
    variance=[]
    for i in file:
        if int(i[0])+int(i[1])/1000000>=initial_i and int(i[0])+int(i[1])/1000000<initial_i_tw:
            
            variance.append(int(i[2]))
    
    if len(variance)==0:
        mean=0
        return 0
    elif len(variance)==1:
        mean=sum(variance)/len(variance)
        return 0
    else:
        mean=sum(variance)/len(variance)
        return sum((np.array(variance)-mean)**2)/(len(variance)-1)
    
def VarianceRead(readpath,initial_i,initial_i_tw,td,tw):
    file=pd.read_csv(readpath).values
    variance=[]
    
    for i in file:
        if (int(i[0])+(int(i[1])/1000000))>=initial_i and (int(i[0])+(int(i[1])/1000000))<initial_i_tw:
            variance.append(int(i[2]))
        
    if len(variance)==0:
        mean=0
        return 0
    elif len(variance)==1:
        mean=sum(variance)/len(variance)
        return 0
    else:
        mean=sum(variance)/len(variance)
        return sum((np.array(variance)-mean)**2)/(len(variance)-1)
            


def AverageShannonEntropy(writepath,initial_i,initial_i_tw,td,tw):
    filewrite=open(writepath)
    writefile=csv.reader(filewrite)
    shannon=0
    N=0
    for i in writefile:
        if int(i[0])+int(i[1])/1000000>=initial_i and int(i[0])+int(i[1])/1000000<initial_i_tw:
            shannon=shannon+float(i[4])
            N=N+1
    filewrite.close()
    if N==0:
        return 0
    else:
        return shannon/N




def Vector(td,tw,readpath,writepath):
    fileread=open(readpath)
    readfile=csv.reader(fileread)
    for i in readfile:
        initial=int(i[0])+(int(i[1])/1000000)
        break
    fileread.close()
    filewrite=open(writepath)
    writefile=csv.reader(filewrite)
    for j in writefile:
        copy_initial=int(j[0])+(int(j[1])/1000000)
        break
    filewrite.close()
    initial=min(initial,copy_initial)
    X=[]
    for i in range(td-tw+1):
        print("For window",(i,i+tw))
        if initial+i+tw>initial+td:
            break
        else:
            X.append((AverageWrite(writepath, initial+i, initial+i+tw, td, tw),
                      AverageRead(readpath, initial+i, initial+i+tw, td, tw),
                      VarianceWrite(writepath, initial+i, initial+i+tw, td, tw),VarianceRead(readpath, initial+i, initial+i+tw, td, tw),
                      AverageShannonEntropy(writepath, initial+i, initial+i+tw, td, tw)))
    return X
        






