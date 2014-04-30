# -*- coding: utf-8 -*-

import preprocess as prep
import CN
import Jaccard
import AA
import RA
import PA
import Katz
import SimRank
import evaluation

path = 'C:/Users/Administrator/Desktop/'
fn = 'input.txt'
ratio = 0.9

def main():
    edges = prep.read_edges(path + fn)
    net = prep.build_net(edges)
    train, test = prep.divide_net(net, ratio)
    
    #CN
    sim = CN.predict_link(train)
    
    #Jaccard
    sim = Jaccard.predict_link(train)
    
    #AA
    sim = AA.predict_link(train)
    
    #RA
    sim = RA.predict_link(train)
    
    #PA
    sim = PA.predict_link(train)
    
    #Katz
    sim = Katz.predict_link(train)
    
    #SimRank
    sim = SimRank.predict_link(train)
    
    
    
    
    

if __name__ == '__main__':
    main()
        
