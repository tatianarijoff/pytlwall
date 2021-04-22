import pytlwall
import pandas as pd

read_cfg = pytlwall.CfgIo('ex_lowbeta/ex_lowbeta.cfg')
mywall = read_cfg.read_pytlwall()
mywall.calc_ZLong()
mywall.calc_ZTrans()

# save all the data in a dataframe
savedir = 'ex_lowbeta/output/'
data = {'f': mywall.f,
        'ZLong real': mywall.ZLong.real, 'ZLong imag': mywall.ZLong.imag,
        'ZTrans real': mywall.ZTrans.real, 'ZTrans imag': mywall.ZTrans.imag}
df = pd.DataFrame(data)
df.to_excel(savedir + 'output.xlsx')

# plot the impedances
savedir = 'ex_lowbeta/img/'
savename = 'ZLong.png'
title = 'Longitudinal impedance'
ZLong = mywall.ZLong + mywall.ZLongISC
my_plot = pytlwall.PlotUtil()
my_plot.plot_Z_vs_f_simple(mywall.f, ZLong, 'L', title,
                           savedir, savename,
                           xscale='log', yscale='log')

savename = 'ZTrans.png'
title = 'Transverse impedance'
ZTrans = mywall.ZTrans + mywall.ZTransISC
my_plot = pytlwall.PlotUtil()
my_plot.plot_Z_vs_f_simple(mywall.f, ZTrans, 'T', title,
                           savedir, savename,
                           xscale='log', yscale='log')
