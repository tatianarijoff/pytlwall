'''
@authors: Tatiana Rijoff,
          Carlo Zannini
@date:    01/03/2013
@copyright CERN

The txt_util module gives you some lazy functions to read and write txt
input and output for tlwall

'''
import os
import pytlwall


def save_ZLong(savedir, savename, f, ZLong, out_label):
    print('Saving %s data in %s' % (out_label, savename))
    try:
        fd = open(savedir + savename, 'w')
    except IOError:
        os.makedirs(savedir)
        fd = open(savedir + savename, 'w')
    fd.write('{0:^20s} {1:^20s} {2:^20s}\n'.format('f', 'ZLong.real',
                                                   'ZLong.imaginary'))
    fd.write('{0:^20s} {1:^20s} {2:^20s}\n'.format('[Hz]', '[Ohm]',
                                                   '[Ohm]'))
    for i in range(len(f)):
        fd.write('{0:20e} {1:20e} {2:20e}\n'.format(f[i], ZLong[i].real,
                                                    ZLong[i].imag))
    fd.close()


def save_ZTrans(savedir, savename, f, ZTrans, out_label):
    print('Saving %s data in %s' % (out_label, savename))
    try:
        fd = open(savedir + savename, 'w')
    except IOError:
        os.makedirs(savedir)
        fd = open(savedir + savename, 'w')
    fd.write('{0:^20s} {1:^20s} {2:^20s}\n'.format('f', 'ZTrans.real',
                                                   'ZTrans.imaginary'))
    fd.write('{0:^20s} {1:^20s} {2:^20s}\n'.format('[Hz]', '[Ohm/m]',
                                                   '[Ohm/m]'))
    for i in range(len(f)):
        fd.write('{0:20e} {1:20e} {2:20e}\n'.format(f[i], ZTrans[i].real,
                                                    ZTrans[i].imag))
    fd.close()


def save_ZAllTrans(savedir, savename, f, ZDipX, ZDipY, ZQuadX,
                   ZQuadY, out_label):
    print('Saving %s data in %s' % (out_label, savename))
    try:
        fd = open(savedir + savename, 'w')
    except IOError:
        os.makedirs(savedir)
        fd = open(savedir + savename, 'w')
    fd.write('{0:^20s} {1:^20s} {2:^20s} {3:^20s} {4:^20s} '
             '{5:^20s} {6:^20s} {7:^20s} {8:^20s} \n'
             .format('f', 'ZDipX.real', 'ZDipX.imaginary', 'ZDipY.real',
                     'ZDipY.imaginary', 'ZQuadX.real', 'ZQuadX.imaginary',
                     'ZQuadY.real', 'ZQuadY.imaginary'))
    fd.write('{0:^20s} {1:^20s} {2:^20s} {3:^20s} {4:^20s} '
             '{5:^20s} {6:^20s} {7:^20s} {8:^20s} \n'
             .format('[Hz]', '[Ohm/m]', '[Ohm/m]', '[Ohm/m]', '[Ohm/m]',
                     '[Ohm/m]', '[Ohm/m]', '[Ohm/m]', '[Ohm/m]'))

    for i in range(len(f)):
        fd.write('{0:20e} {1:20e} {2:20e} {3:20e} {4:20e} '
                 '{5:20e} {6:20e} {7:20e} {8:20e} \n'
                 .format(f[i], ZDipX[i].real, ZDipX[i].imag, ZDipY[i].real,
                         ZDipY[i].imag, ZQuadX[i].real, ZQuadX[i].imag,
                         ZQuadY[i].real, ZQuadY[i].imag))
    fd.close()


def save_Zgeneric(savedir, savename, f, list_Z, list_label,
                  list_unit, out_label):
    print('Saving %s data in %s' % (out_label, savename))
    try:
        fd = open(savedir + savename, 'w')
    except IOError:
        os.makedirs(savedir)
        fd = open(savedir + savename, 'w')
    fd.write('{0:^20s}'.format(f))
    for i in range(len(list_label)):
        fd.write('{0:^20s}'.format(list_label[i]))
    fd.write('\n')
    for i in range(len(list_unit)):
        fd.write('{0:^20s}'.format(list_unit[i]))
    for i in range(len(f)):
        fd.write('{0:20e}'.format(f[i]))
        for j in range(len(list_Z)):
            fd.write('{0:20e}'.format(list_Z[j][i]))
        fd.write('\n')
    fd.close()


def read_frequency_txt(filename, separator='', column=0,
                       skipped_rows=0, unit='Hz'):
    freq = []
    print(filename)
    fd = open(filename, 'r')
    for i in range(skipped_rows):
        fd.readline()
    data = fd.readlines()
    fd.close()
    # define multiplication factor
    if unit == 'THz':
        mult = 1e12
    elif unit == 'GHz':
        mult = 1e9
    elif unit == 'MHz':
        mult = 1e6
    elif unit == 'kHz':
        mult = 1e3
    else:
        mult = 1
    # we need to distinguish the default separator from other possibilities
    if separator == '':
        for line in data:
            row = line.split()
            freq.append(mult * float(row[column]))
    else:
        for line in data:
            row = line.split(separator)
            freq.append(mult * float(row[column]))

    return freq


def load_apertype(filename):
    list_apertype = []
    with open(filename, 'r') as f:
        list_apertype = f.read().splitlines()
    return list_apertype


def load_b_L(filename):
    list_pipe_radius = []
    list_pipe_len = []
    with open(filename) as f:
        lines = f.readlines()
    for line in lines:
        pipe_radius, pipe_len = line.split()
        list_pipe_radius.append(float(pipe_radius))
        list_pipe_len.append(float(pipe_len))
    return list_pipe_radius, list_pipe_len


def load_b_L_betax_betay(filename):
    list_pipe_radius = []
    list_pipe_len = []
    list_betax = []
    list_betay = []
    with open(filename) as f:
        lines = f.readlines()
    for line in lines:
        if len(line.strip()) == 0:
            continue
        pipe_radius, pipe_len, betax, betay = line.split()
        list_pipe_radius.append(float(pipe_radius))
        list_pipe_len.append(float(pipe_len))
        list_betax.append(float(betax))
        list_betay.append(float(betay))
    return list_pipe_radius, list_pipe_len, list_betax, list_betay


def load_x_y_L_betax_betay(filename):
    list_pipe_hor = []
    list_pipe_ver = []
    list_pipe_len = []
    list_betax = []
    list_betay = []
    with open(filename) as f:
        lines = f.readlines()
    for line in lines:
        if len(line.strip()) == 0:
            continue
        pipe_hor, pipe_ver, pipe_len, betax, betay = line.split()
        list_pipe_hor.append(float(pipe_hor))
        list_pipe_ver.append(float(pipe_ver))
        list_pipe_len.append(float(pipe_len))
        list_betax.append(float(betax))
        list_betay.append(float(betay))
    return list_pipe_hor, list_pipe_ver, list_pipe_len,\
        list_betax, list_betay
