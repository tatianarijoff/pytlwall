import unittest
import pytlwall
import pytlwall.plot_util as plot


class TestPlot(unittest.TestCase):
    def test_longitudinal_output(self):
        print('\nTesting longitudinal simple plot, scale log')
        read_cfg = pytlwall.CfgIo('input/one_layer.cfg')
        mywall = read_cfg.read_pytlwall()
        mywall.calc_ZLong()
        savedir = 'output/one_layer/img/'
        savename = 'ZLong.png'
        imped_type = "L"
        title = 'Longitudinal impedance'
        plot.plot_Z_vs_f_simple(mywall.f, mywall.ZLong,  imped_type, title,
                                savedir, savename, xscale='log', yscale='log')

    def test_transverse_output(self):
        print('\nTesting transverse  plot, scale log, symlog')
        read_cfg = pytlwall.CfgIo('input/one_layer.cfg')
        mywall = read_cfg.read_pytlwall()
        mywall.calc_ZTrans()
        savedir = 'output/one_layer/img/'
        savename = 'ZTransReal.png'
        imped_type = "T"
        f = mywall.f
        list_Z = [mywall.ZDipX.real, mywall.ZDipY.real, mywall.ZQuadX.real,
                  mywall.ZQuadY.real]
        title = 'Transverse impedance Real'
        list_label = ['Dipolar X', 'Dipolar Y', 'Quadrupolar X',
                      'Quadrupolar Y']
        plot.plot_list_Z_vs_f(f, list_Z, list_label, 'T', title,
                              savedir, savename, 'log', 'symlog')
        savename = 'ZTransImag.png'
        list_Z = [mywall.ZDipX.imag, mywall.ZDipY.imag, mywall.ZQuadX.imag,
                  mywall.ZQuadY.imag]
        list_label = ['Dipolar X', 'Dipolar Y', 'Quadrupolar X',
                      'Quadrupolar Y']
        title = 'Transverse impedance Imaginary Part'
        plot.plot_list_Z_vs_f(f, list_Z, list_label, 'T', title,
                              savedir, savename, 'log', 'symlog')


if __name__ == '__main__':
    unittest.main()
