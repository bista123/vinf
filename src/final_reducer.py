#!/usr/bin/env python
"""final_reducer.py"""

import sys
import re
import json


# class Page which represents one final wiki page
class Page:

    def __init__(self):
        self.ID = ""
        self.Categories = []
        self.Links = []
        self.Label = ""

    # print json object to output
    def save_file(self):
        y = json.dumps(self.__dict__, ensure_ascii=False)
        print(y)


if __name__ == '__main__':

    pattern = None
    current_id = None
    current_values = "  "

    # iterate through mapper output by lines
    for line in sys.stdin:

        line = line.strip()
        # match tabulator
        pattern = re.match(r"^(.+)\t(.*)$", line)

        if pattern is not None:
            # continue with the same page
            if pattern.group(1) == current_id:
                # find particular page part and add value to particular object attribute
                if "ID:" in pattern.group(2):
                    obj.ID = pattern.group(2)[pattern.group(2).index(' ')+1:]
                if "Label:" in pattern.group(2):
                    obj.Label = pattern.group(2)[pattern.group(2).index(' ')+1:]
                if "Kategorie:" in pattern.group(2):
                    cats = pattern.group(2)[pattern.group(2).index(' ')+1:]
                    obj.Categories = list(cats.split(" "))
                if "Linky:" in pattern.group(2):
                    links = pattern.group(2)[pattern.group(2).index(' ')+1:]
                    obj.Links = list(links.split(" "))
            # new page was found
            else:
                # first page
                if current_id is None:
                    # create new Page object
                    obj = Page()
                    # find particular page part and add value to particular object attribute
                    if "ID:" in pattern.group(2):
                        obj.ID = pattern.group(2)[pattern.group(2).index(' ')+1:]
                    if "Label:" in pattern.group(2):
                        obj.Label = pattern.group(2)[pattern.group(2).index(' ')+1:]
                    if "Kategorie:" in pattern.group(2):
                        cats = pattern.group(2)[pattern.group(2).index(' ') + 1:]
                        obj.Categories = list(cats.split(" "))
                    if "Linky:" in pattern.group(2):
                        links = pattern.group(2)[pattern.group(2).index(' ') + 1:]
                        obj.Links = list(links.split(" "))
                else:
                    # print current page object to output
                    obj.save_file()
                    # initialize new page object
                    obj = Page()
                    # find particular page part and add value to particular object attribute
                    if "ID:" in pattern.group(2):
                        obj.ID = pattern.group(2)[pattern.group(2).index(' ')+1:]
                    if "Label:" in pattern.group(2):
                        obj.Label = pattern.group(2)[pattern.group(2).index(' ')+1:]
                    if "Kategorie:" in pattern.group(2):
                        cats = pattern.group(2)[pattern.group(2).index(' ') + 1:]
                        obj.Categories = list(cats.split(" "))
                    if "Linky:" in pattern.group(2):
                        links = pattern.group(2)[pattern.group(2).index(' ') + 1:]
                        obj.Links = list(links.split(" "))
            current_id = pattern.group(1)

# print last page to output
obj.save_file()
