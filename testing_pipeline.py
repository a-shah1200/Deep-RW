# -*- coding: utf-8 -*-
"""


@author: Asfahan
"""

import requests
from vector import *
import pandas as pd

dic={0: (0.0, 19750144.0),
 1: (0.0, 16580659.2),
 2: (0.0, 1.4756593983777554e+16),
 3: (0.0, 9674702136419698.0),
 4: (0.0, 0.9943700936801816)}   ## Normalization parameters derieved via training data


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


def make_prediction(read_file_path,write_file_path,api_link):
    json_file=make_json(get_input_csv(read_file_path,write_file_path,dic))
    api_response=requests.post(api_link,json=json_file)
    try:
       pred=int(api_response.json()["Prediction"])
       return pred
    except:
       return None


    
    


