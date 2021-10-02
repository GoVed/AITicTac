# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 17:58:27 2021

@author: vedhs
"""
from tensorflow import keras
import numpy as np

class AI:
    
    model=None
    
    def __init__(self,model):
        self.model = keras.models.load_model(model)
        
    def predict(self,isX,isO):
        x=np.array([[isO,isX]])
        x=x.reshape((x.shape[0],3,3,2))
        res = self.model.predict(x)
        print(res)
        return res