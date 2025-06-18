'''
Making visualisation tool with usage of turtle
 making plots of dataset

input : points 
ouput : plot
'''
import turtle as tl
from turtle_tools import *

# Turtle global settings and variables 
turtle = tl.Turtle()
turtle.pencolor('white')
window = tl.Screen()
window.bgcolor('black')
window.screensize(600,600)
turtle.hideturtle()

class Graph:
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
      
      nums = number_partition(ranges,20,label_l=True)
      axis_seed = {'x_axis':(ranges[0],origin[1]),'y_axis':(origin[0],ranges[0])}
      
      for position in axis_seed:
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
      t = self.t
      teleport(points_list[0])
      t.pencolor('green')
      for _ in points_list[1:]:
         t.goto(_)
         t.pencolor('yellow')
         t.dot()
         t.pencolor('green')
         


g = Graph()
g.grid_plot(shifting_constant=200)
window.exitonclick()