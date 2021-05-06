#!/usr/bin/python3
"""
a script that markdown
a text file to html
"""
import sys
import os.path as path
from sys import argv as argv

if __name__ == "__main__":
    if len(argv) != 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        exit(1)

File_in = argv[1]
File_out = argv[2]

if not path.exists(File_in):
    sys.stderr.write("Missing {}\n".format(File_in))
    exit(1)
exit(0)
