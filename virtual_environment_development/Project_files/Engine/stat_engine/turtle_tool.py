import math
import random

def number_partition_g(numbers_range=(-50,50), partitions_number=10, label_l=False):  # Number partition done 
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
   print(f'position : {position}')
   t.goto(position)
   t.pendown()

def draw_bar(handle, base, height):
    try:
        t = handle
        x, y = t.position()
        base, height = float(base or 10), abs(float(height or 0))
        
        colors = ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'cyan', 'magenta']
        t.fillcolor(random.choice(colors))
        t.begin_fill()
        t.pendown()
        
        # Draw rectangle
        t.goto(x, y)
        t.goto(x + base, y)
        t.goto(x + base, y + height)
        t.goto(x, y + height)
        t.goto(x, y)
        
        t.end_fill()
        t.penup()
        t.goto(x + base, y)
        
    except Exception as e:
        print(f"draw_bar error: {e}")
        t.penup()
