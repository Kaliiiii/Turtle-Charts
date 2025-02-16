"""
File name: constants_globals.py
Author: Kalista Hamad
Created: 15 Feb 2025
Description: This file holds all values that are used for the bar and line graphs for this project.
             It is also used in setting the measurements for the canvas.
             These value could be constants, but are scalable to match different data sets.
"""
#NOTE : While these values are constant, they depend on your data set
#       and what size you want the graph to be. You can expierament with all of 
#       these values to get the best look for your data set.

#Constants for line graph and bar graph
X_LEN = 6
Y_MAX = 300

#Constants for scatter graph
DATA_POINTS = 25
SP_X_MAX = 10
SP_Y_MAX = 100

#Constants for whisker graph
DATA_POINTS = 50

GRAPH_HEIGHT = 300            # Current value is 300
GRAPH_WIDTH = 300             # Current value is 300

CANVAS_WIDTH = GRAPH_HEIGHT+100              # Current value is 400
CANVAS_HEIGHT = GRAPH_HEIGHT+100             # Current value is 400

HOME_X = -150
HOME_Y = -150

TITLE_Y = HOME_Y + GRAPH_HEIGHT + 15

LABEL_FONT = ("Arial", 14)
TITLE_FONT = ("Arial", 20)                      # Based on preference and ideal look

