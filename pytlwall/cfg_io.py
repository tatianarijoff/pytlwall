
'''
@authors: Tatiana Rijoff,
          Carlo Zannini
@date:    01/03/2013
@copyright CERN
'''
import pandas as pd
import configparser
import re
from pathlib import Path
import pytlwall
import pytlwall.plot_util as plot
import pytlwall.txt_util as txt


class CfgIo(object):
    def __init__(self, cfg_file=None):
        self.config = configparser.ConfigParser()
        if cfg_file is not None:
            self.read_cfg(cfg_file)
        return

    def read_chamber(self, cfg_file=None):
        if cfg_file is not None:
            self.read_cfg(cfg_file)
        if self.config.has_section('base_info') is False:
            return None
        pipe_len_m = self.config.getfloat('base_info', 'pipe_len_m')
        # pipe radius is equal to vertical dimension so in the cfg file or
        # it is defined the radius or the vertical dimension
        if self.config.has_option('base_info', 'pipe_radius_m'):
            pipe_rad_m = self.config.getfloat('base_info', 'pipe_radius_m')
            pipe_hor_m = pipe_rad_m
            pipe_ver_m = pipe_rad_m
        else:
            pipe_ver_m = self.config.getfloat('base_info', 'pipe_ver_m')
            pipe_rad_m = pipe_ver_m
        if self.config.has_option('base_info', 'pipe_hor_m'):
            pipe_hor_m = self.config.getfloat('base_info', 'pipe_hor_m')

        chamber_shape = self.config.get('base_info', 'chamber_shape')
        if self.config.has_option('base_info', 'component_name'):
            component_name = self.config.get('base_info', 'component_name')
        else:
            component_name = 'chamber'
        betax = self.config.getfloat('base_info', 'betax')
        betay = self.config.getfloat('base_info', 'betay')
        nbr_layers = self.config.getint('layers_info', 'nbr_layers')
        layers = []

        for i in range(nbr_layers):
            layer_type = self.config.get('layer' + str(i), 'type')
            thick_m = self.config.getfloat('layer' + str(i), 'thick_m')
            if layer_type == 'CW':
                muinf_Hz = self.config.getfloat('layer' + str(i), 'muinf_Hz')
                epsr = self.config.getfloat('layer' + str(i), 'epsr')
                sigmaDC = self.config.getfloat('layer' + str(i), 'sigmaDC')
                k_Hz = self.config.getfloat('layer' + str(i), 'k_Hz')
                tau = self.config.getfloat('layer' + str(i), 'tau')
                RQ = self.config.getfloat('layer' + str(i), 'RQ')
                layers.append(pytlwall.Layer(layer_type=layer_type,
                                             thick_m=thick_m,
                                             muinf_Hz=muinf_Hz,
                                             epsr=epsr,
                                             sigmaDC=sigmaDC,
                                             k_Hz=k_Hz,
                                             tau=tau,
                                             RQ=RQ,
                                             boundary=False))
            else:
                layers.append(pytlwall.Layer(layer_type=layer_type,
                                             thick_m=thick_m,
                                             boundary=False))

        layer_type = self.config.get('boundary', 'type')
        if layer_type == 'CW':
            muinf_Hz = self.config.getfloat('boundary', 'muinf_Hz')
            epsr = self.config.getfloat('boundary', 'epsr')
            sigmaDC = self.config.getfloat('boundary', 'sigmaDC')
            k_Hz = self.config.getfloat('boundary', 'k_Hz')
            tau = self.config.getfloat('boundary', 'tau')
            RQ = self.config.getfloat('boundary', 'RQ')
            layers.append(pytlwall.Layer(layer_type=layer_type,
                                         muinf_Hz=muinf_Hz,
                                         epsr=epsr,
                                         sigmaDC=sigmaDC,
                                         k_Hz=k_Hz,
                                         tau=tau,
                                         RQ=RQ,
                                         boundary=True))
        else:
            layers.append(pytlwall.Layer(layer_type=layer_type,
                                         boundary=True))

        chamber = pytlwall.Chamber(pipe_len_m=pipe_len_m,
                                   pipe_rad_m=pipe_rad_m,
                                   pipe_hor_m=pipe_hor_m,
                                   pipe_ver_m=pipe_ver_m,
                                   chamber_shape=chamber_shape,
                                   betax=betax,
                                   betay=betay,
                                   layers=layers,
                                   component_name=component_name)
        return chamber

    def read_freq(self, cfg_file=None):
        if cfg_file is not None:
            self.read_cfg(cfg_file)

        if self.config.has_section('frequency_info'):
            fmin = self.config.getfloat('frequency_info', 'fmin')
            fmax = self.config.getfloat('frequency_info', 'fmax')
            fstep = self.config.getfloat('frequency_info', 'fstep')
            freq = pytlwall.Frequencies(fmin=fmin, fmax=fmax, fstep=fstep)
        elif self.config.has_section('frequency_file'):
            filename = self.config.get('frequency_file', 'filename')
            try:
                sep = self.config.get('frequency_file', 'separator')
            except NoOptionError:
                sep = ''
            try: 
                col = self.config.getint('frequency_file', 'freq_col')
            except NoOptionError:
                col = 0
            try: 
                skip_rows = self.config.getint('frequency_file', 
                                                 'skip_rows')
            except NoOptionError:
                skip_rows = 0
            freq = txt.read_frequency_txt(filename, sep, col, skip_rows)
        else:
            freq = pytlwall.Frequencies()
        return freq

    def save_chamber(self, chamber):
        self.config.add_section('base_info')
        self.config.set('base_info', 'component_name',
                        chamber.component_name)
        self.config.set('base_info', 'chamber_shape',
                        chamber.chamber_shape)
        if chamber.chamber_shape == 'CIRCULAR':
            self.config.set('base_info', 'pipe_radius_m',
                            str(chamber.pipe_rad_m))
        else:
            self.config.set('base_info', 'pipe_hor_m',
                            str(chamber.pipe_hor_m))
            self.config.set('base_info', 'pipe_ver_m',
                            str(chamber.pipe_ver_m))
        self.config.set('base_info', 'pipe_len_m',
                        str(chamber.pipe_len_m))
        self.config.set('base_info', 'betax',
                        str(chamber.betax))
        self.config.set('base_info', 'betay',
                        str(chamber.betay))

    def save_layer(self, layers):
        self.config.add_section('layers_info')
        self.config.set('layers_info', 'nbr_layers',
                        str(len(layers)-1))
        for i in range(len(layers)-1):
            self.config.add_section(f'layer{i}')
            self.config.set(f'layer{i}', 'thick_m',
                            str(layers[i].thick_m))
            self.config.set(f'layer{i}', 'type',
                            layers[i].layer_type)
            if (layers[i].layer_type == 'CW'):
                self.config.set(f'layer{i}', 'muinf_Hz',
                                str(layers[i].muinf_Hz))
                self.config.set(f'layer{i}', 'k_Hz',
                                str(layers[i].k_Hz))
                self.config.set(f'layer{i}', 'sigmaDC',
                                str(layers[i].sigmaDC))
                self.config.set(f'layer{i}', 'epsr',
                                str(layers[i].epsr))
                self.config.set(f'layer{i}', 'tau',
                                str(layers[i].tau))
                self.config.set(f'layer{i}', 'RQ',
                                str(layers[i].RQ))
        self.config.add_section(f'boundary')
        self.config.set(f'boundary', 'type',
                        layers[i].layer_type)
        if (layers[i].layer_type == 'CW'):
            self.config.set(f'boundary', 'muinf_Hz',
                            str(layers[i].muinf_Hz))
            self.config.set(f'boundary', 'k_Hz',
                            str(layers[i].k_Hz))
            self.config.set(f'boundary', 'sigmaDC',
                            str(layers[i].sigmaDC))
            self.config.set(f'boundary', 'epsr',
                            str(layers[i].epsr))
            self.config.set(f'boundary', 'tau',
                            str(layers[i].tau))
            self.config.set(f'boundary', 'RQ',
                            str(layers[i].RQ))

    def save_beam(self, beam):
        self.config.add_section('beam_info')
        self.config.set(f'beam_info', 'test_beam_shift',
                        str(beam.test_beam_shift))
        self.config.set(f'beam_info', 'betarel',
                        str(beam.betarel))
        self.config.set(f'beam_info', 'gammarel',
                        str(beam.gammarel))
        self.config.set(f'beam_info', 'mass_MeV_c2',
                        str(beam._m_MeV_c2))
        self.config.set(f'beam_info', 'Ekin_MeV',
                        str(beam.Ekin_MeV))
        self.config.set(f'beam_info', 'p_MeV_c',
                        str(beam.p_MeV_c))

    def save_freq(self, freq):
        try:
            freq.filename
            self.config.add_section('frequency_file')
        except AttributeError:
            self.config.add_section('frequency_info')
        if self.config.has_section('frequency_file'):
            self.config.set('frequency_file', 'filename', freq.filename)
            self.config.set('frequency_file', 'freq_column',
                            str(freq.freq_column))
            self.config.set('frequency_file', 'skipped_rows',
                            str(freq.skipped_rows))
        else:
            self.config.set('frequency_info', 'fmin', str(int(freq.fmin)))
            self.config.set('frequency_info', 'fmax', str(int(freq.fmax)))
            self.config.set('frequency_info', 'fstep', str(int(freq.fstep)))

    def save_calc(self, list_calc):
        self.list_output = []
        self.config.add_section('output')
        for imped in list_calc:
            self.config.set(f'output', imped,
                            str(list_calc[imped]))
            if list_calc[imped] is True:
                self.list_output.append(imped)

    def save_output(self, list_output):
        i = 1
        while self.config.has_section('output' + str(i)):
            print(i)

    def read_beam(self, cfg_file=None):
        if cfg_file is not None:
            self.read_cfg(cfg_file)
        if self.config.has_section('beam_info') is False:
            return None
        test_beam_shift = self.config.getfloat('beam_info', 'test_beam_shift')
        if self.config.has_option('beam_info', 'betarel'):
            betarel = self.config.getfloat('beam_info', 'betarel')
            if self.config.has_option('beam_info', 'mass_MeV_c2'):
                mass_MeV_c2 = self.config.getfloat('beam_info', 'mass_MeV_c2')
                beam = pytlwall.Beam(betarel=betarel,
                                     test_beam_shift=test_beam_shift,
                                     mass_MeV_c2=mass_MeV_c2)
            else:
                beam = pytlwall.Beam(betarel=betarel,
                                     test_beam_shift=test_beam_shift)
            return beam
        if self.config.has_option('beam_info', 'gammarel'):
            gammarel = self.config.getfloat('beam_info', 'gammarel')
            if self.config.has_option('beam_info', 'mass_MeV_c2'):
                mass_MeV_c2 = self.config.getfloat('beam_info', 'mass_MeV_c2')
                beam = pytlwall.Beam(gammarel=gammarel,
                                     test_beam_shift=test_beam_shift,
                                     mass_MeV_c2=mass_MeV_c2)
            else:
                beam = pytlwall.Beam(gammarel=gammarel,
                                     test_beam_shift=test_beam_shift)
            return beam
        if self.config.has_option('beam_info', 'Ekin_MeV'):
            Ekin_MeV = self.config.getfloat('beam_info', 'Ekin_MeV')
            if self.config.has_option('beam_info', 'mass_MeV_c2'):
                mass_MeV_c2 = self.config.getfloat('beam_info', 'mass_MeV_c2')
                beam = pytlwall.Beam(Ekin_MeV=Ekin_MeV,
                                     test_beam_shift=test_beam_shift,
                                     mass_MeV_c2=mass_MeV_c2)
            else:
                beam = pytlwall.Beam(Ekin_MeV=Ekin_MeV,
                                     test_beam_shift=test_beam_shift)
            return beam
        if self.config.has_option('beam_info', 'p_MeV_c'):
            p_MeV_c = self.config.getfloat('beam_info', 'p_MeV_c')
            if self.config.has_option('beam_info', 'mass_MeV_c2'):
                mass_MeV_c2 = self.config.getfloat('beam_info', 'mass_MeV_c2')
                beam = pytlwall.Beam(p_MeV_c=p_MeV_c,
                                     test_beam_shift=test_beam_shift,
                                     mass_MeV_c2=mass_MeV_c2)
            else:
                beam = pytlwall.Beam(p_MeV_c=p_MeV_c,
                                     test_beam_shift=test_beam_shift)
            return beam

    def read_output(self, cfg_file=None):
        output_list = ['ZLong',
                       'ZTrans',
                       'ZDipX',
                       'ZDipY',
                       'ZQuadX',
                       'ZQuadY',
                       'ZLongSurf',
                       'ZTransSurf',
                       'ZLongDSC',
                       'ZLongISC',
                       'ZTransDSC',
                       'ZTransISC'
                       ]
        self.list_output = []
        self.file_output = {}
        self.img_output = {}
        if cfg_file is not None:
            self.read_cfg(cfg_file)

        for imped in output_list:
            if (self.config.has_option('output', imped) and
               self.config.getboolean('output', imped) is True):
                self.list_output.append(imped)
        i = 1
        while self.config.has_section('output' + str(i)):
            section = 'output' + str(i)
            filename = self.config.get(section, 'output_name')
            self.file_output[filename] = {}
            self.file_output[filename]['imped'] = []
            if (self.config.has_option(section, 'use_name_flag') and
               self.config.getboolean(section, 'use_name_flag') is True):
                self.file_output[filename]['prefix'] = \
                     self.config.get('base_info', 'component_name')
            else:
                self.file_output[filename]['prefix'] = ''
            imped_list = self.config.get(section, 'output_list').split(',')
            for imped in imped_list:
                imped = imped.strip()
                self.file_output[filename]['imped'].append(imped.strip())
            i += 1

        i = 1
        while self.config.has_section('img_output' + str(i)):
            section = 'img_output' + str(i)
            filename = self.config.get(section, 'img_name')
            self.img_output[filename] = {}
            self.img_output[filename]['imped'] = []
            if (self.config.has_option(section, 'use_name_flag') and
               self.config.getboolean(section, 'use_name_flag') is True):
                self.img_output[filename]['prefix'] = \
                     self.config.get('base_info', 'component_name')
            else:
                self.img_output[filename]['prefix'] = ''
            if (self.config.has_option(section, 're_im_flag') and
               (self.config.get(section, 're_im_flag').lower() == 'real' or
               (self.config.get(section, 're_im_flag').lower() == 'imag'))):
                self.img_output[filename]['real_imag'] = \
                     self.config.get(section, 're_im_flag').lower()
            else:
                self.img_output[filename]['real_imag'] = 'both'
            if self.config.has_option(section, 'title'):
                self.img_output[filename]['title'] = \
                    self.config.get(section, 'title')
            else:
                self.img_output[filename]['title'] = None
            if self.config.has_option(section, 'xscale'):
                self.img_output[filename]['xscale'] = \
                    self.config.get(section, 'xscale')
            else:
                self.img_output[filename]['xscale'] = 'lin'
            if self.config.has_option(section, 'yscale'):
                self.img_output[filename]['yscale'] = \
                    self.config.get(section, 'yscale')
            else:
                self.img_output[filename]['yscale'] = 'lin'
            imped_list = self.config.get(section, 'imped_list').split(',')
            for imped in imped_list:
                imped = imped.strip()
                self.img_output[filename]['imped'].append(imped.strip())
            i += 1

        return

    def read_pytlwall(self, cfg_file=None):
        if cfg_file is not None:
            self.read_cfg(cfg_file)
        chamber = self.read_chamber()
        beam = self.read_beam()
        freq = self.read_freq()

        if chamber is not None and beam is not None and freq is not None:
            mywall = pytlwall.TlWall(chamber, beam, freq)
            return mywall

    def read_cfg(self, cfg_file):
        myfile = Path(cfg_file)
        if myfile.exists():
            self.config.read(cfg_file)
        else:
            print('The file %s does not exist, try again!' % cfg_file)

    def calc_wall(self):
        self.myimped = {}
        self.mywall = self.read_pytlwall()
        for imped in self.list_output:
            self.myimped[imped] = getattr(self.mywall, imped)

    def print_wall(self):
        for output_file in self.file_output.keys():
            try:
                prefix = self.file_output[output_file]['prefix']
            except KeyError:
                if(self.file_output[output_file]['prefix_flag'] is True):
                    prefix = ''
                    # ~ self.config.get('base_info', 'component_name')
                else:
                    prefix = ''
            _, ext = output_file.split('.')
            if ('re_im_flag' in self.file_output[output_file].keys() and
               self.file_output[output_file]['re_im_flag'] == 'real'):
                data = self.collect_real_output(output_file, prefix)
            elif ('re_im_flag' in self.file_output[output_file] and
                  self.file_output[output_file]['re_im_flag'] == 'imag'):
                data = self.collect_imag_output(output_file, prefix)
            else:
                data = self.collect_both_output(output_file, prefix)
            df = pd.DataFrame.from_dict(data)
            if ext == 'xlsx':
                df.to_excel(output_file, index=False)
            else:
                df.to_csv(output_file, index=None, sep='\t', mode='w')

    def collect_real_output(self, output_file, prefix):
        data = {}
        data['f  [Hz] '] = self.mywall.f
        for imped in self.file_output[output_file]['imped']:
            unit = '[Ohm/m]' if imped.find('ong') == -1 else '[Ohm]'
            data[prefix + ' ' + imped + ' real ' + unit] = \
                self.myimped[imped].real
        return data

    def collect_imag_output(self, output_file, prefix):
        data = {}
        data['f  [Hz] '] = self.mywall.f
        for imped in self.file_output[output_file]['imped']:
            unit = '[Ohm/m]' if imped.find('ong') == -1 else '[Ohm]'
            data[prefix + ' ' + imped + ' imag ' + unit] = \
                self.myimped[imped].imag
        return data

    def collect_both_output(self, output_file, prefix):
        data = {}
        data['f  [Hz] '] = self.mywall.f
        for imped in self.file_output[output_file]['imped']:
            unit = '[Ohm/m]' if imped.find('ong') == -1 else '[Ohm]'
            data[prefix + ' ' + imped + ' real ' + unit] = \
                self.myimped[imped].real
            data[prefix + ' ' + imped + ' imag ' + unit] = \
                self.myimped[imped].imag
        return data

    def plot_wall(self):
        for img_file in self.img_output.keys():
            savename = img_file
            try:
                prefix = self.img_output[img_file]['prefix']
            except KeyError:
                if(self.img_output[img_file]['prefix_flag'] is True):
                    prefix = ''
                    # ~ self.config.get('base_info', 'component_name')
                else:
                    prefix = ''
            title = self.img_output[img_file]['title']
            xscale = self.img_output[img_file]['xscale']
            yscale = self.img_output[img_file]['yscale']
            list_f = []
            list_imped = []
            list_label = []
            f = self.mywall.f
            for imped in self.img_output[img_file]['imped']:
                if self.img_output[img_file]['real_imag'] != 'imag':
                    list_imped.append(self.myimped[imped].real)
                    list_label.append(prefix + ' ' + imped + ' real ')
                if self.img_output[img_file]['real_imag'] != 'imag':
                    list_imped.append(self.myimped[imped].imag)
                    list_label.append(prefix + ' ' + imped + ' imag ')
            if imped.find('ong') != -1:
                imped_type = 'L'
            else:
                imped_type = 'T'
            plot.plot_list_Z_vs_f(f=f,
                                  list_Z=list_imped, list_label=list_label,
                                  imped_type=imped_type, title=title,
                                  savename=savename,
                                  xscale=xscale, yscale=yscale)
