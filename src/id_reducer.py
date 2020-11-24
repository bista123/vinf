#!/usr/bin/env python
"""id_reducer.py"""

import sys
import re

pattern = None
current_id = None

for line in sys.stdin:

    line = line.strip()

    pattern = re.match(r"^(.+)\t(.*)$", line)

    if pattern is not None:
        if pattern.group(1) == current_id:
            print(" " + pattern.group(2))
        else:
            print(pattern.group(1) + '\t' + "ID: " + pattern.group(2))
        current_id = pattern.group(1)
