#encoding:utf8

import sys
import pylab as pl
stock_id = sys.argv[1]

f = open('label_data/'+stock_id)

lines = f.readlines()
x = []
y = []
b_x = []
b_y = []
s_x = []
s_y = []
size = len(lines)
for idx in range(0, size):
    line = lines[idx]
    vals = line.split(',')
    close_val = float(vals[3])
    op = int(vals[len(vals)-1])
    x.append(size - idx - 1)
    y.append(close_val)
    if op == 0:
        b_x.append(size-idx-1)
        b_y.append(close_val)
    elif op == 1:
        s_x.append(size-idx-1)
        s_y.append(close_val)
print (x,y)
pl.plot(x,y)
pl.plot(b_x,b_y,'or')
pl.plot(s_x,s_y,'og')
pl.show()

