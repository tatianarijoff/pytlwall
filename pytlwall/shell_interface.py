# This module contains all the pytlwall function for a shell use
from pathlib import Path
import scipy.constants as const
import pytlwall
import pytlwall.txt_util as txt_u
prot_mass = const.physical_constants['proton mass energy equivalent in MeV'][0]


def welcome_message():
    print(" ")
    print("*************************************************************")
    print("*     PyTLWall                                              *")
    print("*                                                           *")
    print("*  C. Zannini and T. Rijoff                                 *")
    print("*************************************************************")


def help_pytlwall():
    print(" usage: ")
    print("       exec_pytlwall -a cfg_file  -- to  read information from"
          " config file  ")
    print("       exec_pytlwall -i  -- for interactive mode            ")
    print("       exec_pytlwall -g  -- for graphic interface            ")
    print(" ")


def menu0_pytlwall():
    print('==================================================================')
    print('TlWall main menu')
    print('==================================================================')
    print('chamber == Define accelerator chamber ')
    print('beam == Define beam characteristics ')
    print('freq == Define frequency range ')
    print('config == Read all the info from a config')


def menu1_pytlwall():
    print('calc == Calculate impedance')
    print('sav == Save impedance')
    print('plot == Plot Impedance')


def menu2_pytlwall():
    print('sav_conf == Save configuration file')


def menuX_pytlwall():
    print('X == Exit')
    print('==================================================================')


def submenu_chamber():
    print('................................................................')
    print('TlWall chamber menu')
    print('Insert the chamber information')
    print('................................................................')
    print('name == define component name (optional)')
    print('shape == chamber shape')
    print('len == pipe length in meters')
    print('radius == radius in meters')
    print('hor == horizontal dimension in meters')
    print('ver == vertical dimension in meters')
    print('betax == horizontal beta')
    print('betay == vertical beta')
    print('layer == layer details')
    print('back == come back to the previous menu')
    print('................................................................')



def submenu_layer(boundary, layer_type, layer_nbr):
    print('................................................................')
    print('TlWall layer menu')
    print(f'Insert the layer {layer_nbr} information')
    print('................................................................')
    if boundary is False:
        print('thickness == define layer thikness in meters')
    print('kind == kind of layer (conductive wall, vacuum, perfect conductive '
          'electric ')
    if layer_type == 'CW':
        print('mu == mu infinity in Hz ')
        print('k == relaxation frequency for permeability ')
        print('sigmaDC == DC conductivity in S/m ')
        print('epsr == real relative permittivity ')
        print('tau == relaxation time for permittivity in seconds ')

    print('back == come back to the previous menu')
    print('................................................................')


def submenu_beam():
    print('................................................................')
    print('TlWall beam menu')
    print('Insert beam information')
    print('................................................................')
    print('beta == relativistic beta')
    print('gamma == relativistic gamma')
    print('mass == beam particles mass in Mev/c^2')
    print('p == beam momentum in MeV/c')
    print('Ekin == kinetic energy in MeV')
    print('shift == The distance between test and beam particle in meters')
    print('back == come back to the previous menu')
    print('................................................................')


def submenu_freq():
    print('................................................................')
    print('TlWall freq menu')
    print('Insert frequencies at which to calculate the impedance')
    print('................................................................')
    print('file == read frequency from file')
    print('lim == define minimum, maximum and frequency step')
    print('back == come back to the previous menu')
    print('................................................................')


def submenu_calc(list_calc):
    print('................................................................')
    print('TlWall calc')
    print('................................................................')
    for imped in list_calc.keys():
        if list_calc[imped] is True:
            string = f'(+) {imped}'
        else:
            string = f'( ) {imped}'
        print(string)
    print('back == come back to the previous menu')
    print('................................................................')


def submenu_print():
    print('................................................................')
    print('TlWall sav file')
    print('................................................................')
    print('new == New file')
    print('back == come back to the previous menu')
    print('................................................................')


def submenu_plot():
    print('................................................................')
    print('TlWall plot')
    print('................................................................')
    print('new == New image')
    print('back == come back to the previous menu')
    print('................................................................')


def submenu_print_plot(list_calc):
    for imped in list_calc.keys():
        if list_calc[imped] is True:
            string = f'(+) {imped}'
        else:
            string = f'( ) {imped}'
        print(string)
    print('back == come back to the previous menu')
    print('................................................................')


