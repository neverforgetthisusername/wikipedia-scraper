"""
Created on Feb 2024
@author: Cédric EL-Dib
"""

#if __name__ == "__main__":

import json
import src.utils as utils
import src.api as api
from src.all_data import All_data


""" import & save the data """
import_file = api.load_data()

   
""" Filling de main class (All_Data) """
all_data1 = All_data(len(import_file))

number_of_countries = len(import_file)
for i in range(number_of_countries):
    number_of_leader = len(import_file[i][1])
    all_data1.assign_country(import_file[i][0])
    for j in range(number_of_leader):
        all_data1.countries[i].number_leaders = number_of_leader
        all_data1.countries[i].assign_leader(import_file[i][0], import_file[i][1][j][1],  
                                             import_file[i][1][j][2], import_file[i][1][j][3], 
                                             import_file[i][1][j][4], import_file[i][1][j][5],  
                                              import_file[i][1][j][6], import_file[i][1][j][7], 
                                             import_file[i][1][j][8], import_file[i][1][j][9])
""" Display data load """
display_file = all_data1.display()      

""" Create an export file """
all_data1.export_csv(display_file)
