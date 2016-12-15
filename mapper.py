#!/usr/bin/env python

import fileinput

Nr = 0
Nc = 0
Mr = 0
Mc = 0

for pos, line in enumerate(fileinput.input()):
    line = line.strip()
    if pos == 0:
        Mr, Mc = map(int, line.split())
    elif pos == 1:
        Nr, Nc = map(int, line.split())
        assert Mc == Nr
    elif pos <= (2 + Mr - 1):
        i = pos - 2
        cols = map(float, line.split())
        for j, m in enumerate(cols):
            for k in range(0, Nc):
                print("%s,%s %s,%s,%s" % (i, k, 'M', j, m))
    else:
        j = pos - 2 - Mr
        cols = map(float, line.split())
        for k, n in enumerate(cols):
            for i in range(0, Mr):
                print("%s,%s %s,%s,%s" % (i, k, 'N', j, n))
