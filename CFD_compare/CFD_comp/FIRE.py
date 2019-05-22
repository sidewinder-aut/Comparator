#!/usr/bin/python

import CFD_comp 
CO = CFD_comp

class FIRE(CO.Reporter):
    
    def __init__(self, parent, name):
        self.parent = parent
        self.name = name
        print("FIRE")