import unittest
import pytlwall


class TestBeam(unittest.TestCase):

    def test_default(self):
        print('\nTesting default values')
        beam = pytlwall.Beam()
        self.assertEqual(1, beam.betarel)
        self.assertEqual(float('inf'), beam.gammarel)
        self.assertEqual(float('inf'), beam.Ekin_MeV)
        self.assertEqual(float('inf'), beam.p_MeV_c)

    def test_string(self):
        print('\nTest string value for beta')
        beam = pytlwall.Beam(betarel='betarel')
        self.assertEqual(1, beam.betarel)

    def test_betarel_neg(self):
        print('\nTest negative value for beta')
        beam = pytlwall.Beam(betarel=-0.99)
        self.assertEqual(1, beam.betarel)

    def test_betarel_gt1(self):
        print('\nTest beta greater than 1')
        beam = pytlwall.Beam(betarel=1.99)
        self.assertEqual(1, beam.betarel)

    def test_Ekin_neg(self):
        print('\nTest negative value for kinetic energy')
        beam = pytlwall.Beam(Ekin_MeV=-0.99)
        self.assertEqual(1, beam.betarel)

    def test_momentum_neg(self):
        print('\nTest negative value for momentum')
        beam = pytlwall.Beam(p_MeV_c=-4.99)
        self.assertEqual(1, beam.betarel)

    def test_betarel(self):
        print('\nTest beta')
        beam = pytlwall.Beam(betarel=0.106)
        self.assertEqual(0.106, beam.betarel)
        self.assertEqual(1.006, round(beam.gammarel, 3))
        self.assertEqual(5.3, round(beam.Ekin_MeV, 1))
        self.assertEqual(100.0, round(beam.p_MeV_c, 1))

    def test_gammarel(self):
        print('\nTest gamma')
        beam = pytlwall.Beam(gammarel=1.006)
        self.assertEqual(0.109, round(beam.betarel, 3))
        self.assertEqual(1.006, round(beam.gammarel, 3))
        self.assertEqual(5.6, round(beam.Ekin_MeV, 1))
        self.assertEqual(102.9, round(beam.p_MeV_c, 1))

    def test_Ekin(self):
        print('\nTest kinetic energy')
        beam = pytlwall.Beam(Ekin_MeV=0.1)
        self.assertEqual(0.015, round(beam.betarel, 3))
        self.assertEqual(1.0, round(beam.gammarel, 3))
        self.assertEqual(0.1, round(beam.Ekin_MeV, 1))
        self.assertEqual(13.7, round(beam.p_MeV_c, 1))

    def test_Ekin(self):
        print('\nTest momentum')
        beam = pytlwall.Beam(p_MeV_c=0.1)
        self.assertEqual(0.87, round(beam.betarel, 2))
        self.assertEqual(2.00, round(beam.gammarel, 3))
        self.assertEqual(938.3, round(beam.Ekin_MeV, 1))
        self.assertEqual(0.1, round(beam.p_MeV_c, 1))


if __name__ == '__main__':
    unittest.main()
