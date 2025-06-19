"""
Making basic tools for projects 
    featuring 
    - Data handle tool
"""
import csv
import math

# MVP tool - Very basic 

# Basic functions 
def load_csv(file_name):  # working fine 
    """
    Loads csv into list : Deadly for big data 
    TODO Making it efficient through using batch processing data flow 
    """
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


class Data_handle():  # working fine 
    '''
    Handles basic data handleing frameworks for lists 
    making use of cordinate systems 
    '''
    def __init__(self,data_set):
        self.data_list = data_set # list 
    
    def row(self, row_name):  # working fine 
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
        return return_list

class Loging_program_report():  # working fine 
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
        print(text)
        print('_'*20)

l = Loging_program_report()

def partition_list(list_input, partition_length=10):  # wprking fine -- Label edge partition
    '''
    Making percentage based division 
    Edge cases : smaller datasets 
    '''
    #todo Variable partition needed urgent 
    # (x/total)X100 = 2% | v -> variable for partition chunks
    v = partition_length  # Making variation with this
    partition_size = int((v * len(list_input)) / 100)
    i = 0
    partition_output = []
    partition_output.append(list_input[0]) # adding label separate | 2 deep down
    del list_input[0] # removing header
    
    while i <= (len(list_input)-(v+1)):
        chunk = list_input[i:v+i]  # No iterations - > error of not geting out out 
        # del list_input[:v]
        partition_output.append(chunk)
        i += v
    return partition_output

def number_partition(numbers_range=(-50,50), partitions_number=10):  # Number partition done 
    v = partitions_number
    bin_list = [] # containning bins of numbers to put into [(starting, ending)...]
    starting_num = numbers_range[0]

    # partition calculations 
    partition_total = (numbers_range[1] - numbers_range[0])
    division = (partition_total / partitions_number)  # Division number

    not_done = True
    i = -50 # bin initiator - loop terminator
    bin_element_list = []
    while not_done:
        bin_element = (i,i+division)
        i = bin_element[1]
        bin_element_list.append(bin_element)
        if (i == numbers_range[1]):
            return bin_element_list

def int_convert(str_l): # integer convertor | tested
    num_l = []
    for i in str_l[1:]:
        num_l.append(int(i))
    return num_l

def bin_frequency(bin_num, l):
    counter = 0
    for i in l:
        condition = '(bin_num[0] <= i) and (bin_num[1] >= i)'
        c1 = eval(condition)  # bin condition
        if c1:
            counter += 1
    return counter



# tools 
def freq_list(l, success_probability_want=False):
    '''
    input : partitioned list
    output : partitioned based dictionary list containning freq of elements in partitions based
    '''
    freq_list = []
    def counter_element(element, l):  # counts freq
        counter = 0
        for i in l: # iterating list
            if (element == i):
                counter += 1
        return counter
    # Binary dataset 
    if l[0] == 'b':
        total_success_probability = 0
        # index based computing for simplicity     
        for chunk in l[1:]:  # taking partitions list 
            chunk_freq_element = {} # freq dictionary
            chunk_freq_element['0'] = counter_element('0', chunk)/10
            chunk_freq_element['1'] = counter_element('1', chunk)/10  # success event

            total_success_probability += chunk_freq_element['1']
            freq_list.append(chunk_freq_element) # adding chunk freq

        if success_probability_want:
            p = (total_success_probability/10)
            return [freq_list, p]
        return freq_list
    # Categorical dataset 
    elif l[0] == 'c':
        elements_to_search = '1,2,3,4,5'.split(',')
        for chunk in l[1:]:
            chunk_freq = {}
            for elems in elements_to_search:
                chunk_freq[elems] = counter_element(elems, chunk)/10
            freq_list.append(chunk_freq)
        return freq_list
    else:
        return None

def facto(i):
    return math.factorial(i)

def factorial_simplification(expression):  # working with simple numbers 
    '''
    Simplifies factorial expression through approach of expansion and cancilation computations and normal computations
    featuring : solving factorial expressiions 
    '''
    nums = expression.split('_')  # integer it 
    n = int(nums[0])
    x = int(nums[1])
    simple_number = len(nums[0]) <= 3
    if simple_number:
        deno = (facto(x) * facto(n-x))
        if deno == 0:
            return 1  # under denominator equates zero
        ans = facto(n) / deno
        return ans
    else:
        print('Making efficient way to deal with them ')

j = factorial_simplification('20_10')

# Testing probability counter 
dataset_load = load_csv('synthetic_data.csv')
handle = Data_handle(dataset_load)

binary_d = handle.row('b')
partition = partition_list(binary_d[1])
f = freq_list(partition, True)
