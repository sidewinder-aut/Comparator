#!/usr/bin/python

import SC_Suite, time, os
SC = SC_Suite

print('\n ---------------------------------- Simulation Control Suite started at: {a} ---------------------------------- \n'.format(a = time.strftime('%d. %B %Y %H:%M')))



Proj = SC.Project("Battery HMC")
Proj.Fire = SC.Fire(Proj,"Case")

Proj.Fire.overwrite_ssc('solver.MO.COM.CM.ISD', 12347)
Proj.Fire.run_case(10)