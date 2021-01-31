import unittest
import numpy as np
from matplotlib import pyplot as plt
import pytlwall


class TestTxtIo(unittest.TestCase):
    def test_longitudinal_output(self):
        print('\nTesting longitudinal output, text')
        read_cfg = pytlwall.CfgIo('input/one_layer.cfg')
        mywall = read_cfg.read_pytlwall()
        filedir = 'output/'
        filename = 'one_layerZLong.txt'
        label = "longitudinal impedance"
        my_output = pytlwall.TxtIo()
        my_output.save_ZLong(filedir, filename, mywall.f, mywall.ZLong, label)

    def test_transverse_output(self):
        print('\nTesting transverse output, text')
        read_cfg = pytlwall.CfgIo('input/one_layer.cfg')
        mywall = read_cfg.read_pytlwall()
        filedir = 'output/'
        filename = 'one_layerZTrans.txt'
        label = "transverse impedance"
        my_output = pytlwall.TxtIo()
        my_output.save_ZTrans(filedir, filename, mywall.f, mywall.ZTrans,
                              label)

    def test_all_transverse_output(self):
        print('\nTesting all the transverse output, text')
        read_cfg = pytlwall.CfgIo('input/one_layer.cfg')
        mywall = read_cfg.read_pytlwall()
        filedir = 'output/'
        filename = 'one_layerZAllTrans.txt'
        label = "transverse impedance"
        my_output = pytlwall.TxtIo()
        my_output.save_ZAllTrans(filedir, filename, mywall.f, mywall.ZDipX,
                                 mywall.ZDipY, mywall.ZQuadX, mywall.ZQuadY,
                                 label)


if __name__ == '__main__':
    unittest.main()
