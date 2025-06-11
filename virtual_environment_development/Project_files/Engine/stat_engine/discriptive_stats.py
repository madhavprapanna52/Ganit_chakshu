"""
Discriptive statistics unit 
    ~ Making discriptive stats units for handling dynamic data structures 
    versetile data structure adoption for making discriptive reports 

    || use to present outputs of loged items : lt.present() ||

"""
from basic_tool import *
import csv 
import statistics


data = load_csv('synthetic_data.csv')  # loads csv file into list | Ram loading 
lt = Loging_program_report()  # Loging tool 

handle_data = Data_handle(data)  # data basic operation tool

# Discriptive statistics tool 
class Discriptive_stat():
    '''
    Making discriptive stat tool for making discriptive stats report for the dataset 
    features 
        1. Central tendency of dataset 
        2. Spread of the dataset 

        Procedure 
            Data type based computation 
            data --> datatype --> computation report 
            
    '''
    def __init__(self, data_set):
        self.data_set = data_set

    def central_tendency(self):
        '''
        Making basic computations of central tendency of dataset 
        '''
