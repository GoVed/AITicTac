# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 13:47:50 2021

@author: vedhs
"""
import numpy as np
import copy

class LogMoves:
    features = []
    labels = []
    
    def log(self,isX,isO,newx,newy):
        isX=copy.deepcopy(isX)
        isO=copy.deepcopy(isO)
        select = [[False]*3 for _ in range(3)]
        select[newx][newy]=True        
        isX[newx][newy]=False        
        self.features.append([isX,isO])
        self.labels.append(select)
    
    def save(self,name=""):
        npF = np.array(self.features)
        npL = np.array(self.labels)
        
        np.save(name+"_features.npy",npF)
        np.save(name+"_labels.npy",npL)
        
        n = len(self.features)
        
        self.features = []
        self.labels = []
        
        return n,name+"_features.npy",name+"_labels.npy"
        