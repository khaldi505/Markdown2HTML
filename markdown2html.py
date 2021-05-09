#!/usr/bin/python3

"""
a script that markdown
a text file to HTML file,
i.e a "# heading" to "<h1> heading</h1>".
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

    def Headings(Pharse):
        """
            a function that converts a phrase with a
            "#" into an html header element.
        """
        Heading_weight = Pharse.count("#")
        Pharse = Pharse.split("#")
        return("<h{}>{}</h{}>\n".format(
            Heading_weight, Pharse[Heading_weight], Heading_weight))

    def lists(Pharse, list_type):
        """
            a function that converts a phrase with a
            "-" into an html list element.
        """
        Pharse = Pharse.split(list_type)
        return("<li>{}</li>\n".format(Pharse[1]))

    f_i = open(File_in, "r")
    content = f_i.read()
    list_type = {"type": "", "tag": ""}
    f_i.close()
    content = content.split("\n")
    counter = 0
    result = ""
    U_list_items = sum(x.count('-') for x in content)
    O_list_items = sum(x.count('*') for x in content)
    created_items = 0
    temp_content = content

    while counter < len(temp_content):
        if str("#") in temp_content[counter]:
            result += Headings(temp_content[counter])

        """checking if there's a list in this phrase"""
        if str("-") in temp_content[counter] \
                or str("*") in temp_content[counter]:
            """ list type ? """
            if str("-") in temp_content[counter]:
                list_type["tag"] = "ul"
                list_type["type"] = "-"
            if str("*") in temp_content[counter]:
                list_type["tag"] = "ol"
                list_type["type"] = "*"
            if not str("<{}>\n".format(list_type["tag"])) \
                    in temp_content and created_items == 0:
                result += "<{}>\n".format(list_type["tag"])
            result += lists(temp_content[counter], list_type["type"])
            created_items += 1
            try:
                if not list_type['type'] in temp_content[counter + 1]:
                    result += "</{}>\n".format(list_type["tag"])
                    created_items = 0
                    U_list_items -= created_items
            except IndexError:
                pass

        if created_items == U_list_items:
            if not str("</{}>\n".format(list_type["tag"])) in result:
                result += "</{}>\n".format(list_type["tag"])
                created_items = 0
        counter += 1

    """
        write the result content to the output file and exit
    """
    f_o = open(File_out, "w")
    f_o.write(str(result))
    f_o.close()
    exit(0)
