# -*- coding: utf-8 -*-
"""
Created on Wed May 17 13:00:26 2023

@author: danie
"""


import Charge_Density_Code_Functions
import pandas as pd



out_name = input('Enter ADF output filename: ')     # identify input xyz file
fin_name = input('Enter filename: ')                # name parsed excel file
out_file = f"X:/{out_name}"                         # finds out_name (when file path specified in full)
fin_file = f"X:/{fin_name}"                         # saves fin_name in specified location

MDCq_list = Charge_Density_Code_Functions.MDCq_finder(out_file)            # takes ams output file, separates lines of interest and returns a list of Atom Number designations with their MDC-q value

Charge_Density_Code_Functions.Charge_Calculator(MDCq_list)                 # takes MDC-q values and calculates mean and standard deviation values           


indx = [1]
df = pd.DataFrame(MDCq_list, index = indx)


df.to_excel(f"X:/{fin_name}.xlsx", index = False)      # returns parsed excel file with MDC-q values easily accessible


