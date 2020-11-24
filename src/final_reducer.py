#!/usr/bin/env python
"""final_reducer.py"""

import sys
import re
import json


class Page:

    def __init__(self, name):
        self.name = name
        self.ID = ""
        self.Label = ""
        self.Categories = []
        self.Links = []

    def save_file(self):

        y = json.dumps(self.__dict__, ensure_ascii=False)
        print(y)


if __name__ == '__main__':

    pattern = None
    current_id = None
    current_values = "  "

    for line in sys.stdin:

        line = line.strip()
        pattern = re.match(r"^(.+)\t(.*)$", line)

        if pattern is not None:
            if pattern.group(1) == current_id:
                if "ID:" in pattern.group(2):
                    obj.ID = pattern.group(2)[pattern.group(2).index(' ')+1:]
                if "Label:" in pattern.group(2):
                    obj.Label = pattern.group(2)[pattern.group(2).index(' ')+1:]
                if "Kategorie:" in pattern.group(2):
                    obj.Categories = pattern.group(2)[pattern.group(2).index(' ')+1:]
                if "Linky:" in pattern.group(2):
                    obj.Links = pattern.group(2)[pattern.group(2).index(' ')+1:]
            else:
                if current_id is None:
                    obj = Page(pattern.group(1))
                    if "ID:" in pattern.group(2):
                        obj.ID = pattern.group(2)[pattern.group(2).index(' ')+1:]
                    if "Label:" in pattern.group(2):
                        obj.Label = pattern.group(2)[pattern.group(2).index(' ')+1:]
                    if "Kategorie:" in pattern.group(2):
                        obj.Categories = pattern.group(2)[pattern.group(2).index(' ')+1:]
                    if "Linky:" in pattern.group(2):
                        obj.Links = pattern.group(2)[pattern.group(2).index(' ')+1:]
                else:
                    obj.save_file()
                    obj = Page(pattern.group(1))
                    if "ID:" in pattern.group(2):
                        obj.ID = pattern.group(2)[pattern.group(2).index(' ')+1:]
                    if "Label:" in pattern.group(2):
                        obj.Label = pattern.group(2)[pattern.group(2).index(' ')+1:]
                    if "Kategorie:" in pattern.group(2):
                        obj.Categories = pattern.group(2)[pattern.group(2).index(' ')+1:]
                    if "Linky:" in pattern.group(2):
                        obj.Links = pattern.group(2)[pattern.group(2).index(' ')+1:]
            current_id = pattern.group(1)
