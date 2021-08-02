from pyspedas import omni
import datetime as dt 
from pytplot import tplot


def main():
    data = omni.data(trange = ['2015-10-16/00:00:00', '2015-10-17/00:00:00'], 
                     datatype = '1min', level='hro2', suffix='', get_support_data=False, 
                     varformat=None, varnames=[], downloadonly=False, notplot=False, 
                     no_update=False, time_clip=True)
        
    run_time  = dt.datetime(2015, 1, 1)
    fname = run_time.strftime('/Users/hossep1/Downloads/%Y_OMNI_5m_with_TS05_variables.dat')
    out_vars = read_W(fname)
    out_vars[run_time]

def read_W(filename):
    with open(filename,'r') as f:
        text = f.readlines()
        time = dt.datetime.strptime(text[0][:14],'%Y %j %H %M')
        var = [float(entry) for entry in text[0].split()]
        w_params = var[-6:]
        breakpoint()
    out_vars[time] = w_params
    return out_vars
    
if __name__ == '__main__':
    main()

""""
# from the terminal 
text
text[0]
text[0].split()
[float(entry) for entry in text[0].split()]
text[0][:14]
dt.datetime.strptime(text[0][:14],'%Y %j %H %M')
time = dt.datetime.strptime(text[0][:14],'%Y %j %H %M')
print(time)
var = [float(entry) for entry in text[0].split()]
var[-6:]
""""
    
"""
# Lookup table
year = 
time = dt.datetime(year,1,1)+dt.timedelta(days=day)+dt.timedelta(minutes=min)
strptime()
st,strptime(short_string, %y %m %d %H %M)

# From date and time
t1 = dt.datetime(2016,1,2,3,4,5)  # year month day hour min sec
t0 = dt.datetime(1970,1,1)   # start of epoch
ut = (t1-t0).total_seconds()
psi = geopack.recalc(ut)

x0gsm,y0gsm,z0gsm = [4.2,3.0,-1.4]

#x0gsm = 9.2
#y0gsm = 5.0
#z0gsm = -2.4 

dirn = 1
rlim = 10
r0 = 1
parmod = [0, 0, 0, 0, 0, 0, 0]
exname = 't04'
inname = 'igrf'
geopack
out = geopack.trace(x0gsm,y0gsm,z0gsm,dirn)#parmod, exname, inname)
out
"""