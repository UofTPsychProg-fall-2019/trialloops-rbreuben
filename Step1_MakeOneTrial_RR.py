#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build a trial loop Step 1
Use this template script to present one trial with your desired structure
@author: katherineduncan
"""
#%% Required set up 
# this imports everything you might need and opens a full screen window
# when you are developing your script you might want to make a smaller window 
# so that you can still see your console 
import numpy as np
import pandas as pd
import os, sys
from psychopy import visual, core, event, gui, logging

# open a white full screen window
myWin = visual.Window(fullscr=True, allowGUI=False, color='grey', unit='height') 

Instructions = visual.TextStim(myWin, text='Press any key to continue')
Instructions.draw()
myWin.flip()

words = open("wordlist.csv")

myStimulus = visual.TextStim(myWin, text='')

for word in words:
    myStimulus.setText(word)
    event.waitKeys()
    myStimulus.draw()
    myWin.flip()



#%% Required clean up
# this cell will make sure that your window displays for a while and then 
# closes properly

core.wait(2)
win.close()
