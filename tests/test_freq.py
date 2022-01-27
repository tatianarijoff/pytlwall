import unittest
from matplotlib import pyplot as plt
import pytlwall


class TestFreq(unittest.TestCase):
    def test_default(self):
        print('\nTesting default values')
        freq = pytlwall.Frequencies()
        self.assertEqual(0, freq.fmin)
        self.assertEqual(8, freq.fmax)
        # ~ self.assertEqual(2, freq.fstep)
        # ~ fig = plt.figure
        # ~ plt.plot(freq.freq, '*')
        # ~ plt.yscale('log')
        # ~ plt.show()

    def test_freq_val(self):
        print('\nTesting frequencies  values')
        freq = pytlwall.Frequencies(fmin=-2, fmax=6, fstep=1)
        self.assertEqual(-2, freq.fmin)
        self.assertEqual(6, freq.fmax)
        self.assertEqual(1, freq.fstep)
        # ~ fig = plt.figure
        # ~ plt.plot(freq.freq, '*')
        # ~ plt.yscale('log')
        # ~ plt.show()


if __name__ == '__main__':

    unittest.main()
