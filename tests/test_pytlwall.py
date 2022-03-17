import unittest
import pytlwall
import pytlwall.txt_util as txt
import pytlwall.plot_util as plot


class TestPyTlWall(unittest.TestCase):
    def test_onelayer_circ(self):
        print('\nTesting one layer circular relativ')
        read_cfg = pytlwall.CfgIo('input/test001.cfg')
        # plot all save all
        mywall = read_cfg.read_pytlwall()
        mywall.calc_ZLong()
        mywall.calc_ZTrans()
        savedir = 'output/test001/'
        savename = 'ZLong.txt'
        label = 'Longitudinal'
        txt.save_ZLong(savedir, savename, mywall.f, mywall.ZLong, label)
        savename = 'ZTrans.txt'
        label = 'Transversal'
        txt.save_ZTrans(savedir, savename, mywall.f, mywall.ZTrans, label)
        savedir = 'output/test001/img/'
        savename = 'ZLong.png'
        imped_type = "L"
        title = 'Longitudinal impedance'
        plot.plot_Z_vs_f_simple(mywall.f, mywall.ZLong,  imped_type, title,
                                savedir, savename, xscale='log', yscale='log')
        savename = 'ZTransReal.png'
        imped_type = "T"
        list_Z = [mywall.ZDipX.real, mywall.ZDipY.real, mywall.ZQuadX.real,
                  mywall.ZQuadY.real]
        title = 'Transverse impedance Real'
        list_label = ['Dipolar X', 'Dipolar Y', 'Quadrupolar X',
                      'Quadrupolar Y']
        plot.plot_list_Z_vs_f(mywall.f, list_Z, list_label, 'T', title,
                              savedir, savename, 'log', 'symlog')
        savename = 'ZTransImag.png'
        list_Z = [mywall.ZDipX.imag, mywall.ZDipY.imag, mywall.ZQuadX.imag,
                  mywall.ZQuadY.imag]
        list_label = ['Dipolar X', 'Dipolar Y', 'Quadrupolar X',
                      'Quadrupolar Y']
        title = 'Transverse impedance Imaginary Part'
        plot.plot_list_Z_vs_f(mywall.f, list_Z, list_label, 'T', title,
                              savedir, savename, 'log', 'symlog')

    def test_onelayer_circSurf(self):
        print('\nTesting one layer circular relativ surface impedance')
        read_cfg = pytlwall.CfgIo('input/test001.cfg')
        # plot all save all
        mywall = read_cfg.read_pytlwall()
        ZLongSurf = mywall.ZLongSurf
        ZTransSurf = mywall.ZTransSurf
        savedir = 'output/test001/'
        savename = 'ZLongSurf.txt'
        label = 'Longitudinal'
        txt.save_ZLong(savedir, savename, mywall.f, ZLongSurf, label)
        savename = 'ZTransSurf.txt'
        label = 'Transversal'
        txt.save_ZTrans(savedir, savename, mywall.f, ZTransSurf, label)
        savedir = 'output/test001/img/'
        savename = 'ZLongSurf.png'
        imped_type = "L"
        title = 'Longitudinal impedance'
        plot.plot_Z_vs_f_simple(mywall.f, ZLongSurf, imped_type, title,
                                savedir, savename, xscale='log', yscale='log')
        savename = 'ZTransSurf.png'
        imped_type = "T"
        plot.plot_Z_vs_f_simple(mywall.f, ZTransSurf, imped_type, title,
                                savedir, savename, xscale='log', yscale='log')

    def test_onelayer_circSurf(self):
        print('\nTesting one layer circular relativ surface impedance')
        read_cfg = pytlwall.CfgIo('input/test001.cfg')
        # plot all save all
        mywall = read_cfg.read_pytlwall()
        ZLongSurf = mywall.ZLongSurf
        ZTransSurf = mywall.ZTransSurf
        savedir = 'output/test001/'
        savename = 'ZLongSurf.txt'
        label = 'Longitudinal'
        txt.save_ZLong(savedir, savename, mywall.f, ZLongSurf, label)
        savename = 'ZTransSurf.txt'
        label = 'Transversal'
        txt.save_ZTrans(savedir, savename, mywall.f, ZTransSurf, label)
        savedir = 'output/test001/img/'
        savename = 'ZLongSurf.png'
        imped_type = "L"
        title = 'Longitudinal impedance'
        plot.plot_Z_vs_f_simple(mywall.f, ZLongSurf, imped_type, title,
                                savedir, savename, xscale='log', yscale='log')
        savename = 'ZTransSurf.png'
        imped_type = "T"
        plot.plot_Z_vs_f_simple(mywall.f, ZTransSurf, imped_type, title,
                                savedir, savename, xscale='log', yscale='log')


if __name__ == '__main__':
    unittest.main()
