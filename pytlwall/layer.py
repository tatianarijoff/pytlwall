'''
@authors: Tatiana Rijoff,
          Carlo Zannini
@date:    01/03/2013
@copyright CERN
'''
import numpy as np
import scipy.constants as const

default_type = 'CW'
default_boundary_type = 'V'
default_thick_m = 1e-2
default_muinf_Hz = 0.
default_epsr = 1.
default_sigmaDC = 1.e6
default_k_Hz = float('inf')
default_tau = 0.
default_RQ = 0.


class Layer(object):
    def __init__(self, layer_type=default_type,
                 thick_m=default_thick_m,
                 muinf_Hz=default_muinf_Hz,
                 epsr=default_epsr,
                 sigmaDC=default_sigmaDC,
                 k_Hz=default_k_Hz,
                 tau=default_tau,
                 RQ=default_RQ,
                 freq_Hz=np.array([]),
                 boundary=False):

        if boundary is True:
            self._layer_type = default_boundary_type
        else:
            self._layer_type = default_type
        self._thick_m = default_thick_m
        self._muinf_Hz = default_muinf_Hz
        self._epsr = default_epsr
        self._sigmaDC = default_sigmaDC
        self._k_Hz = default_k_Hz
        self._tau = default_tau
        self._RQ = default_RQ
        self._freq_Hz = np.array([])

        self.layer_type = layer_type
        self.freq_Hz = freq_Hz
        self.thick_m = thick_m
        self._muinf_Hz = muinf_Hz
        self.epsr = epsr
        self.sigmaDC = sigmaDC
        self.k_Hz = k_Hz
        self.tau = tau
        self.RQ = RQ

    @property
    def layer_type(self):
        return self._layer_type

    @layer_type.setter
    def layer_type(self, newtype):
        if (newtype.upper() == 'CW' or
           newtype.upper() == 'V' or
           newtype.upper() == 'PEC'):
            self._layer_type = newtype.upper()
        else:
            print("%s is not a good value for the layer type, "
                  "the value is not modified" % (newtype))
            return

        return

    @property
    def thick_m(self):
        return self._thick_m

    @thick_m.setter
    def thick_m(self, newthick):
        try:
            tmp_thick = float(newthick)
        except ValueError:
            print("%s is not a good value for the layer thickness, "
                  "the value is not modified" % (newthick))
            return
        self._thick_m = tmp_thick
        return

    @property
    def epsr(self):
        return self._epsr

    @epsr.setter
    def epsr(self, newepsr):
        try:
            tmp_epsr = float(newepsr)
        except ValueError:
            print("%s is not a good value for the layer relative "
                  "permittivity, the value is not modified" % (newepsr))
            return
        self._epsr = tmp_epsr
        return

    @property
    def muinf_Hz(self):
        return self._muinf_Hz

    @muinf_Hz.setter
    def muinf_Hz(self, newmuinf_Hz):
        try:
            tmp_muinf_Hz = float(newmuinf_Hz)
        except ValueError:
            print("%s is not a good value for the layer permeability, "
                  "the value is not modified" % (newmuinf_Hz))
            return
        self._muinf_Hz = tmp_muinf_Hz
        return

    @property
    def k_Hz(self):
        return self._k_Hz

    @k_Hz.setter
    def k_Hz(self, newk_Hz):
        try:
            tmp_k_Hz = float(newk_Hz)
        except ValueError:
            print("%s is not a good value for the layer relaxation frequency"
                  " for permeability, the value is not modified" % (newk_Hz))
            return
        self._k_Hz = tmp_k_Hz
        return

    @property
    def sigmaDC(self):
        return self._sigmaDC

    @sigmaDC.setter
    def sigmaDC(self, newsigmaDC):
        try:
            tmp_sigmaDC = float(newsigmaDC)
        except ValueError:
            print("%s is not a good value for the layer DC conductivity, "
                  " the value is not modified" % (newsigmaDC))
            return
        self._sigmaDC = tmp_sigmaDC
        return

    @property
    def tau(self):
        return self._tau

    @tau.setter
    def tau(self, newtau):
        try:
            tmp_tau = float(newtau)
        except ValueError:
            print("%s is not a good value for the layer relaxation time"
                  " for permittivity, the value is not modified" % (newtau))
            return
        self._tau = tmp_tau
        return

    @property
    def RQ(self):
        return self._RQ

    @RQ.setter
    def RQ(self, newRQ):
        try:
            tmp_RQ = float(newRQ)
        except ValueError:
            print("%s is not a good value for the layer roughness,"
                  " the value is not modified" % (newRQ))
            return
        self._RQ = tmp_RQ
        return

    @property
    def freq_Hz(self):
        return self._freq_Hz

    @freq_Hz.setter
    def freq_Hz(self, newfreq_Hz):
        try:
            tmp_freq_Hz = newfreq_Hz.astype(float)
        except ValueError:
            print("The given value is not a good value for frequencies list,"
                  " the value is not modified")
            return
        except AttributeError:
            print("The given value is not a good value for frequencies list,"
                  " the value is not modified")
            return
        self._freq_Hz = tmp_freq_Hz

        return

    @property
    def KZ(self):
        try:
            return self._KZ
        except AttributeError:
            KZ = (1. + 1.j) / (self.sigmaPM * self.deltaM)
        return KZ

    @KZ.setter
    def KZ(self, newKZ):
        """ KZ is the surface impedance, in general the code will calculate
            this value but you can need to put it directly if the frequencies
            for the surface impedances are the one already defined for the 
            layer, if not use the function set_surf_imped."""
        if np.iscomplex(newKZ).all:
            self._KZ = newKZ
        else:
            print("The given value is not a good value for the surface "
                  " impedance, the value is not modified")
        return

    def set_surf_imped(self, newfreq_Hz, newKZ):
        """ set_surf_imped allows you to insert directly the known values of
        the surface impedance related to a given set of the frequencies (in HZ)
        the function interpolate the values to the layer frequencies."""
        if np.iscomplex(newKZ).all:
            tmp_KZ = newKZ
        else:
            print("The given value is not a good value for the surface "
                  " impedance, the value is not modified")
        tmp_freq_Hz = newfreq_Hz
        self._KZ = np.interp(self._freq_Hz, newfreq_Hz, tmp_KZ)
        return

            
    @property
    def sigmaAC(self):
        self._sigmaAC = self.calc_sigmaAC()
        return self._sigmaAC

    @property
    def sigmaPM(self):
        self._sigmaPM = self.calc_sigmaPM()
        return self._sigmaPM

    @property
    def eps(self):
        self._eps = const.epsilon_0 * self._epsr
        return self._eps

    @property
    def mur(self):
        self._mur = self.calc_mur()
        return self._mur

    @property
    def mu(self):
        self._mur = self.calc_mur()
        self._mu = const.mu_0 * self._mur
        return self._mu

    @property
    def delta(self):
        self._delta = self.calc_delta()
        return self._delta

    @property
    def deltaM(self):
        self._deltaM = self.calc_deltaM()
        return self._deltaM

    @property
    def RS(self):
        self._RS = self.calc_RS()
        return self._RS

    @property
    def sigmaDC_R(self):
        self._sigmaDC_R = self.calc_sigmaDC_R()
        return self._sigmaDC_R

    @property
    def kprop(self):
        kprop = (1 - 1.j) / self.delta
        return kprop

    def calc_sigmaAC(self):
        """ sigmaAC = sigmaDC / (1 + j 2 pi tau f ) """
        sigmaAC = self.sigmaDC_R / (1. + 2.j *
                                    const.pi * self.tau * self.freq_Hz)
        return sigmaAC

    def calc_mur(self):
        """ mur = 1 +  (muinf / ( 1 + j ( f / k)))
                   if k = inf  """
        mur = 1 + (self.muinf_Hz / (1 + 1.j * (self.freq_Hz / self.k_Hz)))
        return mur

    def calc_sigmaPM(self):
        """ sigmaPM = sqrt((2 pi  f  eps)^2 + sigma_ac^2 ) """
        sigmaPM = np.sqrt((2 * const.pi * self.freq_Hz * self.eps)**2 +
                          self.sigmaAC**2)
        return sigmaPM

    def calc_delta(self):
        """ delta = sqrt(2 / (2  pi f  mu sigma_ac
                    + j  mu eps ( 2 pi f)^2 )) """
        delta = np.sqrt(2 / (2 * const.pi * self.freq_Hz * self.mu *
                        self.sigmaAC + 1.j * self.mu * self.eps *
                        (2 * const.pi * self.freq_Hz)**2))
        return delta

    def calc_deltaM(self):
        """ deltaM = sqrt(2 / (2 pi f mu sigma_ac - j mu eps ( 2 pi f)^2)) """
        deltaM = np.sqrt(2 / (2 * const.pi * self.freq_Hz * self.mu *
                         self.sigmaAC - 1.j * self.mu * self.eps *
                         (2 * const.pi * self.freq_Hz)**2))
        return deltaM

    def calc_RS(self):
        """ RS = sqrt(mu omega/ 2 sigmaDC)
           ( 1 + (2/pi) * arctan(0.7 * mu  omega sigmaDC RQ^2 )) """
        RS = np.sqrt(self.mu * np.pi * self.freq_Hz / self.sigmaDC) * \
            (1 + (2 / np.pi) *
             np.arctan(0.7 * self.mu * 2 * np.pi * self.freq_Hz *
             self.sigmaDC * self.RQ**2))
        return RS

    def calc_sigmaDC_R(self):
        """ sigmaDC = pi * f * mu0 / RS^2 """
        sigmaDC = (np.ones(len(self.freq_Hz)) * self.sigmaDC +
                   1.j * np.ones(len(self.freq_Hz)))
        self._RS = np.ones(len(self.freq_Hz)) * self.RS
        mask = self._RS != 0

        sigmaDC[mask] = (np.pi * self.freq_Hz[mask] *
                         self.mu / self._RS[mask]**2)
        return sigmaDC
