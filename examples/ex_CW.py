import unittest
import pytlwall
import pandas as pd

read_cfg = pytlwall.CfgIo('ex_CW/ex_CW.cfg')
mywall = read_cfg.read_pytlwall()
mywall.calc_ZLong()
mywall.calc_ZTrans()

# save all the data in a dataframe
savedir = 'ex_CW/output/'
data = {'f': mywall.f,
        'ZLong real': mywall.ZLong.real, 'ZLong imag': mywall.ZLong.imag,
        'ZTrans real': mywall.ZTrans.real, 'ZTrans imag': mywall.ZTrans.imag}
df = pd.DataFrame(data)
df.to_excel(savedir + 'output.xlsx')

# plot the impedances
savedir = 'ex_CW/img/'
savename = 'ZLong.png'
title = 'Longitudinal impedance'
my_plot = pytlwall.PlotUtil()
my_plot.plot_Z_vs_f_simple(mywall.f, mywall.ZLong, 'L', title,
                           savedir, savename,
                           xscale='log', yscale='log')

savename = 'ZTrans.png'
title = 'Transversal impedance'
my_plot = pytlwall.PlotUtil()
my_plot.plot_Z_vs_f_simple(mywall.f, mywall.ZTrans, 'T', title,
                           savedir, savename,
                           xscale='log', yscale='log')
