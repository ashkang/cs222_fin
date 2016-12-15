#!/usr/bin/env python
import numpy as np
import sys

_, name, m, n, p = sys.argv

M = np.random.rand(int(m), int(n))
N = np.random.rand(int(n), int(p))

f = open(name, 'w')
f.write('%s %s%s' % (m, n, '\n'))
f.write('%s %s%s' % (n, p, '\n'))

for i in M:
    f.write(' '.join(map(str, i)))
    f.write('\n')

for i in N:
    f.write(' '.join(map(str, i)))
    f.write('\n')

f.close
