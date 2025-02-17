import tkinter 
import turtle
from collections import defaultdict
import helpers
from constants_globals import *

TITLE_TEXT = "Scatter Plot"
SPACE_BETWEEN_Y_LABELS = 20 
DOT_SIZE = 5

def scatter_graph(d_list, turtle_obj):
    helpers.build_graph(turtle_obj)

    turtle_obj.penup()
    turtle_obj.goto(HOME_X, TITLE_Y)
    turtle_obj.write(TITLE_TEXT, font= TITLE_FONT)

    dictionary_values = defaultdict(list)
    for x, y in d_list:
        if x in dictionary_values.keys():
            dictionary_values[x].append(y)
        else:
            dictionary_values[x] = [y]
    print(dictionary_values)
    print (dictionary_values.keys())

    label_space = GRAPH_WIDTH / len(dictionary_values.keys())
    labels = list(dictionary_values.keys())
    print(labels)
    labels.sort()
    print(labels)
    helpers.write_x_labels(turtle_obj, labels, False, label_space)
    helpers.write_y_labels(turtle_obj, SPACE_BETWEEN_Y_LABELS, SP_Y_MAX, 1)

    turtle_obj.penup()
    turtle_obj.goto(HOME_X, HOME_Y)
    pos_diff = label_space
    for key in labels:
        for val in dictionary_values[key]:
            turtle_obj.goto(HOME_X+pos_diff, HOME_Y+val)
            turtle_obj.dot(DOT_SIZE)
        pos_diff += label_space

    turtle_obj.hideturtle()