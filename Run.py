# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 12:41:57 2021

@author: vedhs
"""
import Game
import UI
import LogMoves


#Init
ui = UI.UI()
game = Game.Game()
logger = LogMoves.LogMoves()

isTraining = False


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
            
            #If in training mode
            if isTraining:
                
                #Playing random
                x,y = game.playRandom()
                ui.drawXO(y, x, 'o')
                
                #Checking win status
                if game.checkWin() == 'o':
                    ui.setStatus("You lost, click retry to play again")
                if game.checkWin() == 'd':
                    ui.setStatus("Draw, click retry to play again")
        else:
            if game.checkWin() == 'x':
                ui.setStatus("You won, click retry to play again")
            else:
                ui.setStatus("Draw, click retry to play again")
    
def trainClicked():
    
    #Switch istraining bool
    global isTraining
    print(isTraining)
    isTraining = not isTraining
    
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
    else:
        ui.setStatus("Training mode OFF")
        
#Reset all
def retryClicked():
    game.reset()
    ui.reset()
        
#Re defining functions
ui.tileClicked = tileClicked
ui.trainClicked = trainClicked
ui.retryClicked = retryClicked


#Mainloop on the end
ui.mainloop()