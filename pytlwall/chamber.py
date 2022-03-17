'''
@authors: Tatiana Rijoff,
          Carlo Zannini
@date:    01/03/2013
@copyright CERN
'''
import numpy as np
from .yokoya_factors.yokoya_q_factor import yoko_q
from .yokoya_factors.ellipt_long import ellipt_long
from .yokoya_factors.ellipt_drivx import ellipt_drivx
from .yokoya_factors.ellipt_drivy import ellipt_drivy
from .yokoya_factors.ellipt_detx import ellipt_detx
from .yokoya_factors.ellipt_dety import ellipt_dety
from .yokoya_factors.rect_long import rect_long
from .yokoya_factors.rect_drivx import rect_drivx
from .yokoya_factors.rect_drivy import rect_drivy
from .yokoya_factors.rect_detx import rect_detx
from .yokoya_factors.rect_dety import rect_dety

default_pipe_len_m = 1.
default_pipe_rad_m = 1.e-2
default_pipe_hor_m = 1.e-2
default_pipe_ver_m = 1.e-2
default_chamber_shape = 'CIRCULAR'
default_betax = 1.
default_betay = 1.
default_component_name = 'el'


class Chamber(object):
    def __init__(self, pipe_len_m=default_pipe_len_m,
                 pipe_rad_m=default_pipe_rad_m,
                 pipe_hor_m=default_pipe_hor_m,
                 pipe_ver_m=default_pipe_ver_m,
                 chamber_shape=default_chamber_shape,
                 betax=default_betax,
                 betay=default_betay, layers=[],
                 component_name=default_component_name):
        self.pipe_len_m = default_pipe_len_m
        self.pipe_rad_m = default_pipe_rad_m
        self.pipe_hor_m = default_pipe_hor_m
        self.pipe_ver_m = default_pipe_ver_m
        self.chamber_shape = default_chamber_shape
        self.betax = default_betax
        self.betay = default_betay
        self.layers = []
        self.component_name = default_component_name
        self.pipe_len_m = pipe_len_m
        self.pipe_rad_m = pipe_rad_m
        if (pipe_hor_m != default_pipe_hor_m):
            self.pipe_hor_m = pipe_hor_m
        if (pipe_ver_m != default_pipe_ver_m):
            self.pipe_ver_m = pipe_ver_m
        self.chamber_shape = chamber_shape
        self.betax = betax
        self.betay = betay
        self.layers = layers
        self.component_name = component_name

    @property
    def pipe_len_m(self):
        return self._pipe_len_m

    @pipe_len_m.setter
    def pipe_len_m(self, newlen):
        try:
            tmp_len = float(newlen)
        except ValueError:
            print("%s is not a good value for the pipe lenght, "
                  "the value is not modified" % (newlen))
            return
        self._pipe_len_m = tmp_len
        return

    @property
    def pipe_rad_m(self):
        return self._pipe_rad_m

    @pipe_rad_m.setter
    def pipe_rad_m(self, newrad):
        try:
            tmp_rad = float(newrad)
        except ValueError:
            print("%s is not a good value for the pipe radius dimension, "
                  "the value is not modified" % (newrad))
            return
        self._pipe_rad_m = tmp_rad
        self._pipe_ver_m = tmp_rad
        self._pipe_hor_m = tmp_rad
        return

    @property
    def pipe_hor_m(self):
        return self._pipe_hor_m

    @pipe_hor_m.setter
    def pipe_hor_m(self, newhor):
        try:
            tmp_hor = float(newhor)
        except ValueError:
            print("%s is not a good value for the pipe horizontal dimension, "
                  "the value is not modified" % (newhor))
            return
        self._pipe_hor_m = tmp_hor
        return

    @property
    def pipe_ver_m(self):
        return self._pipe_ver_m

    @pipe_ver_m.setter
    def pipe_ver_m(self, newver):
        try:
            tmp_ver = float(newver)
        except ValueError:
            print("%s is not a good value for the pipe vertical dimension, "
                  "the value is not modified" % (newver))
            return
        self._pipe_ver_m = tmp_ver
        self._pipe_rad_m = tmp_ver
        return

    @property
    def yokoya_q(self):
        yokoya_q = abs(self.pipe_hor_m - self.pipe_ver_m)\
                     / (self.pipe_hor_m + self.pipe_ver_m)
        return yokoya_q

    @property
    def yokoya_q_idx(self):
        idx = (np.abs(yoko_q - self.yokoya_q)).argmin()
        return idx

    @property
    def long_yokoya_factor(self):
        return self.long_yoko_list[self.yokoya_q_idx]

    @property
    def drivx_yokoya_factor(self):
        return self.drivx_yoko_list[self.yokoya_q_idx]

    @property
    def drivy_yokoya_factor(self):
        return self.drivy_yoko_list[self.yokoya_q_idx]

    @property
    def detx_yokoya_factor(self):
        return self.detx_yoko_list[self.yokoya_q_idx]

    @property
    def dety_yokoya_factor(self):
        return self.dety_yoko_list[self.yokoya_q_idx]

    @property
    def betax(self):
        return self._betax

    @betax.setter
    def betax(self, newbetax):
        try:
            tmp_betax = float(newbetax)
        except ValueError:
            print("%s is not a good value for the beta x, "
                  "the value is not modified" % (newbetax))
            return
        self._betax = tmp_betax
        return

    @property
    def betay(self):
        return self._betay

    @betay.setter
    def betay(self, newbetay):
        try:
            tmp_betay = float(newbetay)
        except ValueError:
            print("%s is not a good value for the beta y, "
                  "the value is not modified" % (newbetay))
            return
        self._betay = tmp_betay
        return

    @property
    def chamber_shape(self):
        return self._chamber_shape

    @chamber_shape.setter
    def chamber_shape(self, tmpchamber_shape):
        if (tmpchamber_shape.upper() == 'ELLIPTICAL'):
            self._chamber_shape = tmpchamber_shape
            self.long_yoko_list = ellipt_long
            self.drivx_yoko_list = ellipt_drivx
            self.drivy_yoko_list = ellipt_drivy
            self.detx_yoko_list = ellipt_detx
            self.dety_yoko_list = ellipt_dety
        elif (tmpchamber_shape.upper() == 'RECTANGULAR'):
            self._chamber_shape = tmpchamber_shape
            self.long_yoko_list = rect_long
            self.drivx_yoko_list = rect_drivx
            self.drivy_yoko_list = rect_drivy
            self.detx_yoko_list = rect_detx
            self.dety_yoko_list = rect_dety
        elif (tmpchamber_shape.upper() == 'CIRCULAR'):
            self._chamber_shape = tmpchamber_shape
            self.long_yoko_list = np.ones(len(yoko_q))
            self.drivx_yoko_list = np.ones(len(yoko_q))
            self.drivy_yoko_list = np.ones(len(yoko_q))
            self.detx_yoko_list = np.zeros(len(yoko_q))
            self.dety_yoko_list = np.zeros(len(yoko_q))
        else:
            print("%s is not a good value for the chamber shape "
                  "the value is not modified" % (tmpchamber_shape))
        return

    @property
    def component_name(self):
        return self._component_name

    @component_name.setter
    def component_name(self, newname):
        self._component_name = newname
        return
