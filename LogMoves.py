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
    
    def save(self,path="",name=""):
        npF = np.array(self.features)
        npL = np.array(self.labels)
        np.save(npF,path+name+"_features.npy")
        np.save(npL,path+name+"_labels.npy")
        self.features = []
        self.labels = []
        