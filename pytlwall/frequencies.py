'''
@authors: Tatiana Rijoff,
          Carlo Zannini
@date:    01/03/2013
@copyright CERN
'''
import numpy as np

default_fmin = 0
default_fmax = 8
default_fstep = 2
default_freq_unit = 'Hz'
default_sep = ' '


class Frequencies(object):
    def __init__(self, freq_list=[], fmin=default_fmin, fmax=default_fmax,
                 fstep=default_fstep):
        '''The frequency object contains the list of frequencies in Hertz at
        which the impedances are calculated. The module can take a list of
        frequency, or can calculate using a minimum (fmin),
        a maximum (fmax) and a step (fstep) exponent, so that the
        frequency list will be the array which starts from 10^fmin and
        arrives to 10^fmax, with step 10^fstep'''
        self._fmin = default_fmin
        self._fmax = default_fmax
        self._fstep = default_fstep

        self.fmin = fmin
        self.fmax = fmax
        self.fstep = fstep

        self.freq = self.calc_freq_array(self.fmin, self.fmax, self.fstep)

    @property
    def fmin(self):
        return self._fmin

    @fmin.setter
    def fmin(self, newfmin):
        try:
            tmp_fmin = float(newfmin)
        except ValueError:
            print("%s is not a good value for minimum frequency exponent, "
                  "the value is not modified" % (newfmin))
            return
        self._fmin = tmp_fmin
        return

    @property
    def fmax(self):
        return self._fmax

    @fmax.setter
    def fmax(self, newfmax):
        try:
            tmp_fmax = float(newfmax)
        except ValueError:
            print("%s is not a good value for maximum frequency exponent, "
                  "the value is not modified" % (newfmax))
            return
        self._fmax = tmp_fmax
        return

    @property
    def fstep(self):
        return self._fstep

    @fstep.setter
    def fstep(self, newfstep):
        try:
            tmp_fstep = float(newfstep)
        except ValueError:
            print("%s is not a good value for step frequency exponent, "
                  "the value is not modified" % (newfstep))
            return
        self._fstep = tmp_fstep
        return

    def calc_freq_array(self, fmin, fmax, fstep):
        f = np.array([])
        for p in np.arange(1, fmax - fmin + 1):
            v1 = (1 + (10**(1 - fstep))) * 10.**(fmin - 1 + p)
            v2 = 10.**(fmin + p)
            v3 = 10.**(fmin - 1 + p - (fstep - 1))
            f = np.append(f, np.arange(v1, v2 + v3, v3))
        return f
