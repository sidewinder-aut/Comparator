#!/usr/bin/python

import CFD_comp, os
CO = CFD_comp

class Comp(CO.Reporter):
    
    def __init__(self, name, foldername):
        self.name = name
        self.foldername = foldername
        
        
        
        
        #results_folderpath = os.getcwd() + "/" + self.foldername
        
        
        # Check if specified results folder can be found - If not, CFD_compare stops
        #if os.path.exists(results_folderpath):
             #self.report("Folder: {a} found in {b}".format(a = self.foldername, b = os.getcwd()),err=False)
        #else:
             #self.report("No folder: {a} found in {b}".format(a = self.foldername, b = os.getcwd()), err=True)
             #self.exit_script()
