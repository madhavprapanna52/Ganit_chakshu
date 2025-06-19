'''
Making visualisation tool with usage of turtle
 making plots of dataset

input : points 
ouput : plot
'''
import math
import turtle as tl
import random
from turtle_tool import *
from inferential_statistics import *

# Turtle global settings and variables 
turtle = tl.Turtle()
turtle.pencolor('white')
window = tl.Screen()
window.bgcolor('black')
window.screensize(600,600)
turtle.hideturtle()
turtle.speed(100)

turtle.penup()
turtle.goto(0,350)
turtle.pendown
turtle.write('MINI MATPLOTLIB',align='center')
turtle.penup()

class Graph:  # working fine - Needs transformation mechanism for good visuals 
   """
   Basic graphing tool made with turtle 
   """
   def __init__(self):
      self.t = turtle  # Main turtle
      
   def grid_plot(self, shifting_constant=0, ranges=(-300,300)):
      '''
      Input x and y ranges 
      ouput : makes grid for plot and returns transformation constants

      simplicity making cartesian plane for the dataset
      '''
      t = self.t
      origin = [0,0]
      i = 0
      
      nums = number_partition_g(ranges,20,label_l=True)
      print(nums)
      axis_seed = {'x_axis':(ranges[0],origin[1]),'y_axis':(origin[0],ranges[0])}
      
      for position in axis_seed:
         print(position)
         seed_location = axis_seed[position]
         teleport(seed_location, t)
         # Making heading position 
         if (position == 'y_axis'):
            t.setheading(90)
         # making iterations based on seed locations - default is x axis 
         for label in nums:
            if (t.heading() == 0):
               position = (label,0)
            else:
               # takes account of y axis iterations 
               position = (0, label)
            t.goto(position)
            t.write(str(int(label)))

   def scatter_plot(self, points_list):
      '''
      input :points_list = [(x_axis, y_axis) ..]
      outpu :Makes scatter plot
      '''
      c = 'blue'
      dc = 'red'
      t = self.t
      teleport(points_list[0],t)
      t.pencolor(c)
      for _ in points_list[1:]:
         t.goto(_)
         t.pencolor(dc)
         t.dot(5)
         t.pencolor(c)

   def bar_graph(self,b):
      t = self.t
      for _ in b:
         
         teleport((_[0],0),t)
         h = b[_]
         h = int(math.ceil(h))
         print(h)


         draw_bar(t ,10, h)

g = Graph()
d = p.Continuous_probability_initialisation()
print(f'This is the output of the continuous dataset ouptu : {d}')
# make type conversions of the dataset 
data = d[0]
print(f'dataset : {data}')
typo_data = {}
for _ in data:
   print(f'types : {type(_)} , {_}')
   # process _ for the making it compatible for operations 
   i = _.split(',')
   n1 = (i[0][1:])
   print(f'n1 : {n1}')
   n2 = (i[1][1:-1])
   print(f'n2 : {n2}')
   n1 = float(n1)
   n2 = float(n2)
   print(f'nums : {n1}, {n2} and types {type(n1)} {type(n2)}')
   t = (n1,n2)
   typo_data[t] = data[_]

g.grid_plot()
g.bar_graph(typo_data)

# Making scatter plot demo dataset
scatter_d = []
for i in range(-50,50):
   r = random.randint(-100,100)
   p = (i*5,r)  #todo make visuals of graphing secreets
   scatter_d.append(p)
g.scatter_plot(scatter_d)

window.exitonclick()