"""
Making basic tools for projects 
    featuring 
    - Data handle tool
"""
import csv

# MVP tool - Very basic 

# Basic functions 
def load_csv(file_name):
    data = []
    f = open(file_name, 'r')
    r = csv.reader(f)
    
    for data_row in r:
        data.append(data_row)
    return data

def index_iteration(index, big_list):
    copy = []
    for row in big_list:
        copy.append(row[index])
    return copy


class Data_handle():
    '''
    Handles basic data handleing frameworks for lists 
    making use of cordinate systems 
    '''
    def __init__(self,data_set):
        self.data_list = data_set # list 
    
    def row(self, row_name):
        '''
        returns copy of the row required for operation through header name
        input : row_name
            exception ~ Having multiple same identical names of row
        output: row copy 
        '''
        header = self.data_list[0]
        return_list = []

        not_done = True
        i = 0
        while not_done:
            if header[i] == row_name:
                data_set = index_iteration(i, self.data_list) # the row that matched
                return_list.append(data_set)  #  specific for the match
            i += 1
            if (i == len(header)):
                not_done = False


        # match labels 
        if (len(return_list) > 1):
            print('Multi match')
            return return_list
        else:
            return return_list


class Loging_program_report():
    def __init__(self):
        self.log_data_dict = {}
        self.label_list = []
    
    def inject(self,presenting_peice, label_text):
        self.label_list.append(label_text)
        self.log_data_dict[label_text] = presenting_peice
    
    def present(self):
        for label in self.label_list:
            self.out(label, self.log_data_dict[label])

    def out(self, label_text, text):
        print('_'*20)
        print(label_text)
        for i in text:
            print(i)
        print('_'*20)