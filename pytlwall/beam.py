'''
@authors: Tatiana Rijoff,
          Carlo Zannini
@date:    01/03/2013
@copyright CERN
'''

import numpy as np
import scipy.constants as const

m_p_MeV = const.physical_constants['proton mass energy equivalent in MeV'][0]
default_betarel = 1
default_gammarel = float('inf')
default_Ekin_MeV = float('inf')
default_p_MeV_c = float('inf')


class Beam(object):
    '''The beam object contains the basic properties of a beam for resistive
    wall calculation: the kinetic properties (velocity, momentum etc) and the
    test beam distance '''

    def __init__(self, Ekin_MeV=default_Ekin_MeV, p_MeV_c=default_p_MeV_c,
                 betarel=default_betarel, gammarel=default_gammarel,
                 test_beam_shift=0.001, mass_MeV_c2=m_p_MeV):

        self._m_MeV_c2 = mass_MeV_c2
        self.test_beam_shift = test_beam_shift
        self.betarel = 1

        if (gammarel != default_gammarel):
            self.gammarel = gammarel
        elif (Ekin_MeV != default_Ekin_MeV):
            self.Ekin_MeV = Ekin_MeV
        elif (p_MeV_c != default_p_MeV_c):
            self.p_MeV_c = p_MeV_c
        else:
            self.betarel = betarel

    @property
    def betarel(self):
        return self._betarel

    @betarel.setter
    def betarel(self, newbeta):
        try:
            tmp_beta = float(newbeta)
        except ValueError:
            print("%s is not a good value for relativistic beta, "
                  "the beta value is not modified" % (newbeta))
            return
        if (tmp_beta <= 0 or tmp_beta > 1):
            print("%s is not a good value for relativistic beta, "
                  " the beta value is not modified" % (tmp_beta))
            return
        try:
            tmp_gamma = np.sqrt(1. / (1. -
                                      (tmp_beta*tmp_beta)))
        except ZeroDivisionError:
            tmp_gamma = float('inf')
        self._betarel = tmp_beta
        self._gammarel = tmp_gamma
        self._p_MeV_c = (self._gammarel * self._m_MeV_c2
                         * self._betarel)
        self._Ekin_MeV = self._m_MeV_c2 * (self._gammarel - 1)

    @property
    def gammarel(self):
        return self._gammarel

    @gammarel.setter
    def gammarel(self, newgamma):
        try:
            tmp_gamma = float(newgamma)
        except ValueError:
            print("%s is not a good value for relativistic gamma, "
                  "the gamma value is not modified" % (newgamma))
            return
        if (tmp_gamma <= 0):
            print("%s is not a good value for relativistic gamma, "
                  " the gamma value is not modified" % (tmp_gamma))
            return

        self._gammarel = tmp_gamma
        self._betarel = np.sqrt(1 - (1/(self._gammarel*self._gammarel)))
        self._p_MeV_c = (self._gammarel * self._m_MeV_c2
                         * self._betarel)
        self._Ekin_MeV = self._m_MeV_c2 * (self._gammarel - 1)

    @property
    def Ekin_MeV(self):
        return self._Ekin_MeV

    @Ekin_MeV.setter
    def Ekin_MeV(self, newEkin):
        try:
            tmp_Ekin = float(newEkin)
        except ValueError:
            print("%s is not a good value for kinetic energy, values is "
                  " not changed " % (newEkin))
        if (tmp_Ekin <= 0):
            print("%s is not a good value for kinetic energy, values is "
                  " not changed " % (tmp_Ekin))
            return
        self._Ekin_MeV = tmp_Ekin
        self._gammarel = (self._Ekin_MeV / self._m_MeV_c2) + 1.
        self._betarel = np.sqrt(1 - (1 / (self._gammarel*self._gammarel)))
        self._p_MeV_c = (self._gammarel * self._m_MeV_c2
                         * self._betarel)

    @property
    def p_MeV_c(self):
        return self._p_MeV_c

    @p_MeV_c.setter
    def p_MeV_c(self, newp):
        try:
            tmp_p = float(newp)
        except ValueError:
            print("%s is not a good value for momentum, value is "
                  " not changed " % (newp))
        if (tmp_p <= 0):
            print("%s is not a good value for momentum, value is "
                  " not changed " % (tmp_p))
            return
        self._p_MeV_c = tmp_p
        self._Ekin_MeV = np.sqrt(self._p_MeV_c**2 + self._m_MeV_c2**2)
        self._gammarel = (self._Ekin_MeV / self._m_MeV_c2) + 1.
        self._betarel = np.sqrt(1 - (1 / (self._gammarel*self._gammarel)))
