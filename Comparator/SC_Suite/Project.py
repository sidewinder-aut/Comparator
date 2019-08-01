#!/usr/bin/python

import SC_Suite, os
SC = SC_Suite

class Project(SC.Reporter):
    
    def __init__(self, name):
        self.name = name
        self.proj_dir = os.getcwd()
        
        
        
        
        #results_folderpath = os.getcwd() + "/" + self.foldername
        
        
        # Check if specified results folder can be found - If not, CFD_compare stops
        #if os.path.exists(results_folderpath):
             #self.report("Folder: {a} found in {b}".format(a = self.foldername, b = os.getcwd()),err=False)
        #else:
             #self.report("No folder: {a} found in {b}".format(a = self.foldername, b = os.getcwd()), err=True)
             #self.exit_script()
