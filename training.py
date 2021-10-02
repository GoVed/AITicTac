# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 17:39:25 2021

@author: vedhs
"""
from tensorflow import keras
import numpy as np


def load(name):    
    global x,y
    x=np.load(name+'_features.npy')
    y=np.load(name+'_labels.npy')
    x=x.reshape((x.shape[0],3,3,2))
    x=np.concatenate((x, np.fliplr(x)))
    x=np.concatenate((x, np.flipud(x)))
    y=np.concatenate((y, np.fliplr(y)))
    y=np.concatenate((y, np.flipud(y)))
    return x,y
    
def makeModel():
    model = keras.models.Sequential()
    model.add(keras.layers.Conv2D(128, (3,3), padding='same',input_shape=(3,3,2)))
    model.add(keras.layers.LeakyReLU(alpha=0.2))
    model.add(keras.layers.BatchNormalization(momentum=0.15, axis=-1))
    
    model.add(keras.layers.Conv2D(256, (2,2), padding='same'))
    model.add(keras.layers.LeakyReLU(alpha=0.2))
    model.add(keras.layers.BatchNormalization(momentum=0.15, axis=-1))
    
    model.add(keras.layers.Conv2D(1, (1,1),padding='same',activation='sigmoid'))
    
    return model

def train(model,epoch,x,y):
    model.compile(optimizer='adam',loss='binary_crossentropy')
    model.fit(x,y,epochs=epoch,shuffle=True)
    

x,y = load('data/hard')
model = makeModel()
train(model,1000,x,y)
model.save('model/hard.h5')
