'''
@authors: Tatiana Rijoff,
          Carlo Zannini
@date:    01/03/2013
@copyright CERN
'''
import os
import pytlwall


class TxtIo(object):
    def save_ZLong(self, filedir, filename, f, ZLong, out_label):
        print('Saving %s data in %s' % (out_label, filename))
        try:
            fd = open(filedir + filename, 'w')
        except IOError:
            os.makedirs(savedir)
            fd = open(filedir + filename, 'w')
        fd.write('{0:^20s} {1:^20s} {2:^20s}\n'.format('f', 'ZLong.real',
                                                       'ZLong.imaginary'))
        fd.write('{0:^20s} {1:^20s} {2:^20s}\n'.format('[Hz]', '[Ohm]',
                                                       '[Ohm]'))
        for i in range(len(f)):
            fd.write('{0:20e} {1:20e} {2:20e}\n'.format(f[i], ZLong[i].real,
                                                        ZLong[i].imag))
        fd.close()

    def save_ZTrans(self, filedir, filename, f, ZTrans, out_label):
        print('Saving %s data in %s' % (out_label, filename))
        try:
            fd = open(filedir + filename, 'w')
        except IOError:
            os.makedirs(savedir)
            fd = open(filedir + filename, 'w')
        fd.write('{0:^20s} {1:^20s} {2:^20s}\n'.format('f', 'ZTrans.real',
                                                       'ZTrans.imaginary'))
        fd.write('{0:^20s} {1:^20s} {2:^20s}\n'.format('[Hz]', '[Ohm/m]',
                                                       '[Ohm/m]'))
        for i in range(len(f)):
            fd.write('{0:20e} {1:20e} {2:20e}\n'.format(f[i], ZTrans[i].real,
                                                        ZTrans[i].imag))
        fd.close()

    def save_ZAllTrans(self, filedir, filename, f, ZDipX, ZDipY, ZQuadX,
                       ZQuadY, out_label):
        print('Saving %s data in %s' % (out_label, filename))
        try:
            fd = open(filedir + filename, 'w')
        except IOError:
            os.makedirs(savedir)
            fd = open(filedir + filename, 'w')
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

    def save_Zgeneric(self, filedir, filename, f, list_Z, list_label,
                      list_unit, out_label):
        print('Saving %s data in %s' % (out_label, filename))
        try:
            fd = open(filedir + filename, 'w')
        except IOError:
            os.makedirs(savedir)
            fd = open(filedir + filename, 'w')
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
