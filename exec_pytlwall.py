'''
@authors: Tatiana Rijoff,
          Carlo Zannini
@date:    01/03/2013
@copyright CERN

exec_pytlwall allows to run pytlwall code or reading all the options from a
configurator file or interactively taking the information from the user
'''

import sys
import pandas as pd
import pytlwall

if len(sys.argv) == 2:
    filename = sys.argv[1]
    myimped = {}
    read_cfg = pytlwall.CfgIo(filename)
    mywall = read_cfg.read_pytlwall()
    read_cfg.read_output()
    for imped in read_cfg.list_output:
        myimped[imped] = getattr(mywall, imped)
    for output_file in read_cfg.file_output.keys():
        prefix = read_cfg.file_output[output_file]['prefix']
        _, ext = output_file.split('.')
        data = {}
        data['f  [Hz] '] = mywall.f
        for imped in read_cfg.file_output[output_file]['imped']:
            if imped.find('ong') != -1:
                data[prefix + ' ' + imped + ' real [Ohm]'] = \
                    myimped[imped].real
                data[prefix + ' ' + imped + ' imag [Ohm]'] = \
                    myimped[imped].imag
            else:
                data[prefix + ' ' + imped + ' real [Ohm/m]'] = \
                    myimped[imped].real
                data[prefix + ' ' + imped + ' imag [Ohm/m]'] = \
                    myimped[imped].imag

        df = pd.DataFrame.from_dict(data)
        if ext == 'xlsx':
            df.to_excel(output_file, index=False)
        else:
            df.to_csv(output_file, index=None, sep='\t', mode='w')
