# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 12:04:50 2017

Main script for the AutoSleepScorer

@author: Simon Kern, sikern[ett]uos.de
"""
import os

import numpy as np
import argparse

from sleepscorer import Scorer


    
    
    #    cnn = 'C:/Users/Simon/dropbox/Uni/Masterthesis/AutoSleepScorerDev/weights/1207LSTM moreL2cnn3adam_filter_morel2_4_0.861-0.774'
#    rnn = 'C:/Users/Simon/dropbox/Uni/Masterthesis/AutoSleepScorerDev/weights/1207LSTM moreL2fc1_4_0.895-0.825'
directory = 'C:/Users/mayan/Documents/AutoSleepScorer-master'
for file in os.listdir(directory):
    if file.endswith('PSG.edf'):
        scorer = Scorer([file], hypnograms=True)
        scorer.run()
    # elif file.endswith('Hypnogram.edf'):
    #     AccuracyCalc([file])
      
    
