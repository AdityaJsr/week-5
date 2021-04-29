  
"""
title - This is a Python script for on-premise reducer in Hadoop.
author name - Aditya Kumar
creation time - 29 February 2021
modified time - 30 April 2021

"""

import sys
import collections

counter = collections.Counter()

for line in sys.stdin:
    word, count = line.strip().split("\t", 1)

    counter[word] += int(count)

for x in counter.most_common(9999):
    print(x[0],"\t",x[1])
