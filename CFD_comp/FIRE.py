#!/usr/bin/python

import CFD_comp, os
#import pandas as pd

CO = CFD_comp

class FIRE(CO.Reporter):
    
    def __init__(self, parent, name):
        self.parent = parent
        self.name = name
        self.foldername = "FIRE"

        
        
        # Check if there is a calculation folder 
        simulation_folderpath = os.getcwd() + "/Calculation/" + self.name 
        self.report("Casefolderpath: {a}".format(a = simulation_folderpath))
        
        if os.path.exists(simulation_folderpath):
             self.report("Folder: {a} found in {b}".format(a = self.name, b = (os.getcwd() + "/Calculation/"),err=False))
        else:
             self.report("No folder: {a} found in {b}".format(a = self.name, b = (os.getcwd() + "/Calculation/"), err=True))
             self.report("Without a valid casefolderpath, the simulation cannot be run - Aborting script", err=False)
             self.exit_script()
             
    def run_case(self, number_of_processors):
         import os
         self.command = CO.fire_cmd(self, "fire", 10, os.getcwd(), "test.fpr", self.name)
         #ommandline = "fire_cmd -no_exe -fire -" + os.getcwd()
         #self.report("Current commandline: {a}".format(a = commandline))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #results_folderpath = os.getcwd() + "/" + parent.foldername + "/" + self.foldername
        # Check if specified results folder can be found - If not, CFD_compare stops
        #if os.path.exists(results_folderpath):
             #self.report("Folder: {a} found in {b}".format(a = self.foldername, b = (os.getcwd() + "/" + parent.foldername),err=False))
        #else:
             #self.report("No older: {a} found in {b}".format(a = self.foldername, b = (os.getcwd() + "/" + parent.foldername), err=True))
             #self.exit_script()