"""
File name: main.py
Author: Kalista Hamad
Created: 10 Feb 2025
Description:
"""

import tkinter as tk
import turtle
import line_graph, bar_graph, scatter_graph, whisker_graph
from constants_globals import *
import sample_data


def main():
    # Create the main Tkinter window
    window = tk.Tk()
    window.title("Turtle Graphs")

    top = tk.Frame(window)
    top_right = tk.Frame(window)
    top_left = tk.Frame(window)
    bottom_right = tk.Frame(window)
    bottom_left = tk.Frame(window)

    top.grid(row=0, column=0, columnspan=2)
    top_right.grid(row=1, column=1)
    top_left.grid(row=1, column=0)
    bottom_right.grid(row=2, column=1)
    bottom_left.grid(row=2, column=0)

    window_title = tk.Label(top, text="Turtle Graphs", font=TITLE_FONT)
    window_title.pack(side = tk.TOP)
    description_label = tk.Label(top, text="Add later", font=LABEL_FONT)
    description_label.pack(side = tk.TOP)

    # Canvas for line graph
    canvas1 = tk.Canvas(top_left, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
    canvas1.pack(side=tk.LEFT)
    turtle1 = turtle.RawTurtle(canvas1)

    # Canvas for scatter graph
    canvas2 = tk.Canvas(top_right, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
    canvas2.pack(side=tk.LEFT)
    turtle2 = turtle.RawTurtle(canvas2) 

    # Canvas for bar graph
    canvas3 = tk.Canvas(bottom_left, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
    canvas3.pack(side=tk.LEFT)
    turtle3 = turtle.RawTurtle(canvas3)

    # Canvas for whisker graph
    canvas4 = tk.Canvas(bottom_right, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
    canvas4.pack(side=tk.LEFT)
    turtle4 = turtle.RawTurtle(canvas4)

    ##Defining sample data##
    s_data, s_labels = sample_data.sales_per_month_data()
    q_data = sample_data.quiz_data()

    line_graph.line_graph(s_labels, s_data, turtle1)
    scatter_graph.scatter_graph(q_data, turtle2)


    window.mainloop()

if __name__ == "__main__":
    main()