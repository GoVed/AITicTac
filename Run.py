# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 12:41:57 2021

@author: vedhs
"""
import Game
import UI

ui = UI.UI()
ui.createGrid()
ui.drawXO(0, 0, "X")
ui.drawXO(1, 0, "X")
ui.drawXO(0, 2, "O")
ui.drawXO(2, 2, "X")
ui.mainloop()