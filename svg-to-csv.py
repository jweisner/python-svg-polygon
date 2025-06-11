from xml.dom import minidom
from svg.path import parse_path
import csv

drawing = minidom.parse('dragonfly.svg')

for objnum,path in enumerate(drawing.getElementsByTagName('path')):
    with open(f"dragonfly-{objnum}.csv", 'w', newline='') as partfile:
        partwriter = csv.writer(partfile, 
                        delimiter=' ',
                        quoting=csv.QUOTE_MINIMAL)
        polygon = parse_path(path.getAttribute('d'))
        for seg in polygon:
            x1 = seg.start.real
            y1 = seg.start.imag
            x2 = seg.end.real
            y2 = seg.end.imag
            partwriter.writerow([x1,y1,x2,y2])
    