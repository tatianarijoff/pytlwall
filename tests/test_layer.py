import unittest
import numpy as np
import pytlwall


class TestLayer(unittest.TestCase):
    def test_default(self):
        print('\nTesting default values')
        layer = pytlwall.Layer()
        self.assertEqual('CW', layer.layer_type)
        self.assertEqual(0., layer.muinf_Hz)

    def test_freq(self):
        print('\nTesting frequency')
        layer = pytlwall.Layer()
        layer.freq_Hz = np.array([10, 100, 1000])
        self.assertEqual(1., layer.mur[0])
        print(layer.sigmaDC_R)

if __name__ == '__main__':
    unittest.main()
