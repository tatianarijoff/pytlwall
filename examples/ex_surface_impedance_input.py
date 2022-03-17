import pandas as pd
import pytlwall
import pytlwall.plot_util as plot
import pytlwall.txt_util as txt

read_cfg = pytlwall.CfgIo('ex_surface_impedance_input/ex_surface_impedance_input.cfg')
mywall = read_cfg.read_pytlwall()
filename = 'ex_surface_impedance_input/surface_impedance_input.txt'
new_f, new_KZ = txt.read_surface_impedance_txt(filename, skipped_rows=1)
mywall.chamber.layers[0].set_surf_imped(new_f, new_KZ)

mywall.calc_ZLong()
mywall.calc_ZTrans()

# save all the data in a dataframe
savedir = 'ex_surface_impedance_input/output/'
data = {'f': mywall.f,
        'ZLong real': mywall.ZLong.real,
        'ZLong imag': mywall.ZLong.imag,
        'ZTrans real': mywall.ZTrans.real,
        'ZTrans imag': mywall.ZTrans.imag,
        }
df = pd.DataFrame(data)
df.to_excel(savedir + 'output.xlsx')

# plot the impedances
savedir = 'ex_surface_impedance_input/img/'
savename = 'ZLong.png'
title = 'Long. impedance'
plot.plot_Z_vs_f_simple(mywall.f, mywall.ZLong, 'S', title,
                        savedir, savename,
                        xscale='log', yscale='log')

savename = 'ZTrans.png'
title = 'Trans. impedance'
plot.plot_Z_vs_f_simple(mywall.f, mywall.ZTrans, 'S', title,
                        savedir, savename,
                        xscale='log', yscale='log')
