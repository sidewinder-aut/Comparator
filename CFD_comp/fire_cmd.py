#!/usr/bin/python

import CFD_comp

CO = CFD_comp

class fire_cmd(CO.Reporter):
    
    def __init__(self, parent, solver_vers, CPU_count, project_dir, project_name, case_name):
       
        #Initialisation of needed parameters to build the commandline for FIRE simulation
        self.name = "Fire run command"
        self.cmd = ['fire_cmd']
        self.parent = parent
        self.solver = solver_vers
        self.cpu_count = CPU_count
        self.project_dir = project_dir
        
        self.report("{a} initialised".format(a=self.name))
        
        
        
        # Building commandline for start of FIRE simulation
        self.cmd.append(" -project_dir"+self.project_dir)
        
        
        
        
        
        self.report("Commandline: {a}".format(a="".join(self.cmd)))
        