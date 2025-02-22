import turtle
from constants_globals import *

def build_graph(turtle_obj):
    turtle_obj.penup()
    turtle_obj.goto(HOME_X, HOME_Y)
    turtle_obj.pendown()
    turtle_obj.goto(HOME_X, HOME_Y+GRAPH_HEIGHT)
    turtle_obj.goto(HOME_X, HOME_Y)
    turtle_obj.goto(HOME_X+GRAPH_WIDTH, HOME_Y)
    turtle_obj.goto(HOME_X, HOME_Y)


def write_x_labels(turtle_obj, x_list, x_space):
    turtle_obj.goto(HOME_X, HOME_Y-20)
    pos_diff = x_space
    align = "left"
    for val in x_list:
        turtle_obj.write(val, align=align, font= LABEL_FONT)
        turtle_obj.goto(HOME_X+pos_diff, HOME_Y-20)
        pos_diff += x_space

def write_y_labels(turtle_obj, y_space, max_y, scale):
    for val in range(0, max_y, y_space):
        turtle_obj.goto(HOME_X-20, HOME_Y+val)
        turtle_obj.write(str(int(val/scale)), align="center", font= LABEL_FONT)

def write_title(turtle_obj, text):
    turtle_obj.penup()
    turtle_obj.goto(HOME_X, TITLE_Y)
    turtle_obj.write(text, font= TITLE_FONT)