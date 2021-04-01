import sys
import collections

counter = collections.Counter()

for line in sys.stdin:
    word, count = line.strip().split("\t", 1)

    counter[word] += int(count)

for x in counter.most_common(9999):
    print(x[0],"\t",x[1])