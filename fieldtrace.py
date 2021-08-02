from pyspedas import omni
import datetime as dt 
from pytplot import tplot
import pandas


def main():
    
    cases = pandas.read_excel('EDR_Cases.xls')    
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


