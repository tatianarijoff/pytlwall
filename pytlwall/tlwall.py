'''
@authors: Tatiana Rijoff,
          Carlo Zannini
@date:    01/03/2013
@copyright CERN
'''
import numpy as np
import scipy.constants as const
from scipy.special import i0, i1, k0, k1, j0, iv, kv, jv
import cmath

Z0 = const.physical_constants['characteristic impedance of vacuum'][0]
np.seterr(over='ignore')
np.seterr(invalid='ignore')


class TlWall(object):
    def __init__(self, chamber, beam, freq):
        '''The TlWall object performs the impedances calculations.'''
        self.accuracy_factor = 0.3
        self.chamber = chamber
        self.beam = beam
        self.freq = freq
        self.f = self.freq.freq
        for layer in self.chamber.layers:
            layer.freq_Hz = self.f
        self.corr_imp = self.calc_corr_imp_factor()

    def calc_ZLong(self):
        """ Zlong = pipe_len  KZeff / (2 pi pipe_rad_m) """
        KZeff = self.calc_KZeff()
        ZLong = self.chamber.pipe_len_m * KZeff\
            / (2. * const.pi * self.chamber.pipe_rad_m)
        # for future refinement we foresee a longitudinal correction factor
        # not fully implemented at the moment
        # ~ corr_imp_long = self.calc_corr_imp_long_factor(KZeff)
        # ~ ZLong_corr = ZLong * corr_imp_long / self.corr_imp
        ZLong_corr = ZLong / self.corr_imp
        # for corr_imp equal to infinity we need to change the results of
        # 1 / inf from nan to 0
        ZLong_corr[np.argwhere(np.isnan(ZLong_corr))] = 0
        self.ZLong = ZLong_corr
        return ZLong_corr

    def calc_ZTrans(self):
        """  Z_dip =  2* Zlongin * bypass /(pipe_rad_m**2 * beta) """
        KZeffin = self.calc_KZeffin()
        Zlongin = self.chamber.pipe_len_m * KZeffin\
            / (2 * const.pi * self.chamber.pipe_rad_m)
        beta = 2 * const.pi * self.f * np.sqrt(const.epsilon_0 * const.mu_0)\
            / self.beam.betarel
        Ind = const.mu_0 * self.chamber.layers[-1].mu\
            / (const.mu_0 + self.chamber.layers[-1].mu)
        Zind = 1.j * self.f * (Ind) * self.chamber.pipe_len_m
        bypass = Zind / (Zlongin + Zind)
        ZTrans = 2 * Zlongin * bypass / (self.chamber.pipe_rad_m**2 * beta)
        ZTrans_corr = ZTrans / self.corr_imp
        # for corr_imp equal to infinity we need to change the results of
        # 1 / inf from nan to 0
        ZTrans_corr[np.argwhere(np.isnan(ZTrans_corr))] = 0
        self.ZTrans = ZTrans_corr
        return ZTrans_corr

    @property
    def ZDipX(self):
        try:
            ZDipX = (self.ZTrans * self.chamber.drivx_yokoya_factor
                     * self.chamber.betax)
        except AttributeError:
            self.ZTrans = self.calc_ZTrans()
            ZDipX = (self.ZTrans * self.chamber.drivx_yokoya_factor
                     * self.chamber.betax)

        return ZDipX

    @property
    def ZDipY(self):
        try:
            ZDipY = (self.ZTrans * self.chamber.drivy_yokoya_factor
                     * self.chamber.betay)
        except AttributeError:
            self.ZTrans = self.calc_ZTrans()
            ZDipY = (self.ZTrans * self.chamber.drivy_yokoya_factor
                     * self.chamber.betay)
        return ZDipY

    @property
    def ZQuadX(self):
        try:
            ZQuadX = (self.ZTrans * self.chamber.detx_yokoya_factor
                      * self.chamber.betax)
        except AttributeError:
            self.ZTrans = self.calc_ZTrans()
            ZQuadX = (self.ZTrans * self.chamber.detx_yokoya_factor
                      * self.chamber.betax)
        return ZQuadX

    @property
    def ZQuadY(self):
        try:
            ZQuadY = (self.ZTrans * self.chamber.dety_yokoya_factor
                      * self.chamber.betay)
        except AttributeError:
            self.ZTrans = self.calc_ZTrans()
            ZQuadY = (self.ZTrans * self.chamber.dety_yokoya_factor
                      * self.chamber.betay)
        return ZQuadY

    #
    #  Impedance functions
    #
    def calc_corr_imp_factor(self):
        reduct_factor = iv(0, 2 * const.pi * self.f
                           * self.chamber.pipe_rad_m
                           / (self.beam.betarel * const.c
                              * self.beam.gammarel))**2
        return reduct_factor

    def calc_corr_imp_long_factor(self, KZeff):
        #
        # This factor is not used for the moment
        #
        reduct_factor = 1 + (1.j * (const.epsilon_0 * self.f * KZeff
                                    * (self.chamber.pipe_rad_m + 3.85
                                       * self.chamber.layers[0].thick_m)**2)
                             / self.chamber.pipe_rad_m)
        return reduct_factor

    #
    #   KZeff and KZeffin functions
    #
    def calc_KZeff(self):
        """ KZeff is calculated recursively with the formula
        KZeff = KZ ((KZeff  + j KZ  tan(kprop t))
              / (KZ  + 1.j  KZeff  tan(kprop t))
        for boundary
            if PEC   KZeff = 0
            elif V   KZeff = Z0 (1 - (1 /BesselI(0, kprop * pipe_rad_m)))
            else     KZeff = sqrt(mu/eps)
        It is used in the longitudinal calculation
        """
        if self.chamber.layers[-1].layer_type.upper() == 'PEC':
            KZeff = 0
        elif self.chamber.layers[-1].layer_type.upper() == 'V':
            kprop = 2 * const.pi * self.f / (const.c)
            # Scil is abs(1/i0(k r)) - abs(k0(k*r/(beta * gamma)))
            # first we calculat the first term and convert the nan obtained
            # when i0 is infinity to 0, then we subtract the second term
            Scil = abs(1 / iv(0, kprop * self.chamber.pipe_rad_m))
            Scil[np.argwhere(np.isnan(Scil))] = 0
            arg = (kprop * self.chamber.pipe_rad_m
                   / (self.beam.betarel * self.beam.gammarel))
            Scil = Scil - abs(kv(0, arg) * (1 - self.beam.betarel)
                              / self.beam.gammarel**2)
            KZeff = Z0 * (1 - Scil)
        else:
            kprop = self.chamber.layers[-1].kprop
            KZ = self.chamber.layers[-1].KZ
            Scil = 1 / jv(0, 1.j * kprop * self.chamber.pipe_rad_m)
            Scil[np.argwhere(np.isnan(Scil))] = 0
            KZeff = KZ * (1 - Scil)

        for i in range(len(self.chamber.layers)-2, -1, -1):
            if self.chamber.layers[i].layer_type.upper() == 'PEC':
                KZ = 0
            elif self.chamber.layers[i].layer_type.upper() == 'V':
                KZ = Z0
                kprop = 2 * const.pi * self.f / const.c
            else:
                kprop = self.chamber.layers[i].kprop
                KZ = self.chamber.layers[i].KZ
            tan_t_kprop = np.tan(kprop * self.chamber.layers[i].thick_m)
            Scil = 1 / (abs(iv(0, 1.j * kprop * self.chamber.pipe_rad_m))
                        * abs(iv(0, 1.j * kprop
                              * self.chamber.layers[i].thick_m
                              * self.beam.gammarel * self.beam.betarel)))
            Scil[np.argwhere(np.isnan(Scil))] = 0
            KZ = KZ * (1 - Scil)
            KZeff = KZ * ((KZeff + 1.j * KZ * tan_t_kprop)
                          / (KZ + 1.j * KZeff * tan_t_kprop))
        return KZeff

    def calc_KZeffin(self):
        """ KZeffin is calculated recursively with the formula
        KZeffin = KZ ((KZeff  + j KZ  tan(kprop t)) /
                 (KZ  + 1.j  KZeffin  tan(kprop t))
        for boundary
            if PEC   KZeff = 0
            elif V   KZeff = Z0
            else     KZeff = sqrt(mu/eps)
        It is used in transvers calculation
        """
        # boundary layer
        if self.chamber.layers[-1].layer_type.upper() == 'PEC':
            KZeffin = 0
        elif self.chamber.layers[-1].layer_type.upper() == 'V':
            KZeffin = Z0
        else:
            KZ = self.chamber.layers[-1].KZ
            KZeffin = KZ
        for i in range(len(self.chamber.layers)-2, -1, -1):
            if self.chamber.layers[i].layer_type.upper() == 'PEC':
                KZ = 0
            elif self.chamber.layers[i].layer_type.upper() == 'V':
                KZ = Z0
                kprop = 2 * const.pi * self.f / const.c
            else:
                kprop = self.chamber.layers[i].kprop
                KZ = self.chamber.layers[i].KZ
            try:
                tan_t_kprop = np.array(list(map(lambda currkprop:
                                       cmath.tan(currkprop
                                            * self.chamber.layers[i].thick_m),
                                       kprop)))
            except TypeError:
                tan_t_kprop = cmath.tan(kprop
                                        * self.chamber.layers[i].thick_m)
            KZeffin = KZ * ((KZeffin + 1.j * KZ * tan_t_kprop)
                            / (KZ + 1.j * KZeffin * tan_t_kprop))
        return KZeffin

    #
    #  Space charge functions
    #
    @property
    def ZLongDSC(self):
        if self.beam.gammarel == float('inf'):
            ZLong_DSC = np.zeros(len(self.f)) + 1.j * np.zeros(len(self.f))
            return ZLong_DSC
        kbess = 2 * const.pi * self.f / (self.beam.betarel * const.c)
        argbess0 = kbess * self.beam.test_beam_shift / self.beam.gammarel
        BessBeamL = (i0(argbess0))**2
        BessBeamLDSC = k0(argbess0) / i0(argbess0)
        # longitudinal direct space charge
        Zlong_DSC = - (1.j * const.pi * self.f * self.chamber.pipe_len_m
                       * BessBeamL * BessBeamLDSC
                       / (const.epsilon_0 * const.pi
                          * (self.beam.gammarel * self.beam.betarel
                             * const.c)**2))
        return ZLong_DSC

    @property
    def ZLongISC(self):
        if self.beam.gammarel == float('inf'):
            ZLong_ISC = np.zeros(len(self.f)) + 1.j * np.zeros(len(self.f))
            return ZLong_ISC
        kbess = 2 * const.pi * self.f / (self.beam.betarel * const.c)
        argbess0 = kbess * self.beam.test_beam_shift / self.beam.gammarel
        argbess1 = kbess * self.chamber.pipe_rad_m / self.beam.gammarel
        BessBeamL = (i0(argbess0))**2
        BessBeamLISC = - k0(argbess1) / i0(argbess1)
        # longitudinal indirect space charge
        ZLong_ISC = - (1.j * const.pi * self.f * self.chamber.pipe_len_m
                       * BessBeamL * BessBeamLISC
                       / (const.epsilon_0 * const.pi
                          * (self.beam.gammarel * self.beam.betarel
                             * const.c)**2))
        return ZLong_ISC

    @property
    def ZTransISC(self):
        if self.beam.gammarel == float('inf'):
            ZTrans_ISC = np.zeros(len(self.f)) + 1.j * np.zeros(len(self.f))
            return ZTrans_ISC
        kbess = 2 * const.pi * self.f / (self.beam.betarel * const.c)
        argbess0 = kbess * self.beam.test_beam_shift / self.beam.gammarel
        argbess1 = kbess * self.chamber.pipe_rad_m / self.beam.gammarel
        BessBeamTISC = - k1(argbess1) / i1(argbess1)
        # transverse indirect space charge
        if (self.beam.test_beam_shift == 0.):
            BessA = kbess**2 / (2 * self.beam.gammarel * self.beam.gammarel) \
                    * k1(argbess1) / i1(argbess1)
            ZTrans_ISC = (1.j * Z0 * self.chamber.pipe_len_m * BessA
                          / (2 * const.pi * self.beam.gammarel**2
                             * self.beam.betarel))
        else:
            BessBeamT = (i1(argbess0) / self.beam.test_beam_shift)**2
            ZTrans_ISC = - (1.j * Z0 * self.chamber.pipe_len_m
                            * BessBeamT * BessBeamTISC
                            / (const.pi * self.beam.gammarel**2
                               * self.beam.betarel))
        return ZTrans_ISC

    @property
    def ZTransDSC(self):
        if self.beam.gammarel == float('inf'):
            ZTrans_DSC = np.zeros(len(self.f)) + 1.j * np.zeros(len(self.f))
            return ZTrans_DSC
        kbess = 2 * const.pi * self.f / (self.beam.betarel * const.c)
        argbess0 = kbess * self.beam.test_beam_shift / self.beam.gammarel
        argbess1 = kbess * self.chamber.pipe_rad_m / self.beam.gammarel
        BessBeamT = (i1(argbess0) / self.beam.test_beam_shift)**2
        BessBeamTDSC = k1(argbess0) / i1(argbess0)
        ZTrans_DSC = - (1.j * Z0 * self.chamber.pipe_len_m * BessBeamT
                        * BessBeamTDSC / (const.pi * self.beam.gammarel**2
                                          * self.beam.betarel))
        return ZTrans_DSC
