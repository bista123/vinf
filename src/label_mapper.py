#!/usr/bin/env python
"""label_mapper.py"""

import sys
import re

pattern = None

for line in sys.stdin:

    line = line.strip()

    pattern = re.match(r"^\<.*resource\/(.*)\> \<.*\> \"(.*)\"\@sk .", line)
    
    if pattern:
        print(pattern.group(1) + '\t' + pattern.group(2))