def layer_interface(boundary, layer_nbr):
    layer = pytlwall.Layer()
    choice = ''
    while choice.lower() != 'back' and choice.lower() != 'x':
        submenu_layer(boundary, layer.layer_type, layer_nbr)
        choice = input('Your choice ')
        if choice == 'thickness':
            choice2 = input(f'What is the layer thickness? ')
            try:
                layer.thick_m = float(choice2)
            except ValueError:
                print(f'Value used {layer.thick_m}')
        elif choice == 'kind':
            if boundary is False:
                choice2 = input('What is the material? (possible values "CW" '
                                '(conductive wall, DEFAULT)  "V" (Vacuum)'
                                ' "PEC" (Perfect electric conductor) )')
                if choice2.upper() == 'V' or choice2.upper == 'PEC':
                    layer.layer_type = choice2.upper()
                else:
                    layer.layer_type = 'CW'
            else:
                choice2 = input('What is the material? (possible values "V" '
                                '(vacuum, DEFAULT)  "CW" (Conductive Wall)'
                                ' "PEC" (Perfect electric conductor) )')
                if choice2.upper() == 'CW' or choice2.upper == 'PEC':
                    layer.layer_type = choice2.upper()
                else:
                    layer.layer_type = 'V'
        elif choice == 'mu':
            choice2 = input(f'What is the layer {i} mu infinity in Hz? ')
            try:
                layer.muinf_Hz = float(choice2)
            except ValueError:
                print(f'Value used {layers.muinf_Hz}')
        elif choice == 'k':
            choice2 = input('What is the relaxation frequency for '
                           'permeability in Hz ZERO NOT ALLOWED ? ')
            try:
                value = float(choice2)
                if value != 0:
                    layer.k_Hz = value
            except ValueError:
                print(f'Value used {layer.k_Hz}')
        elif choice == 'sigmaDC':
            choice2 = input('What is DC conductivity in S/m '
                            ' INFINITY NOT ALLOWED ? ')
            try:
                value = float(choice2)
                if value != float('inf'):
                    layer.sigmaDC = value
            except ValueError:
                print(f'Value used {layer.sigmaDC}')
        elif choice == 'epsr':
            choice2 = input('What is the real relative permittivity? ')
            try:
                layer.epsr = float(choice2)
            except ValueError:
                print(f'Value used {layer.epsr}')
        elif choice == 'tau':
            choice2 = input('What is the relaxation time for '
                                   'permittivity in seconds? ')
            try:
                layer.tau = float(choice2)
            except ValueError:
                print(f'Value used {layer.tau}')
        elif choice == 'RQ':
            choice2 = input('What is the RQ value ')
            try:
                layer.RQ = float(choice2)
            except ValueError:
                print(f'Value used {layer.RQ}')
    return layer


def chamber_interface():
    choice = ''
    chamber = pytlwall.Chamber()
    while choice.lower() != 'back' and choice.lower() != 'x':
        submenu_chamber()
        choice = input('Your choice: ')
        if choice.lower() == 'name':
            choice = input('insert component name ')
            chamber.component_name = choice
            print(f'Component name {chamber.component_name}')
        elif choice.lower() == 'shape':
            choice = input('what is chamber shape (allowed values= CIRCULAR'
                           ' (default), ELLIPTICAL, RECTANGULAR ')
            if (choice.upper() == 'ELLIPTICAL'
               or choice.upper() == 'RECTANGULAR'):
                chamber.chamber_shape = choice.upper()
            print(f'Used chamber shape {chamber.chamber_shape}')
        elif choice.lower() == 'len':
            choice = input('what is chamber len in meters ')
            try:
                chamber.pipe_len_m = float(choice)
            except ValueError:
                pass
            print(f'Used chamber len {chamber.pipe_len_m}')
        elif choice.lower() == 'radius':
            choice = input('what is chamber radius in meters ')
            try:
                chamber.pipe_rad_m = float(choice)
            except ValueError:
                pass
            print(f'Used chamber radius {chamber.pipe_rad_m}')
        elif choice.lower() == 'hor':
            choice = input('what is chamber horizontal dimension in meters ')
            try:
                chamber.pipe_hor_m = float(choice)
            except ValueError:
                pass
            print(f'Used chamber horizontal dimension {chamber.pipe_hor_m}')
        elif choice.lower() == 'ver':
            choice = input('what is chamber vertical dimension in meters ')
            try:
                chamber.pipe_ver_m = float(choice)
            except ValueError:
                pass
            print(f'Used chamber vertical dimension {chamber.pipe_ver_m}')
        elif choice.lower() == 'betax':
            choice = input('what is horizontal beta ')
            try:
                chamber.betax = float(choice)
            except ValueError:
                pass
            print(f'Used horizontal beta {chamber.betax}')
        elif choice.lower() == 'betay':
            choice = input('what is vertical beta ')
            try:
                chamber.betax = float(choice)
            except ValueError:
                pass
            print(f'Used vertical beta {chamber.betay}')
        elif choice.lower() == 'layer':
            choice = input('How many layers does the chamber have '
                               '(not counting the boundary) ')
            try:
                nbr_layer = int(choice)
            except ValueError:
                nbr_layer = 1
            for i in range(nbr_layer):
                layer = layer_interface(boundary=False, layer_nbr=i)
                chamber.layers.append(layer)
            i = i + 1
            layer = layer_interface(boundary=True, layer_nbr=i)
            chamber.layers.append(layer)
    return chamber


