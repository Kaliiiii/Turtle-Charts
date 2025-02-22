"""
File name: line_graph.py
Author: Kalista Hamad
Created: 10 Feb 2025
Description: This file contains the code to draw a line graph using Turtle.
"""

import turtle
import helpers
from constants_globals import *

TITLE_TEXT = "Line Graph"
SPACE_BETWEEN_Y_LABELS = 20  

def line_graph(x_list, y_list, turtle_obj):
    helpers.build_graph(turtle_obj)
    helpers.write_title(turtle_obj, TITLE_TEXT)
    label_space = GRAPH_WIDTH / len(x_list)
    helpers.write_x_labels(turtle_obj, x_list, label_space)
    helpers.write_y_labels(turtle_obj, SPACE_BETWEEN_Y_LABELS, Y_MAX, 1)

    turtle_obj.goto(HOME_X, HOME_Y)
    turtle_obj.pendown()
    pos_diff = 0
    for val in y_list:
        turtle_obj.goto(HOME_X+pos_diff, HOME_Y+val)
        pos_diff += label_space
    
    turtle_obj.hideturtle()


        
