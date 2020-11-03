#!/usr/bin/env python
"""label_reducer.py"""

from operator import itemgetter
import sys
import re

pattern = None
current_id = None

for line in sys.stdin:

    line = line.strip()

    pattern = re.match(r"^(.+)\t(.*)$", line)

    if pattern.group(1) == current_id:
        print(' ' + pattern.group(2))
    else:
        print(pattern.group(1) + '\t' + pattern.group(2))
    current_id = pattern.group(1)

