#!/usr/bin/python3
"""
a script that will take a markdown file as input, read from
the file and create another file
with the same content of the first markdown file
"""
from sys import argv

if len(argv) <= 2:
    print("Usage: ./markdown2html.py README.md README.html")
    exit(1)


File_name = argv[1]
Out_File = argv[2]

try:
    f = open(File_name, 'r')
except FileNotFoundError:
    print("Missing " + File_name)
    exit(1)
else:
    f = open(Out_File, 'w')
    exit(0)
