#!/usr/bin/env python

import fileinput

Mlist = {}
Nlist = {}

for line in fileinput.input():
    line = line.strip()
    key, data = line.split()
    l, j, val = data.split(',')
    j = int(j)
    val = float(val)

    if l == 'M':
        if key in Mlist.keys():
            Mlist[key].append((j, val))
        else:
            Mlist[key] = [(j, val)]
    else:
        if key in Nlist.keys():
            Nlist[key].append((j, val))
        else:
            Nlist[key] = [(j, val)]

# Already sorted by Hadoop
# for key, arr in Mlist.items():
#     arr.sort(key=lambda t: t[0])
#
# for key, arr in Nlist.items():
#     arr.sort(key=lambda t: t[0])

for key, arr in Mlist.items():
    s = 0
    for i, val in enumerate(arr):
        s += val[1] * Nlist[key][i][1]

    print("%s %s" % (key, s))
