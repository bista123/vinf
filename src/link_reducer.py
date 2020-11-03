#!/usr/bin/env python
"""link_reducer.py"""

import sys
import re

pattern = None
current_id = None
current_values = ""

for line in sys.stdin:

    line = line.strip()

    pattern = re.match(r"^(.+)\t(.*)$", line)

    if pattern is not None:
        if pattern.group(1) == current_id:
            current_values = current_values + " " + str(pattern.group(2))
        else:
            if current_id is None:
                current_values = "" + str(pattern.group(2))
            else:
                print(str(current_id) + '\t' + current_values)
                current_values = "" + str(pattern.group(2))
        current_id = pattern.group(1)