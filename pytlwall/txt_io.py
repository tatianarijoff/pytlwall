'''
@authors: Tatiana Rijoff,
          Carlo Zannini
@date:    01/03/2013
@copyright CERN
'''
import os
import pytlwall


class TxtIo(object):
    def save_ZLong(self, savedir, savename, f, ZLong, out_label):
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

    def save_ZTrans(self, savedir, savename, f, ZTrans, out_label):
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

    def save_ZAllTrans(self, savedir, savename, f, ZDipX, ZDipY, ZQuadX,
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

    def save_Zgeneric(self, savedir, savename, f, list_Z, list_label,
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

    def read_frequency_txt(self, filename, separator='', column=0,
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
        elif unit =='GHz':
            mult = 1e9
        elif unit =='MHz':
            mult = 1e6
        elif unit =='kHz':
            mult = 1e3
        else:
            mult = 1
        # we need to distinguish the default separator from other possibilities
        if separator is '':
            for line in data:
                row = line.split()
                freq.append(mult * float(row[column]))
        else:
            for line in data:
                row = line.split(separator)
                freq.append(mult * float(row[column]))

        return freq
