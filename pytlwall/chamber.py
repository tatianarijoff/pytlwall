'''
@authors: Tatiana Rijoff,
          Carlo Zannini
@date:    01/03/2013
@copyright CERN
'''
import numpy as np

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
        yokoya_q = abs(pipe_hor_m - pipe_ver_m) / (pipe_hor_m + pipe_ver_m)
        return yokoya_q

    @property
    def long_yokoya_factor(self):
        # to do
        long_yoko = 1.
        return long_yoko

    @property
    def drivx_yokoya_factor(self):
        # to do
        drivx_yoko = 1.
        return drivx_yoko

    @property
    def drivy_yokoya_factor(self):
        # to do
        drivy_yoko = 1.
        return drivy_yoko

    @property
    def detx_yokoya_factor(self):
        # to do
        detx_yoko = 0.
        return detx_yoko

    @property
    def dety_yokoya_factor(self):
        # to do
        dety_yoko = 0.
        return dety_yoko

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
        if (tmpchamber_shape.upper() == 'ELLIPTICAL' or
                tmpchamber_shape.upper() == 'RECTANGULAR' or
                tmpchamber_shape.upper() == 'CIRCULAR'):
            self._chamber_shape = tmpchamber_shape
            # TO DO
            # READ THE FILE FOR THE SHAPE
        else:
            print("%s is not a good value for the chamber shape "
                  "the value is not modified" % (newbetay))
        return

    @property
    def component_name(self):
        return self._component_name

    @component_name.setter
    def component_name(self, newname):
        self._component_name = newname
        return

    def calc_form_factor(self):
        x_coord = abs(self.pipe_hor_m - self.pipe_ver_m)\
                  / (self.pipe_hor_m - self.pipe_ver_m)
        # TO DO
        self.form_factor_longit = 1
        self.form_factor_drivx = 1
        self.form_factor_drivy = 1
        self.form_factor_detx = 1
        self.form_factor_dety = 1
        return
