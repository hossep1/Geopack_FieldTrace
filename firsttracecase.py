import numpy as np
import datetime as dt
from geopack import geopack
from geopack import t04
import trace
import pdb
import numpy as np
import matplotlib.pyplot as plt
"""
For T89
par: A model parameter. It is an integer (1-7) maps to the Kp index
| par |  1   |    2    |    3    |    4    |    5    |    6    |  7   |
| Kp  | 0,0+ | 1-,1,1+ | 2-,2,2+ | 3-,3,3+ | 4-,4,4+ | 5-,5,5+ | > 6- |
"""
# From date and time
t1 = dt.datetime(2001,1,2,3,4,5)  # year month day hour min sec
t0 = dt.datetime(1970,1,1)   # start of epoch
ut = (t1-t0).total_seconds()
ps = geopack.recalc(ut)


# Case 1
x0gsm,y0gsm,z0gsm = [6.3, 5.3, -2.9]
parmod = [5.43, -100, -0.93, 0.91, 0, 0, 0, 0, 0, 0]


dir = 1
rlim = 20
r0 = 0.02 
exname = 't04'
inname = 'igrf'
out = geopack.trace(x0gsm, y0gsm, z0gsm, dir, rlim, r0, parmod, exname, inname)



ax = plt.axes(projection='3d')
ax.plot3D(out[3], out[4], out[5], 'gray')
ax.set_xlabel('X_gsm')
ax.set_xlabel('Y_gsm')

ax.scatter(0,0,0)
ax.scatter(x0gsm,y0gsm,z0gsm)
out