import unittest
import pytlwall
import pandas as pd
import numpy as np

read_cfg = pytlwall.CfgIo('ex_CW/ex_CW.cfg')
mywall = read_cfg.read_pytlwall()
mywall.calc_ZLong()
mywall.calc_ZTrans()

# comparing data
compare_long = 'benchmark/ZlongWLHCvvNEGCu2layers18p4mm_some_element.dat'
f_compL = np.array([])
ZLongRe_comp = np.array([])
ZLongIm_comp = np.array([])

fd = open(compare_long)
fd.readline()
for line in fd.readlines():
    f, ZLRe, ZLIm = line.split()
    f_compL = np.append(f_compL, float(f))
    ZLongRe_comp = np.append(ZLongRe_comp, float(ZLRe))
    ZLongIm_comp = np.append(ZLongIm_comp, float(ZLIm))
fd.close()

compare_trans = 'benchmark/ZtransdipWLHCvvNEGCu2layers18p4mm_some_element.dat'
f_compT = np.array([])
ZTransRe_comp = np.array([])
ZTransIm_comp = np.array([])

fd = open(compare_trans)
fd.readline()
fd.readline()
for line in fd.readlines():
    f, ZLRe, ZLIm = line.split()
    f_compT = np.append(f_compT, float(f))
    ZTransRe_comp = np.append(ZTransRe_comp, float(ZLRe))
    ZTransIm_comp = np.append(ZTransIm_comp, float(ZLIm))
fd.close()


# plot the impedances
savedir = 'ex_CW/img/'
savename = 'ZLongCompare.png'
title = 'Longitudinal impedance'
ZLong = mywall.ZLong + mywall.ZLongISC
list_f = [mywall.f, mywall.f, f_compL, f_compL]
list_Z = [ZLong.real, ZLong.imag, ZLongRe_comp, ZLongIm_comp]
label = ['new real', 'new imag', 'old real', 'old imag']
my_plot = pytlwall.PlotUtil()
my_plot.plot_Z_vs_f_simple_single_compare(list_f, list_Z, label, 'L', title,
                           savedir, savename
                           ,
                           xscale='log', yscale='log')

savedir = 'ex_lowbeta/img/'
savename = 'ZTransCompare.png'
title = 'Transversal impedance'
ZTrans = mywall.ZTrans + mywall.ZTransISC
list_f = [mywall.f, mywall.f, f_compT, f_compT]
list_Z = [ZTrans.real, ZTrans.imag, ZTransRe_comp, ZTransIm_comp]
label = ['new real', 'new imag', 'old real', 'old imag']
my_plot = pytlwall.PlotUtil()
my_plot.plot_Z_vs_f_simple_single_compare(list_f, list_Z, label, 'L', title,
                           savedir, savename,
                           xscale='log', yscale='log')

# ~ print(f_comp)
import matplotlib.pyplot as plt
# ~ plt.plot(mywall.f, ZLong.real, label='new')
# ~ plt.plot(f_comp, ZLongRe_comp, label='old')
# ~ plt.xscale('log')
# ~ plt.yscale('log')
# ~ plt.legend()
plt.show()
