#!/usr/bin/env python
import fileinput
import numpy as np

Nr = 0
Nc = 0
Mr = 0
Mc = 0

M = []
N = []

for pos, line in enumerate(fileinput.input()):
    line = line.strip()
    if pos == 0:
        Mr, Mc = map(int, line.split())
    elif pos == 1:
        Nr, Nc = map(int, line.split())
        assert Mc == Nr
    elif pos <= (2 + Mr - 1):
        M.append([float(i) for i in line.split()])
    else:
        N.append([float(i) for i in line.split()])

M = np.matrix(M)
N = np.matrix(N)

P = M * N
f = open('mul.numpy.out', 'w')

for i in P:
    f.write(' '.join(map(str, i)))
    f.write('\n')

f.close
