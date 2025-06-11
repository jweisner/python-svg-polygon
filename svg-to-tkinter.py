from xml.dom import minidom
from svg.path import parse_path
import tkinter as tk

drawing = minidom.parse('dragonfly.svg')
svgnode = drawing.getElementsByTagName('svg')
width = svgnode[0].getAttribute('width')
height = svgnode[0].getAttribute('height')

root = tk.Tk()
root.geometry(f"{width}x{height}")
root.title('Dragonfly')
canvas = tk.Canvas(root, width=width, height=height, bg='black')
canvas.pack(anchor=tk.CENTER, expand=True)

for objnum,path in enumerate(drawing.getElementsByTagName('path')):
    polygon = parse_path(path.getAttribute('d'))
    polygon_xy = []
    for seg in polygon:
        x1 = seg.start.real
        y1 = seg.start.imag
        x2 = seg.end.real
        y2 = seg.end.imag
        polygon_xy.append([x1,y1,x2,y2])
    canvas.create_polygon(*polygon_xy, width=4, fill='green')
root.mainloop()