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
             
    def overwrite_ssc(self, ssc_key, value, table = False, add = False):
       """ Creates and/or writes to the *.ssc File to change the solver steering
           parameters. It needs the "ssc_key" as an input string that one can get
           from the templates in AVL FIRE WM. The value is usually a number""" 
       
       # Determing path of the *.ssf File 
       ssc_file_path =  self.proj_dir + "/Calculation/" + self.name +"/" + self.name + ".ssc"
       
       # Check, if there is already a File in the folder
       self.report("Writing ssc_key: {a} with value {b}".format(a=ssc_key, b=value), err = False)
       if not os.path.isfile(ssc_file_path):
           a = open(ssc_file_path, 'w+')
           a.close()
          
       # Check if a table, additional argument or constant value has to be written 
       # Currently only constant values are supported
       if table:
           pref = 'set-table'
       elif add:
           pref = 'add'
       else:
           pref = 'set-const'
       
       # Open file for reading and check if the "ssc_key" is already written. 
       # If yes - Append new line and then close file
       # If no - write new line and then close file
       a = open(ssc_file_path, 'r')
       lines_in = a.readlines()
       a.close()
       
       lines_out = []
       
       Found = False
       
       for line in lines_in:
           if line.find(ssc_key) != -1:
               lines_out.append('{p} {a} {b}\n'.format(a = ssc_key, b = value, p = pref))
               Found = True
           else:
               lines_out.append(line)
               
       if not Found:
           lines_out.append('{p} {a} {b}\n'.format(a = ssc_key, b = value, p = pref))
                
       a = open(ssc_file_path, 'a')
        
       for line in lines_out:
           a.write(line)
            
       a.close()     
       
    
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
        