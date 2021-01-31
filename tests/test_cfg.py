import unittest
import numpy as np
from matplotlib import pyplot as plt
import pytlwall


class TestCfgIo(unittest.TestCase):
    def test_onelayer(self):
        print('\nTesting one layer cfg')
        read_cfg = pytlwall.CfgIo()
        chamber = read_cfg.read_chamber('input/one_layer.cfg')
        self.assertEqual('prova', chamber.component_name)
        self.assertEqual(2e-2, chamber.pipe_hor_m)
        self.assertEqual('CW', chamber.layers[0].layer_type)
        self.assertEqual('PEC', chamber.layers[1].layer_type)

    def test_frequency(self):
        print('\nTesting frequency')
        read_cfg = pytlwall.CfgIo()
        freq = read_cfg.read_freq('input/one_layer.cfg')
        self.assertEqual(2, freq.fstep)

    def test_beam(self):
        print('\nTesting beam')
        read_cfg = pytlwall.CfgIo()
        beam = read_cfg.read_beam('input/one_layer.cfg')
        self.assertEqual(0.01, beam.test_beam_shift)
        self.assertEqual(1e5, round(beam.gammarel, 3))

    def test_pytlwall(self):
        print('\nTesting pytlwall')
        read_cfg = pytlwall.CfgIo('input/one_layer.cfg')
        mywall = read_cfg.read_pytlwall()
        self.assertEqual(0.01, mywall.beam.test_beam_shift)
        self.assertEqual(1.e5, round(mywall.beam.gammarel, 3))

if __name__ == '__main__':
    unittest.main()
