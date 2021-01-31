import unittest
import numpy as np
from matplotlib import pyplot as plt
import pytlwall


class TestPlot(unittest.TestCase):
    def test_longitudinal_output(self):
        print('\nTesting longitudinal simple plot, scale log')
        read_cfg = pytlwall.CfgIo('input/one_layer.cfg')
        mywall = read_cfg.read_pytlwall()
        savedir = 'output/img/one_layer'
        savename = 'ZLong.png'
        imped_type = "L"
        title = 'Longitudinal impedance'
        my_plot = pytlwall.PlotUtil()
        my_plot.plot_Z_vs_f_simple(mywall.f, mywall.ZLong,  imped_type, title,
                                   savedir, savename,
                                   xscale='log', yscale='log')


if __name__ == '__main__':
    unittest.main()
