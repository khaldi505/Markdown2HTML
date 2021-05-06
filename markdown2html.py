#!/usr/bin/python3
"""
a script that will take a markdown file as input, read from
the file and create another file with the same content of the first markdown file
"""
from sys import argv as argv
from sys import exit as exit
len_arguments = len(argv)
if len_arguments < 2:
    print("Usage: ./markdown2html.py README.md README.html")
    exit(1)
output_file = argv[2]
markdown_file = argv[1]
try:
    f = open(markdown_file, "r")
except FileNotFoundError as error:
    print("Missing " + markdown_file)
    exit(1)
else:
    content = f.read()
    f = open(output_file, "w")
    f.write(content)
