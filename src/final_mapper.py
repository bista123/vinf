#!/usr/bin/env python
"""final_mapper.py"""

import sys
import re

pattern = None

for line in sys.stdin:

    line = line.strip()

    pattern = re.match(r"^(.+)\t(.*)$", line)

    if pattern:
        print(pattern.group(1) + '\t' + pattern.group(2))
