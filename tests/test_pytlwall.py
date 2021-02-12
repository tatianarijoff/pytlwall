import unittest
import pytlwall


class TestPlot(unittest.TestCase):
    def test_onelayer_circ(self):
        print('\nTesting one layer circular relativ')
        read_cfg = pytlwall.CfgIo('input/test001.cfg')
        # plot all save all
        mywall = read_cfg.read_pytlwall()
        mywall.calc_ZLong()
        mywall.calc_ZTrans()
        savedir = 'output/test001/'
        my_output = pytlwall.TxtIo()
        savename = 'ZLong.txt'
        label = 'Longitudinal'
        my_output.save_ZLong(savedir, savename, mywall.f, mywall.ZLong,
                             label)
        savename = 'ZTrans.txt'
        label = 'Transversal'
        my_output.save_ZTrans(savedir, savename, mywall.f, mywall.ZTrans,
                              label)
        savedir = 'output/test001/img/'
        savename = 'ZLong.png'
        imped_type = "L"
        title = 'Longitudinal impedance'
        my_plot = pytlwall.PlotUtil()
        my_plot.plot_Z_vs_f_simple(mywall.f, mywall.ZLong,  imped_type, title,
                                   savedir, savename,
                                   xscale='log', yscale='log')
        savename = 'ZTransReal.png'
        imped_type = "T"
        list_f = [mywall.f, mywall.f, mywall.f, mywall.f]
        print(mywall.chamber.yokoya_q)
        print(mywall.chamber.detx_yokoya_factor)
        list_Z = [mywall.ZDipX.real, mywall.ZDipY.real, mywall.ZQuadX.real,
                  mywall.ZQuadY.real]
        title = 'Transverse impedance Real'
        list_label = ['Dipolar X', 'Dipolar Y', 'Quadrupolar X',
                      'Quadrupolar Y']
        my_plot.plot_Z_vs_f_simple_single_compare(list_f, list_Z, list_label,
                                                  'T', title,
                                                  savedir, savename,
                                                  'log', 'symlog')
        savename = 'ZTransImag.png'
        list_Z = [mywall.ZDipX.imag, mywall.ZDipY.imag, mywall.ZQuadX.imag,
                  mywall.ZQuadY.imag]
        list_label = ['Dipolar X', 'Dipolar Y', 'Quadrupolar X',
                      'Quadrupolar Y']
        title = 'Transverse impedance Imaginary Part'
        my_plot.plot_Z_vs_f_simple_single_compare(list_f, list_Z, list_label,
                                                  'T', title,
                                                  savedir, savename,
                                                  'log', 'symlog')


if __name__ == '__main__':
    unittest.main()
