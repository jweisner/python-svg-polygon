#!/usr/bin/env python3
"""
Adapted from https://stackoverflow.com/a/65851533
The input SVG must be flattened/combined into single node/path first.
Recommended to optimize the SVG first with SVGO or Inkscape's Save As Optimized SVG.
First two columns are the starting coordinates and the second ones are the ending ones.
"""

from xml.dom import minidom
from svg.path import parse_path

doc = minidom.parse('dragonfly.svg')
for ipath, path in enumerate(doc.getElementsByTagName('path')):
    d = path.getAttribute('d')
    parsed = parse_path(d)
    for obj in parsed:
        print(f"{round(obj.start.real)}, {round(obj.start.imag)}, {round(obj.end.real)}, {round(obj.end.imag)}")
doc.unlink()