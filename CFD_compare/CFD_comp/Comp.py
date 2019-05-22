#!/usr/bin/python

import CFD_comp 
CO = CFD_comp

class ASDF(CO.Reporter):
    
    def __init__(self, name):
        self.name = name
        print("Spawn")