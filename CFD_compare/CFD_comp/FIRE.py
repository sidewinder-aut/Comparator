#!/usr/bin/python

import CFD_comp, os
import pandas as pd

CO = CFD_comp

class FIRE(CO.Reporter):
    
    def __init__(self, parent, name):
        self.parent = parent
        self.name = name
        self.foldername = "FIRE"

        results_folderpath = os.getcwd() + "/" + parent.foldername + "/" + self.foldername
        
        # Check if specified results folder can be found - If not, CFD_compare stops
        if os.path.exists(results_folderpath):
             self.report("Folder: {a} found in {b}".format(a = self.foldername, b = (os.getcwd() + "/" + parent.foldername),err=False))
        else:
             self.report("No older: {a} found in {b}".format(a = self.foldername, b = (os.getcwd() + "/" + parent.foldername), err=True))
             self.exit_script()
             
             
        # Import FIRE Table data using pandas
        test = pd.read_csv(results_folderpath + "/fl2_results.txt", sep='\t')
        print(test.values)