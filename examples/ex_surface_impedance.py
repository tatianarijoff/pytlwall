import pytlwall
import pandas as pd

read_cfg = pytlwall.CfgIo('ex_surface_impedance/ex_surface_impedance.cfg')
mywall = read_cfg.read_pytlwall()
mywall.calc_ZLong()
mywall.calc_ZTrans()

# save all the data in a dataframe
savedir = 'ex_surface_impedance/output/'
data = {'f': mywall.f,
        'ZLong real': mywall.ZLong.real,
        'ZLong imag': mywall.ZLong.imag,
        'ZTrans real': mywall.ZTrans.real,
        'ZTrans imag': mywall.ZTrans.imag,
        'ZLong Equivalent Surface real': mywall.ZLongSurf.real,
        'ZLong Equivalent Surface imag': mywall.ZLongSurf.imag,
        'ZTrans Equivalent Surface real': mywall.ZTransSurf.real,
        'ZTrans Equivalent Surface imag': mywall.ZTransSurf.imag}
df = pd.DataFrame(data)
df.to_excel(savedir + 'output.xlsx')

# plot the impedances
savedir = 'ex_surface_impedance/img/'
savename = 'ZLongSurf.png'
title = 'Eq. Long. Surface imp.'

my_plot = pytlwall.PlotUtil()
my_plot.plot_Z_vs_f_simple(mywall.f, mywall.ZLongSurf, 'S', title,
                           savedir, savename,
                           xscale='log', yscale='log')

savename = 'ZTrans.png'
title = 'Eq. Trans. Surface imp.'

my_plot = pytlwall.PlotUtil()
my_plot.plot_Z_vs_f_simple(mywall.f, mywall.ZTransSurf, 'S', title,
                           savedir, savename,
                           xscale='log', yscale='log')