def beam_interface():
    choice = ''
    beam = pytlwall.Beam()
    while choice.lower() != 'back' and choice.lower() != 'x':
        submenu_beam()
        choice = input('Your choice: ')
        if choice.lower() == 'beta':
            choice = input('Insert beta value ')
            try:
                value = float(choice)
            except ValueError:
                    print(f'Value used {beam.betarel}')
            if value > 0 and value < 1:
                beam.betarel = value
            else:
                print(f'Beta must be between 0 and 1, value used '
                      f' {beam.betarel}')
        elif choice.lower() == 'gamma':
            choice = input('Insert gamma value ')
            try:
                value = float(choice)
            except ValueError:
                    print(f'Value used {beam.gammarel}')
            if value > 0:
                beam.gammarel = value
            else:
                print(f'Gamma must be greater than 0, used value '
                      f' {beam.gammarel}')
        elif choice.lower() == 'mass':
            choice = input(f'Insert mass value, default = {prot_mass}')
            try:
                value = float(choice)
            except ValueError:
                    print(f'Value used {beam._m_MeV_c2}')
            if value > 0:
                beam._m_MeV_c2 = value
            else:
                print(f'Mass must be greater than 0, used value '
                      f' {beam._m_MeV_c2}')
        elif choice.lower() == 'p':
            choice = input('Insert momentum value in MeV/c ')
            try:
                value = float(choice)
            except ValueError:
                    print(f'Value used {beam.p_MeV_c}')
            if value > 0:
                beam.p_MeV_c = value
            else:
                print(f'Momentum must be greater than 0, used value '
                      f' {beam.p_MeV_c}')
        elif choice.lower() == 'ekin':
            choice = input('Insert kinetic energy value in MeV ')
            try:
                value = float(choice)
            except ValueError:
                    print(f'Value used {beam.Ekin_MeV}')
            if value > 0:
                beam.Ekin_MeV = value
            else:
                print(f'Kinetic energy must be greater than 0, used value '
                      f' {beam.Ekin_MeV}')
        elif choice.lower() == 'shift':
            choice = input('Insert beam test shift in meters ')
            try:
                value = float(choice)
            except ValueError:
                    print(f'Value used {beam.Ekin_MeV}')
            if value > 0:
                beam.test_beam_shift = value
            else:
                print(f'The shift must be greater than 0, used value '
                      f' {beam.test_beam_shift}')
    return beam


def freq_interface():
    choice = ''
    freq = None
    while choice.lower() != 'back' and choice.lower() != 'x':
        submenu_freq()
        choice = input('Your choice: ')
        if choice.lower() == 'lim':
            choice = input('insert exponential lower limit ')
            try:
                fmin = int(choice)
            except ValueError:
                print(f'{choice} is not a valid exponent')
                fmin = 0
                print(f'Used {fmin}')
            choice = input('insert exponential upper limit ')
            try:
                fmax = int(choice)
            except ValueError:
                print(f'{choice} is not a valid exponent')
                fmax = 8
                print(f'Used {fmax}')
            choice = input('insert exponential step ')
            try:
                fstep = int(choice)
            except ValueError:
                print(f'{choice} is not a valid exponent')
                fstep = 2
                print(f'Used {fstep}')
            freq = pytlwall.Frequencies(fmin=fmin, fmax=fmax, fstep=fstep)
        elif choice.lower() == 'file':
            choice = input('insert filename ')
            myfile = Path(choice)
            if myfile.exists():
                choice2 = input('At which column are the frequencies? (first '
                                'column=0)  ')
                try:
                    col = int(choice2)
                except ValueError:
                    print(f'{choice2} is not a valid number')
                    col = 0
                    print(f'Used {col}')
                choice2 = input('How many row to skip (default 0)  ')
                try:
                    row = int(choice2)
                except ValueError:
                    row = 0
                    print(f'Used {row}')
                freq_list = txt_u.read_frequency_txt(choice, column=col,
                                                     skipped_rows=row)
                freq = pytlwall.Frequencies(freq_list=freq_list)
                freq.filename = choice
                freq.freq_column = col
                freq.skipped_rows = row
            else:
                print('*********************************************')
                print('Wrong filename, please try again')
                print('*********************************************')
    return freq


