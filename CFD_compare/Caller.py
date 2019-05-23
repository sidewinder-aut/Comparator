#!/usr/bin/python
import CFD_comp
CO = CFD_comp



result_folder = "2D_Results"


Comp_1 = CO.Comp("Comparison Object", result_folder)
Comp_1.fire_1 = CO.FIRE(Comp_1,"FIRE Object")