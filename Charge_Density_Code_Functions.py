# -*- coding: utf-8 -*-
"""
Created on Wed May 17 12:50:37 2023

@author: danie
"""

import statistics as stat


def MDCq_finder(in_file):                                                                   # takes ams output file, separates lines of interest and returns a list of lines with unecessary syntax removed
    
    l_count = 0
    MDCq_line = 2
   
    MDCq_list = []
    MDCq_Refined_List = {}
    output_dict = {}
    
    with open(in_file, 'r') as file_object:
        output_list = file_object.readlines()                                               # read file as lines in a list
        output_list = [x.strip() for x in output_list]                                      # removes '/n'          
            
    for line in output_list:
        if line != 'Atom    Level:     MDC-m        MDC-d        MDC-q':
            l_count += 1
            output_dict[l_count] = line                                                     # assigns line numbers
        else:
            MDCq_line += l_count                                                            # notes line number of interest
            l_count += 1
            output_dict[l_count] = line
            
    

    
    while output_dict[MDCq_line] != '------------------------------------------------':
        MDCq_line += 1
        MDCq_list += [f"{output_dict[MDCq_line]}"]                                          # stores lines in MDCq_line until condition reached
        
    
    MDCq_list.remove('------------------------------------------------')
    MDCq_list.remove('')                                                                    # removes unecessary lines


    for line in MDCq_list:                                                                  # tidying up of lines, removing syntax and spaces
        
        num = line[42:]
        
        com_num = num.strip(',')
        spa_num = com_num.replace(' ','')
        dun_num = float(spa_num)
        
        
        MDCq_Refined_List[line[:10]] = dun_num                                              # adds tidied lines to MDCq_Refined_List with Atom Number designation


    
    return(MDCq_Refined_List)                                                               
    
    


def Charge_Calculator(Charge_List):
    
    Total_Charge = 0
    Total_Mean_Atomic_Charge = 0
    Standard_Deviation_Atomic_Charge = 0
    Oxygen_Only_Mean_Atomic_Charge = 0
    Oxygen_Only_Standard_Deviation_Atomic_Charge = 0
    Countercation_Only_Mean_Atomic_Charge = 0
    Countercation_Only_Standard_Deviation_Atomic_Charge = 0
    
    Heteroatom_List = ['Al', 'As', 'B', 'Bi', 'Br', 'Cl', 'Co', 'Fe', 'Ga', 'Ge', 'I', 'In', 'Mo', 'P', 'Pt', 'S', 'Sb', 'Se', 'Si', 'Sn', 'Te', 'U', 'V', 'Xe']
    Countercation_List = ['Be', 'Ca', 'K', 'Li', 'Mg', 'Na', 'Rb']
    
    Oxygen_Only_List = []
    Tungsten_Only_List = []
    Heteroatom_Only_List = []
    Countercation_Only_List = []
    Empty = []

        



    
    Total_Charge = sum(Charge_List.values())                                                # simply returns total MDC-q charge across all atoms, should be identical to overall molecular charge
    Total_Mean_Atomic_Charge = stat.mean(Charge_List.values())                              # returns mean atomic MDC-q charge
    Standard_Deviation_Atomic_Charge = stat.stdev(Charge_List.values())                     # returns standard deviation of MDC-q charge across all atoms in the molecules
    
    for k in Charge_List.keys():                                                            # separates atoms into elemental groups
        #print(k)
        if 'O' in k:
            #print(Charge_List[k])
            Oxygen_Only_List.append(Charge_List[k])
        elif 'W' in k:
            Tungsten_Only_List.append(Charge_List[k])
        else:
            for X in Heteroatom_List:
                if X in k:
                    Heteroatom_Only_List.append(Charge_List[k])
                else:
                    for C in Countercation_List:
                        if C in k:
                            Countercation_Only_List.append(Charge_List[k])
            

    Oxygen_Only_Mean_Atomic_Charge = stat.mean(Oxygen_Only_List)                                # returns mean MDC-q charge across all oxygen atoms
    Oxygen_Only_Standard_Deviation_Atomic_Charge = stat.stdev(Oxygen_Only_List)                 # returns standard deviation in MDC-q charge across all oxygen atoms
    
    Tungsten_Only_Mean_Atomic_Charge = stat.mean(Tungsten_Only_List)                            # returns mean MDC-q charge across all tungsten atoms
    Tungsten_Only_Standard_Deviation_Atomic_Charge = stat.stdev(Tungsten_Only_List)             # returns standard deviation in MDC-q charge across all tungsten atoms
    
    if len(Heteroatom_Only_List) > 1:
        Heteroatom_Only_Mean_Atomic_Charge = stat.mean(Heteroatom_Only_List)                    # if heteroatoms are present, returns mean MDC-q charge across all heteroatoms
        Heteroatom_Only_Standard_Deviation_Atomic_Charge = stat.stdev(Heteroatom_Only_List)     # if heteroatoms are present, returns standard deviation MDC-q charge across all heteroatoms
    else:
        Heteroatom_Only_Standard_Deviation_Atomic_Charge = 0
    

    
    
    print(f'Total Charge: {round(Total_Charge, 3)}')
    print(f'Total Mean Atomic Charge: {round(Total_Mean_Atomic_Charge, 3)}')
    print(f'Total Standard Deviation Atomic Charge: {round(Standard_Deviation_Atomic_Charge, 3)}')
    
    print(f'Oxygen Only Mean Atomic Charge: {round(Oxygen_Only_Mean_Atomic_Charge, 3)}')
    print(f'Oxygen Only Standard Deviation Atomic Charge: {round(Oxygen_Only_Standard_Deviation_Atomic_Charge, 3)}')
    
    print(f'Tungsten Only Mean Atomic Charge: {round(Tungsten_Only_Mean_Atomic_Charge, 3)}')
    print(f'Tungsten Only Standard Deviation Atomic Charge: {round(Tungsten_Only_Standard_Deviation_Atomic_Charge, 3)}')
    
    if len(Heteroatom_Only_List) > 1:
        print(f'Heteroatom Only Mean Atomic Charge: {round(Heteroatom_Only_Mean_Atomic_Charge, 3)}')
        print(f'Heteroatom Only Standard Deviation Atomic Charge: {round(Heteroatom_Only_Standard_Deviation_Atomic_Charge, 3)}')
    
    if Countercation_Only_List != Empty:                        
        Countercation_Only_Mean_Atomic_Charge = stat.mean(Countercation_Only_List)                                                          # if countercations are present, returns mean MDC-q charge across all cations
        Countercation_Only_Standard_Deviation_Atomic_Charge = stat.stdev(Countercation_Only_List)                                           # if countercations are present, returns standard deviation MDC-q charge across all cations
        print(f'Countercation Only Mean Atomic Charge: {round(Countercation_Only_Mean_Atomic_Charge, 3)}')
        print(f'Countercation Only Standard Deviation Atomic Charge: {round(Countercation_Only_Standard_Deviation_Atomic_Charge, 3)}')
    
    
    return(Total_Charge, Total_Mean_Atomic_Charge, Standard_Deviation_Atomic_Charge, Oxygen_Only_Mean_Atomic_Charge, Oxygen_Only_Standard_Deviation_Atomic_Charge, Tungsten_Only_Mean_Atomic_Charge, Heteroatom_Only_Mean_Atomic_Charge, Tungsten_Only_Standard_Deviation_Atomic_Charge,Heteroatom_Only_Standard_Deviation_Atomic_Charge, Countercation_Only_Mean_Atomic_Charge, Countercation_Only_Standard_Deviation_Atomic_Charge)

    
