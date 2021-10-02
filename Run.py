# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 12:41:57 2021

@author: vedhs
"""
import Game
import UI
import LogMoves
import AIPlay
import numpy as np
#Init
ui = UI.UI()
game = Game.Game()
logger = LogMoves.LogMoves()
easyAI = AIPlay.AI('model/easy.h5')
hardAI = AIPlay.AI('model/hard.h5')

isTraining = False
isAI = ''

#Update the initial status
if game.turn:
    ui.setStatus('X\'s turn')
else:
    ui.setStatus('O\'s turn')
    
#On tile click
def tileClicked(x,y):
    
    #Select the tile at x,y
    res = game.select(x, y)
    ui.setStatus(res)
    
    #If result is x/o i.e a tile is selected
    if res=='x' or res=='o':
        
        #Showing status as per x or o
        if res=='x':
            ui.drawXO(y, x, 'x')
            ui.setStatus('X selected')
        else:
            ui.drawXO(y, x, 'o')
            ui.setStatus('O selcted')
            
        #Logging the state
        logger.log(game.isX, game.isO, x, y)
        
        #Checking win status
        if game.checkWin() == '-':            
            checkTurn()
        else:
            if game.checkWin() == 'x':
                ui.setStatus("You won, click retry to play again")
            else:
                ui.setStatus("Draw, click retry to play again")
    
#on train clicked
def trainClicked():
    #Switch istraining bool
    global isTraining    
    isTraining = not isTraining
    checkTurn()

#on save logs clicked
def saveClicked():
    n,a,b = logger.save(name=ui.saveName.get("1.0", "end-1c")) 
    ui.setStatus("Saved "+str(n)+" plays in "+a+" and "+b)
    
#on easy ai clicked
def easyAIClicked():
    global isAI,isTraining
    isAI='easy'
    isTraining = False
    ui.setStatus("Easy AI playing")
    
#on hard ai clicked
def hardAIClicked():
    global isAI,isTraining
    isAI='hard'
    isTraining = False
    ui.setStatus("Hard AI playing")
    
#Reset all
def retryClicked():
    game.reset()
    ui.reset()
    checkTurn()
        
def checkTurn():
    #check new value of the bool
    if isTraining:
        ui.setStatus("Training mode ON")
        if not game.turn:
            #Playing random
            x,y = game.playRandom()
            ui.drawXO(y, x, 'o')
            
            #Checking win status
            if game.checkWin() == 'o':
                ui.setStatus("You lost, click retry to play again")
            if game.checkWin() == 'd':
                ui.setStatus("Draw, click retry to play again")
    elif isAI == 'easy' or isAI == 'hard':
        if not game.turn:
            #Playing random
            res = None
            if isAI == 'easy':
                res = easyAI.predict(game.isX, game.isO)
            else:
                res = hardAI.predict(game.isX, game.isO)
            res = res.reshape((3,3))
            res = np.fliplr(np.array(np.unravel_index(np.argsort(res, axis=None), res.shape)))
            x,y = game.playPriority(res)
            ui.drawXO(y, x, 'o')
            
            #Checking win status
            if game.checkWin() == 'o':
                ui.setStatus("You lost, click retry to play again")
            if game.checkWin() == 'd':
                ui.setStatus("Draw, click retry to play again")
    else:
        ui.setStatus("Training mode OFF")

#Re defining functions
ui.tileClicked = tileClicked
ui.trainClicked = trainClicked
ui.retryClicked = retryClicked
ui.saveClicked = saveClicked
ui.easyAIClicked = easyAIClicked
ui.hardAIClicked = hardAIClicked


#Mainloop on the end
ui.mainloop()