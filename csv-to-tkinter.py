#!/usr/bin/env

import tkinter as tk
import csv

root = tk.Tk()
root.geometry('500x500')
root.title('Dragonfly')
canvas = tk.Canvas(root, width=500, height=500, bg='white')
canvas.pack(anchor=tk.CENTER, expand=True)

with open('dragonfly_xy.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",", quoting=csv.QUOTE_NONNUMERIC)
    polygon_paths = [(row[0], row[1], row[2], row[3]) for row in csvreader]

canvas.create_polygon(*polygon_paths, width=4, fill='green')
root.mainloop()