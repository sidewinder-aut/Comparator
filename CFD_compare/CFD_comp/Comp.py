#!/usr/bin/python

import CFD_comp, os
CO = CFD_comp

class Comp(CO.Reporter):
    
    def __init__(self, name):
        self.name = name
        
        
        results_folderpath = os.getcwd() + "/2D_Results"
        
        if os.path.exists(results_folderpath):
            self.report("2D results folder found in {a}".format(a=os.getcwd()),err=False)
        else:
            self.report("No 2D results folder found in {a}".format(a=os.getcwd()),err=True)
            self.exit_script()