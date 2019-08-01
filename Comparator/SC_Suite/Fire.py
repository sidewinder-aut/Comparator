#!/usr/bin/python

import SC_Suite, os
#import pandas as pd

SC = SC_Suite

class Fire(SC.Reporter):
    
    def __init__(self, parent, name):
        
        # Getting attributes from initial call
        self.parent = parent
        self.name = name
        
        # Getting attributes from parent
        self.proj_dir = parent.proj_dir
             
    def run_case(self, num_procs):
        import os,time
        #Checking relevant files and folders for the simulation to run
        self.report("---------- Starting fire case checks ----------", err = False)
        if self.check_fire_project():
             self.report("---------- Fire project case checks finished ----------\n", err = False)    
        else:
             self.report("Fire project checks not successfull - Aborting script now")
             self.exit()    
        
        self.report("---------- Assembling commandline ----------", err = False)
        self.command = SC.Fire_cmd(self, "fire", num_procs, self.proj_dir, self.fpr_file, self.name)
        self.report("---------- Assembling commandline finished ----------\n", err = False)
        
        self.report("---------- Starting Fire Simulation at {a} ----------".format(a= time.strftime('%d. %B %Y %H:%M')))
        os.system("".join(self.command.cmd))
         #ommandline = "fire_cmd -no_exe -fire -" + os.getcwd()
         #self.report("Current commandline: {a}".format(a = commandline))
         
         
    def check_fire_project(self):
              
        # Check if there is a project file and if there is only one project file
        fpr_counter = len([f for f in os.listdir(self.proj_dir) 
                     if f.endswith('.fpr') and os.path.isfile(os.path.join(self.proj_dir, f))])
        fpr_filename = [f for f in os.listdir(self.proj_dir) if f.endswith('.fpr')]
        self.fpr_file = fpr_filename[0]
        
        if (fpr_counter == 1):
            self.report("Fire project file: {a} found".format(a=fpr_filename[0], err = False))
        else:
            self.report(" No or more than one *.fpr file found in {b}".format(b = self.proj_dir, err=True))
            self.report("Without a valid number (=1) of project files, the simulation cannot be run", err=False)
            return False
        
        #Check if there is a case folder 
        simulation_folderpath = self.proj_dir + "/Calculation/" + self.name +"/"
        self.report("Casefolderpath: {a}".format(a = simulation_folderpath))
        
        if os.path.exists(simulation_folderpath):
             self.report("Folder: {a} found in {b}".format(a = self.name, b = (self.proj_dir + "/Calculation/"),err=False))
        else:
             self.report("No folder: {a} found in {b}".format(a = self.name, b = (self.proj_dir + "/Calculation/"), err=True))
             self.report("Without a valid casefolderpath, the simulation cannot be run", err=False)
             return False
         
        # Check if there is a *.ssf file in the Case directory
        ssf_counter = len([f for f in os.listdir(simulation_folderpath) 
                     if f.endswith('.ssf') and os.path.isfile(os.path.join(simulation_folderpath, f))])
        ssf_filename = [f for f in os.listdir(simulation_folderpath) if f.endswith('.ssf')]
    
        if (ssf_counter >= 1):
            self.report("Solver steering file: {a} found".format(a=ssf_filename[0], err = False))
        else:
            self.report("No *.ssf file found in {b}".format(b = simulation_folderpath, err=True))
            self.report("Without a ssf file, the simulation cannot be run - Aborting script", err=False)
            return False            

        # Check if there is a *.dat file in the Case directory
        dat_counter = len([f for f in os.listdir(simulation_folderpath) 
                     if f.endswith('.dat') and os.path.isfile(os.path.join(simulation_folderpath, f))])
        dat_filename = [f for f in os.listdir(simulation_folderpath) if f.endswith('.dat')]
    
        if (dat_counter >= 1):
            self.report("dat file: {a} found".format(a=dat_filename[0], err = False))
        else:
            self.report("No *.dat file found in {b}".format(b = simulation_folderpath, err=True))
            self.report("Without a dat file, the simulation cannot be run", err=False)
            return False                
            
        return True
        