# -*- coding: utf-8 -*-
"""
Created on Sat Apr 05 14:57:47 2014

@author: Administrator
"""

import numpy as np

def predict_link(train, beta):
    dim = train.shape[0]
    sim = np.linalg.inv(np.eye(dim, dtype = np.float) - beta * train) - np.eye(dim, dtype = np.float)
    return sim