# -*- coding: utf-8 -*-
"""
Created on Sat Apr 05 14:32:59 2014

@author: Administrator
"""

import numpy as np

def predict_link(train):
    sim = np.dot(train, train)
    return sim
    
