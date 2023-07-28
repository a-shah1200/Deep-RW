# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 01:24:32 2023

@author: Asfahan
"""

import requests
from vector import *
import pandas as pd

dic={0: (0.0, 19750144.0),
 1: (0.0, 16580659.2),
 2: (0.0, 1.4756593983777554e+16),
 3: (0.0, 9674702136419698.0),
 4: (0.0, 0.9943700936801816)}


def normalize(df,dic):
    for i in range(5):
        df[i]=(df[i]-dic[i][0])/(dic[i][1]-dic[i][0])
    return df

def get_input_csv(read,write,dic):
    X=Vector(30,10,read,write)
    df=pd.DataFrame(X)
    df_new=normalize(df,dic)
    x=df_new.values
    return x

def make_json(x):
    df_json=pd.DataFrame(x.T,["col1","col2","col3","col4","col5"])
    json = df_json.to_json()
    return json



read_file_path=""  # Path for read file
write_file_path="" # Path for write file
link="" # API link. API link can be generated by running api.py file and copying the hosted url.

j=make_json(get_input_csv(read_file_path,write_file_path,dic))
temp=requests.post(link,json=j)

name_class={0:"AESCrypt", 1:"Cerber", 2:"Cerber-largefiles", 3:"Cerber-w10dirs", 4:"Darkside", 5:"Darkside-largefiles", 6:"Darkside-w10dirs",
     7:"Excel", 8:"Firefox", 9:"GandCrab4", 10:"GandCrab4-largefiles", 11:"GandCrab4-w10dirs",
     12:"Ryuk",13:"Ryuk-largefiles",14:"Ryuk-w10dirs",15:"SDelete",16:"Sodinokibi",17:"Sodinokibi-largefiles",18:"Sodinokibi-w10dirs",
     19:"TeslaCrypt",20:"TeslaCrypt-largefiles",21:"TeslaCrypt-w10dirs",22:"WannaCry",
     23:"WannaCry-largefiles",24:"WannaCry-w10dirs",25:"Zip"}


ans=int(temp.json()["Prediction"])
if ans in [0,25,7,8,15]:
    print("Benign",name_class[ans])
else:
    print("Ransomware",name_class[ans])