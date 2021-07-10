'''
@authors: Tatiana Rijoff,
          Carlo Zannini
@date:    01/03/2013
@copyright CERN

The plot_util module gives you some lazy functions to plot the tlwall results
'''
import numpy as np
import matplotlib.pyplot as plt
import os
import pytlwall


def plot_Z_vs_f_simple(f, Z,  imped_type='L', title=None,
                       savedir=None, savename=None,
                       xscale='lin', yscale='lin'):
    mask_real = np.logical_not(np.isnan(Z.real))
    fRe = f[mask_real]
    ZRe = Z[mask_real].real
    mask_imag = np.logical_not(np.isnan(Z.imag))
    fIm = f[mask_imag]
    ZIm = Z[mask_imag].imag
    if (len(fRe) == 0. and len(fIm) == 0.):
        return
    print(savename)
    if imped_type == 'L':
        Z_unit = r'$\Omega$'
    elif imped_type == 'S':
        Z_unit = r'$\Omega$ m'
    else:
        Z_unit = r'$\Omega$/m'
    fig = plt.figure()
    ax = plt.subplot(1, 1, 1)
    if title is not None:
        plt.title(title, fontsize=24)
    ax.plot(fRe, ZRe, linewidth=5, label='real')
    ax.plot(fIm, ZIm, linewidth=5, label='imaginary')
    ax.set_ylabel('Z [' + Z_unit + ']', fontsize=20)
    ax.set_xlabel('f [Hz]', fontsize=20)
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
    if xscale == 'log':
        plt.xscale('log')
    if xscale == 'symlog':
        plt.xscale('symlog')
    if yscale == 'symlog':
        plt.yscale('symlog')
    if yscale == 'log':
        plt.yscale('log')
    plt.xticks(fontsize=18)
    plt.yticks(fontsize=18)
    ax.grid(True)
    ax.legend(loc='best', fontsize=20)
    plt.tight_layout()
    if savename is not None:
        try:
            plt.savefig(savedir + savename)
        except IOError:
            os.makedirs(savedir)
            plt.savefig(savedir + savename)
    return fig


def plot_Z_vs_f_simple_single(f, Z, imped_type='L', title=None,
                              savedir=None, savename=None,
                              xscale='lin', yscale='lin'):
    mask = np.logical_not(np.isnan(Z))
    f = f[mask]
    Z = Z[mask]

    if (len(f) == 0.):
        return
    if imped_type == 'L':
        Z_unit = r'$\Omega$'
    elif imped_type == 'S':
        Z_unit = r'$\Omega$ m'
    else:
        Z_unit = r'$\Omega$/m'
    fig = plt.figure()
    ax = plt.subplot(1, 1, 1)
    if title is not None:
        plt.title(title, fontsize=24)
    ax.plot(f, Z, linewidth=5)
    ax.set_ylabel('Z [' + Z_unit + ']', fontsize=20)
    ax.set_xlabel('f [Hz]', fontsize=20)
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
    if xscale == 'log':
        plt.xscale('log')
    if xscale == 'symlog':
        plt.xscale('symlog')
    if yscale == 'symlog':
        plt.yscale('symlog')
    if yscale == 'log':
        plt.yscale('log')
    plt.xticks(fontsize=18)
    plt.yticks(fontsize=18)
    ax.grid(True)
    plt.tight_layout()
    if savename is not None:
        try:
            plt.savefig(savedir + savename)
        except IOError:
            os.makedirs(savedir)
            plt.savefig(savedir + savename)
    return fig


def plot_Z_vs_f_simple_single_compare(list_f, list_Z, list_label,
                                      imped_type='L', title=None,
                                      savedir=None, savename=None,
                                      xscale='lin', yscale='lin'):
    if imped_type == 'L':
        Z_unit = r'$\Omega$'
    elif imped_type == 'S':
        Z_unit = r'$\Omega$ m'
    else:
        Z_unit = r'$\Omega$/m'
    fig = plt.figure()
    ax = plt.subplot(1, 1, 1)
    if title is not None:
        plt.title(title, fontsize=24)
    for i in range(len(list_label)):
        width = len(list_f) * 3 - 2 * i
        ax.plot(list_f[i], list_Z[i], linewidth=width,
                label=list_label[i])
    ax.set_ylabel('Z [' + Z_unit + ']', fontsize=20)
    ax.set_xlabel('f [Hz]', fontsize=20)
    # ~ plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
    if xscale == 'log':
        plt.xscale('log')
    if xscale == 'symlog':
        plt.xscale('symlog')
    if yscale == 'symlog':
        plt.yscale('symlog')
    if yscale == 'log':
        plt.yscale('log')
    plt.xticks(fontsize=18)
    plt.yticks(fontsize=18)
    ax.grid(True)
    ax.legend(loc='best', fontsize=20)
    plt.tight_layout()
    if savename is not None:
        try:
            plt.savefig(savedir + savename)
        except IOError:
            os.makedirs(savedir)
            plt.savefig(savedir + savename)
    return fig


def plot_list_Z_vs_f(f, list_Z, list_label,
                     imped_type='L', title=None,
                     savedir='', savename=None,
                     xscale='lin', yscale='lin'):
    if imped_type == 'L':
        Z_unit = r'$\Omega$'
    elif imped_type == 'S':
        Z_unit = r'$\Omega$ m'
    else:
        Z_unit = r'$\Omega$/m'
    fig = plt.figure()
    ax = plt.subplot(1, 1, 1)
    if title is not None:
        plt.title(title, fontsize=24)
    for i in range(len(list_label)):
        width = len(list_Z) * 3 - 2 * i
        ax.plot(f, list_Z[i], linewidth=width,
                label=list_label[i])
    ax.set_ylabel('Z [' + Z_unit + ']', fontsize=20)
    ax.set_xlabel('f [Hz]', fontsize=20)
    # ~ plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
    if xscale == 'log':
        plt.xscale('log')
    if xscale == 'symlog':
        plt.xscale('symlog')
    if yscale == 'symlog':
        plt.yscale('symlog')
    if yscale == 'log':
        plt.yscale('log')
    plt.xticks(fontsize=18)
    plt.yticks(fontsize=18)
    ax.grid(True)
    ax.legend(loc='best', fontsize=20)
    plt.tight_layout()
    if savename is not None:
        try:
            plt.savefig(savedir + savename)
        except IOError:
            os.makedirs(savedir)
            plt.savefig(savedir + savename)
    return fig
