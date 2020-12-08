#!/usr/bin/env python
# coding=utf-8
"""link_mapper.py"""

import sys
import re

pattern = None

for line in sys.stdin:

    line = line.strip()

    pattern = re.match(r"^\<.*resource\/(.*)\> \<.*\> \<(.*)\> .", line)

    if pattern:
        if pattern.group(1).__contains__('Kategória:') or pattern.group(1).__contains__('Podkategória:') \
                or pattern.group(1).__contains__('Šablóna:') or pattern.group(1).__contains__('Šablóny:') \
                or pattern.group(1).__contains__('Súbor:') or pattern.group(1).__contains__('WP:'):
            continue
        else:
            print(pattern.group(1) + '\t' + pattern.group(2))
    else:
        continue