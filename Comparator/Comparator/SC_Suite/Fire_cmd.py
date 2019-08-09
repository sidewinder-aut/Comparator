#!/usr/bin/python

import SC_Suite

SC = SC_Suite

class Fire_cmd(SC.Reporter):
    
    def __init__(self, parent, solver_vers, CPU_count, project_dir, fpr_file, case_name):
       
        #Initialisation of needed parameters to build the commandline for FIRE simulation
        self.name = "Fire run command"
        self.cmd = ["fire_cmd"]
        self.parent = parent
        self.solver = solver_vers
        self.cpu_count = CPU_count
        self.project_dir = project_dir
        self.fpr_file = fpr_file
        self.case_name = case_name
        
        self.report("{a} initialised".format(a=self.name))
        
        
        # Building commandline for start of FIRE simulation
        self.cmd.append(" -project_dir="+self.project_dir)
        self.cmd.append(" -solver_vers="+self.solver)
        self.cmd.append(" -project="+self.fpr_file)
        self.cmd.append(" -case=" + self.case_name)
        self.cmd.append(" -mpi")
        self.cmd.append(" -cpu=" + str(self.cpu_count))
        self.cmd.append(" -merge_initial_ssc")
        

        