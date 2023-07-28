# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 01:24:07 2023

@author: Asfahan
"""

from flask import Flask, jsonify,request
import numpy as np
from tcn import TCN
import pandas as pd
app = Flask(__name__)
import tensorflow as tf

def reconvert(json):
    convert=pd.read_json(json)
    x=convert.values
    return x.T


     
    
@app.route("/model", methods=['POST'] )

def pred():
    json_ = request.json
    x=reconvert(json_)
    x=np.reshape(x,(-1,1,5))
    fin=tf.keras.models.load_model('model_imp_optimized.hdf5',custom_objects={'TCN': TCN})
    pred_pre=fin.predict(x)
    fin_pred=np.argmax(pred_pre,axis=1)
    ans=max(list(fin_pred),key=list(fin_pred).count)
    return jsonify({"Prediction":str(ans)})

    
