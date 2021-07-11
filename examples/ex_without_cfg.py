import pytlwall
import pandas as pd
import pytlwall.plot_util as plot


# Define Beam
beam = pytlwall.Beam(betarel=0.9, test_beam_shift=0.002)

# Define Frequencies list
freq = pytlwall.Frequencies(fmin=2, fmax=8, fstep=2)

# Define Layers
layers = []
layer0 = pytlwall.Layer(layer_type='CW',
                        thick_m=0.1,
                        muinf_Hz=0.,
                        epsr=1.,
                        sigmaDC=1.e6,
                        k_Hz=float('inf'),
                        tau=0.,
                        RQ=0.,
                        boundary=False)
layers.append(layer0)
boundary = pytlwall.Layer(layer_type='V', boundary=True)
layers.append(boundary)

# Define Chamber characteristics
pipe_len_m = 1.
pipe_rad_m = 0.0184
chamber_shape = 'CIRCULAR'
betax = 1.
betay = 1.
component_name = 'newCW'

chamber = pytlwall.Chamber(pipe_len_m=pipe_len_m,
                           pipe_rad_m=pipe_rad_m,
                           chamber_shape=chamber_shape,
                           betax=betax,
                           betay=betay,
                           layers=layers,
                           component_name=component_name)

# Run TlWall
mywall = pytlwall.TlWall(chamber, beam, freq)
ZLong = mywall.ZLong
ZTrans = mywall.ZTrans
ZLongSurf = mywall.ZLongSurf
ZTransSurf = mywall.ZTransSurf

# save the data in a dataframe
savedir = 'ex_CW/output/'
data = {'f': mywall.f,
        'ZLong real': mywall.ZLong.real, 'ZLong imag': mywall.ZLong.imag,
        'ZTrans real': mywall.ZTrans.real, 'ZTrans imag': mywall.ZTrans.imag}
df = pd.DataFrame(data)
df.to_excel(savedir + 'output.xlsx')

# plot the impedances
savedir = 'ex_without_cfg/img/'
savename = 'ZLong.png'
title = 'Longitudinal impedance'
plot.plot_Z_vs_f_simple(mywall.f, mywall.ZLong, 'L', title,
                        savedir, savename,
                        xscale='log', yscale='log')

savename = 'ZTrans.png'
title = 'Transversal impedance'
plot.plot_Z_vs_f_simple(mywall.f, mywall.ZTrans, 'T', title,
                        savedir, savename,
                        xscale='log', yscale='log')
