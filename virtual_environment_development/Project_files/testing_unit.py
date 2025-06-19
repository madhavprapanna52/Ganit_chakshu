import random
import csv
'''
Testing unit 
features 
    1. Random Data generator
    2. Testing components
'''

def shuffel(l):
    len_l = len(l)
    pic = random.randint(0,len_l-1)
    label = 'b,c,n'.split(',')
    return l[pic], label[pic]

# Random Data generator
def Random_data_generator(size=50, dimensions=5):
    data_points_list = []
    ranges = [(0,1),(1,5),(-50,50)] # ranges for datasets

    for colum in range(dimensions):
        collum_data_points = []

        data_type, label_set = shuffel(ranges) # geting data , Label attached 
        collum_data_points.append(label_set)  # seting label as header 
        for data in range(size):
            d = random.randint(data_type[0],data_type[1])
            collum_data_points.append(d)
        data_points_list.append(collum_data_points)
    return data_points_list  # tested ok

# Formating output 
def format_output(data_points):
    """
    Iterations for the data for formated output and processing 
    Nested iterations 
    Iter1 - size ONE iteration
        iter-2 collum based - reset mechanism 
    """
    data_points = data_points
    collum_size = (len(data_points[0])-1)
    formated_data = []
    for i in range(0,collum_size):
        j = 0 # reset 
        row_data = []
        while j <= (len(data_points)-1):
            row_data.append(data_points[j][i])  # required element |
            j += 1
        formated_data.append(row_data)  # applying row data 
    return formated_data  # tested ok

data_set = format_output(Random_data_generator(101,10))

# Data science into file
def comunicate_file():
    data_file = open("synthetic_data.csv", 'w')
    writer = csv.writer(data_file)
    for row in data_set:
        writer.writerow(row)
    print('Data is writen')

comunicate_file()