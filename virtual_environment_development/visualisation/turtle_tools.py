def number_partition(numbers_range=(-50,50), partitions_number=10, label_l=False):  # Number partition done 
    v = partitions_number
    bin_list = [] # containning bins of numbers to put into [(starting, ending)...]
    starting_num = numbers_range[0]

    # partition calculations 
    partition_total = (numbers_range[1] - numbers_range[0])
    division = (partition_total / partitions_number)  # Division number

    not_done = True
    i = numbers_range[0] # bin initiator - loop terminator
    bin_element_list = []
    lable_list = [i,i+division]
    while not_done:
      bin_element = (i,i+division)
      i = bin_element[1]
      bin_element_list.append(bin_element)

      if len(bin_element_list) > 1:
         lable_list.append(bin_element[1])

      if (i == numbers_range[1]):
         if label_l:
            return lable_list
         return bin_element_list

def teleport(position, handle):
   t = handle
   t.penup()
   t.goto(position)
   t.pendown()

