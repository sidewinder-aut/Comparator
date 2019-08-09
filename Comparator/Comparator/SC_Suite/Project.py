#!/usr/bin/python

import SC_Suite, os
SC = SC_Suite

class Project(SC.Reporter):
    
    def __init__(self, name):
        self.name = name
        self.proj_dir = os.getcwd()
        
