import unittest
import pytlwall
import pytlwall.txt_util as txt


class TestTxtIo(unittest.TestCase):
    def test_longitudinal_output(self):
        print('\nTesting longitudinal output, text')
        read_cfg = pytlwall.CfgIo('input/one_layer.cfg')
        mywall = read_cfg.read_pytlwall()
        mywall.calc_ZLong()
        filedir = 'output/'
        filename = 'one_layerZLong.txt'
        label = "longitudinal impedance"
        txt.save_ZLong(filedir, filename, mywall.f, mywall.ZLong, label)

    def test_transverse_output(self):
        print('\nTesting transverse output, text')
        read_cfg = pytlwall.CfgIo('input/one_layer.cfg')
        mywall = read_cfg.read_pytlwall()
        mywall.calc_ZTrans()
        filedir = 'output/'
        filename = 'one_layerZTrans.txt'
        label = "transverse impedance"
        txt.save_ZTrans(filedir, filename, mywall.f, mywall.ZTrans,
                        label)

    def test_all_transverse_output(self):
        print('\nTesting all the transverse output, text')
        read_cfg = pytlwall.CfgIo('input/test001.cfg')
        mywall = read_cfg.read_pytlwall()
        mywall.calc_ZTrans()
        filedir = 'output/'
        filename = 'test001ZAllTrans.txt'
        label = "transverse impedance"
        txt.save_ZAllTrans(filedir, filename, mywall.f, mywall.ZDipX,
                           mywall.ZDipY, mywall.ZQuadX, mywall.ZQuadY,
                           label)

    def test_frequency_input001(self):
        print('\nTesting frequency input')
        filedir = 'input/'
        filename = filedir + 'freq_input.txt'
        freq_list = txt.read_frequency_txt(filename, skipped_rows=2)
        freq = pytlwall.Frequencies(freq_list=freq_list)
        self.assertEqual(1.1, min(freq.freq))
        self.assertEqual(1e12, max(freq.freq))

    def test_frequency_input002(self):
        print('\nTesting frequency input unit GHz, comma separator')
        filedir = 'input/'
        filename = filedir + 'freq_input2.txt'
        freq_list = txt.read_frequency_txt(filename, separator=',',
                                           column=1, skipped_rows=2,
                                           unit='GHz')
        self.assertEqual(1e12, max(freq_list))
        freq = pytlwall.Frequencies(freq_list=freq_list)
        self.assertEqual(1e12, max(freq.freq))


if __name__ == '__main__':
    unittest.main()
