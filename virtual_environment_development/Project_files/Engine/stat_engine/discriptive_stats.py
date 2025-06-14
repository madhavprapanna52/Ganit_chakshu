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
        self.data_set = data_set  # whole dataset into list 

    def central_tendency(self, data_list):  # working fine 
        '''
        Making basic computations of central tendency of dataset
        mean , median mode computations based on data type : 
            MVP : Only for numerical datasets for now 
        '''
        # TODO Interface for the function required 
        # Making type conversion 
        int_list = []
        for i in data_list:
            int_list.append(int(i))  # int converg
        mean = statistics.mean(int_list)
        median = statistics.median(int_list)
        mode = statistics.mode(int_list)

        del int_list
        print(f"""
        Central tendency Data report 
        MEAN OF DATA : {mean}
        MEDIAN OF DATA : {median}
        MODE OF DATA : {mode}
        """)  #TODO Make sujjester which gives best parameter to consider for the data 

    def present(self):
        """
        Making presentation for the all collums 
        iterating with row selection through dataset 
        # TODO organised data strucures flow is must in project 
        """
        # fetch collums of numericals
        numerical_data_collums = handle_data.row('n')  # data of all numerical dataset 
        boolean_data = handle_data.row('b')
        categorical_data = handle_data.row('c')
        mark = 1   # simple marking 
        for collums in numerical_data_collums: 
            print(mark)
            self.central_tendency(collums[1:])  # due to header exception
            mark += 1

