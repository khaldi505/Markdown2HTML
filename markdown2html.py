#!/usr/bin/python3

"""
a script that markdown
a text file to html
"""
import sys
from os import path as path
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

    else:
        f_i = open(File_in, "r")
        content = f_i.read()
        f_i.close()
        content = content.split("\n")
        counter = 0
        line = ""
        result = ""
        while counter < len(content):
            if str("#") in content[counter]:
                Heading_weight = content[counter].count('#')
                content[counter] = content[counter].split("#")
                if counter < len(content) - 1:
                    result += "<h{}>".format(Heading_weight) + \
                        content[counter][Heading_weight] + \
                        "</h{}>".format(Heading_weight) + "\n"
                else:
                    result += "<h{}>".format(Heading_weight) + \
                        content[counter][Heading_weight] + \
                        "</h{}>".format(Heading_weight)

            counter += 1
        f_o = open(File_out, "w")
        f_o.write(str(result))
        f_o.close()
        exit(0)