def calc_interface():
    choice = ''
    list_calc = {'ZLong': True,
                 'ZTrans': False,
                 'ZDipX': False,
                 'ZDipY': False,
                 'ZQuadX': False,
                 'ZQuadY': False,
                 'ZLongSurf': False,
                 'ZTransSurf': False,
                 'ZLongDSC': False,
                 'ZLongISC': False,
                 'ZTransDSC': False,
                 'ZTransISC': False}

    while (choice.lower() != 'back' and choice.lower() != 'x' and 
          choice.lower() != 'end'):
        submenu_calc(list_calc)
        choice = input('Your choice: ')
        if choice in list_calc.keys():
            list_calc[choice] = True
    return list_calc


def sav_interface(list_calc):
    choice = ''
    file_output = {}
    list_sav = {key: value for key, value in list_calc.items() 
                if value is True}
    while (choice.lower() != 'back' and choice.lower() != 'x' and 
          choice.lower() != 'end'):
        submenu_print()
        choice = input('Your choice ')
        if choice.lower() == 'new':
            list_sav = dict.fromkeys(list_sav, False)
            choice = input('Print the name of the file where to save the data.'
                           ' (with the directory and extension) ')
            file_output[choice] = {}
            file_output[choice]['re_im_flag'] = ''
            file_output[choice]['prefix_flag'] = False
            file_output[choice]['imped'] = []
            choice2 = ''
            while (choice2.lower() != 'back' and choice2.lower() != 'x' and 
                choice2.lower() != 'end'):
                submenu_print_plot(list_sav)
                choice2 = input('What do you want to save in the file? ')
                if choice2 in list_sav.keys():
                    list_sav[choice2] = True
                    file_output[choice]['imped'].append(choice2)
            choice2 = input('Do you want to save the real part of the '
                           ' impedance, the imaginary part or both '
                           ' (default)?  ')
            if choice2.lower() == 'real':
                file_output[choice]['re_im_flag'] == 'real'
            if choice2.lower() == 'imag':
                file_output[choice]['re_im_flag'] == 'imag'
            else:
                file_output[choice]['re_im_flag'] == 'both'
            choice2 = input('Do you want to insert the component name in '
                           'the saved variables? (y, N)')
            if choice2.lower == 'Y':
                file_output[choice]['prefix_flag'] is True

    return file_output


def plot_interface(list_calc):
    choice = ''
    img_output = {}
    list_sav = {key: value for key, value in list_calc.items() 
                if value is True}
    while (choice.lower() != 'back' and choice.lower() != 'x' and 
          choice.lower() != 'end'):
        submenu_print()
        choice = input('Your choice ')
        if choice.lower() == 'new':
            list_sav = dict.fromkeys(list_sav, False)
            choice = input('Print the name of the file where to save the data.'
                           ' (with the directory and extension) ')
            img_output[choice] = {}
            img_output[choice]['real_imag'] = ''
            img_output[choice]['prefix_flag'] = False
            img_output[choice]['title'] = ''
            img_output[choice]['xscale'] = 'lin'
            img_output[choice]['yscale'] = ''
            img_output[choice]['imped'] = []
            choice2 = ''
            while (choice2.lower() != 'back' and choice2.lower() != 'x' and 
                choice2.lower() != 'end'):
                submenu_print_plot(list_sav)
                choice2 = input('What do you want to save in the file? ')
                if choice2 in list_sav.keys():
                    list_sav[choice2] = True
                    img_output[choice]['imped'].append(choice2)
            choice2 = input('Do you want to save the real part of the '
                           ' impedance, the imaginary part or both '
                           ' (default)?  ')
            if choice2.lower() == 'real':
                img_output[choice]['real_imag'] == 'real'
            if choice2.lower() == 'imag':
                img_output[choice]['real_imag'] == 'imag'
            else:
                img_output[choice]['real_imag'] == 'both'
            choice2 = input('Do you want to insert the component name in '
                           'the saved variables? (y, N)')
            if choice2.lower == 'Y':
                img_output[choice]['prefix_flag'] is True
            choice2 = input('What is image title (if any, default enter)')
            img_output[choice]['title'] = choice2
            choice2 = input('What is the image horizontal scale (lin'
                            ' DEFAULT, log, symlog)')
            if choice2.lower() == 'log' or choice2.lower() == 'symlog':
                img_output[choice]['xscale'] = choice2
            choice2 = input('What is the image vertical scale (lin'
                            ' DEFAULT, log, symlog)')
            if choice2.lower() == 'log' or choice2.lower() == 'symlog':
                img_output[choice]['yscale'] = choice2
    return img_output
