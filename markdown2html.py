#!/usr/bin/python3
"""
a script markdown2html.py that takes an argument 2 strings:
First argument is the name of the Markdown file
Second argument is the output file name
"""
from sys import argv

if len(argv) <= 2:
    sys.stderr.write("Usage: ./markdown2html.py README.md README.html")
    exit(1)


File_name = argv[1]
Out_File = argv[2]

try:
    f = open(File_name, 'r')
except FileNotFoundError:
    print("Missing " + File_name)
    exit(1)

else:
    exit(0)
