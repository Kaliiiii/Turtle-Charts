import tkinter 
import turtle
from collections import defaultdict
import helpers
from constants_globals import *

TITLE_TEXT = "Scatter Plot"
SPACE_BETWEEN_Y_LABELS = 20  
DOT_SIZE = 5

#TO DO: implement decimal values for hours
def scatter_graph(d_list, turtle_obj):
    helpers.build_graph(turtle_obj)

    turtle_obj.penup()
    turtle_obj.goto(HOME_X, TITLE_Y)
    turtle_obj.write(TITLE_TEXT, font= TITLE_FONT)

    label_space = GRAPH_WIDTH / len(d_list)

    x_list = []
    y_list = []
    for val in d_list:
        x_list.append(val[0])
        y_list.append(val[1])
    
    labels = list(range(0, SP_X_MAX))
    helpers.write_x_labels(turtle_obj, labels, False, label_space)
    helpers.write_y_labels(turtle_obj, SPACE_BETWEEN_Y_LABELS, SP_Y_MAX, 3)

    turtle_obj.penup()
    turtle_obj.goto(HOME_X, HOME_Y)
    pos_diff = label_space
    for x in labels:
        if x in x_list:
            ind = x_list.index(x)
            turtle_obj.goto(HOME_X+pos_diff, HOME_Y+y_list[ind])
            turtle_obj.dot(DOT_SIZE)
        pos_diff += label_space
    
    turtle_obj.hideturtle()