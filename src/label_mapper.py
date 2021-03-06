#!/usr/bin/env python
# coding=utf-8
"""label_mapper.py"""

import sys
import re

pattern = None

# iterate through lines of turtle file
for line in sys.stdin:

    line = line.strip()

    # parse page identificator and label from line with regex
    pattern = re.match(r"^\<.*resource\/(.*)\> \<.*\> \"(.*)\"\@sk .", line)
    
    if pattern:
        # filter out pages without useful data, like templates, categories or files
        if pattern.group(1).__contains__('Kategória:') or pattern.group(1).__contains__('Podkategória:') \
                or pattern.group(1).__contains__('Šablóna:') or pattern.group(1).__contains__('Šablóny:') \
                or pattern.group(1).__contains__('Súbor:') or pattern.group(1).__contains__('WP:'):
            continue
        else:
            # print tab separated output for reducer
            print(pattern.group(1) + '\t' + pattern.group(2))
    else:
        continue
