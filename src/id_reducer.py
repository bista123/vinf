#!/usr/bin/env python
"""id_reducer.py"""

import sys
import re

pattern = None
current_id = None
current_values = "ID: "

# iterate through lines of mapper output
for line in sys.stdin:

    line = line.strip()

    # parse input by tabulator
    pattern = re.match(r"^(.+)\t(.*)$", line)

    if pattern is not None:
        # continue with the same page, this should not happen for ID
        if pattern.group(1) == current_id:
            current_values = current_values + " " + str(pattern.group(2))
        # new page was found
        else:
            # if the page is first
            if current_id is None:
                current_values = "ID: " + str(pattern.group(2))
            else:
                # print ID for page and initialize new page
                print(str(current_id) + '\t' + current_values)
                current_values = "ID: " + str(pattern.group(2))
        current_id = pattern.group(1)

# print last page
print(str(current_id) + '\t' + current_values)
