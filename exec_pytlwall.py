'''
@authors: Tatiana Rijoff,
          Carlo Zannini
@date:    01/03/2013
@copyright CERN

exec_pytlwall allows to run pytlwall code or reading all the options from a
configurator file or interactively taking the information from the user
'''

import sys
import pytlwall
import pytlwall.shell_interface as shell


if len(sys.argv) == 1:
    shell.welcome_message()
    shell.help_pytlwall()
else:
    param = sys.argv[1]
    if param == '-a':
        filename = sys.argv[2]
        read_cfg = pytlwall.CfgIo(filename)
        read_cfg.read_output()
        read_cfg.calc_wall()
        read_cfg.print_wall()
        read_cfg.plot_wall()
    elif param == '-i':
        choice = ''
        shell.welcome_message()
        myconfig = pytlwall.CfgIo()
        while choice.upper() != 'X' and choice.lower() != 'exit':
            if ('chamber' in locals() and 'beam' in locals()
               and 'freq' in locals() and 'wall' not in locals()):
                if len(chamber.layers) > 0:
                    defined_wall = True
                    wall = pytlwall.TlWall(chamber, beam, freq)
            shell.menu0_pytlwall()
            if 'wall' in locals():
                shell.menu1_pytlwall()
            if ('chamber' in locals() and 'beam' in locals()
               and 'freq' in locals()):
                shell.menu2_pytlwall()
            shell.menuX_pytlwall()

            choice = input('your choice: ')
            if choice.lower() == 'chamber':
                chamber = shell.chamber_interface()
                myconfig.save_chamber(chamber)
                if len(chamber.layers) > 0:
                    myconfig.save_layer(chamber.layers)
                else:
                    print('Layer REQUIRED')
            elif choice.lower() == 'beam':
                beam = shell.beam_interface()
                myconfig.save_beam(beam)
            elif choice.lower() == 'freq':
                freq = shell.freq_interface()
                myconfig.save_freq(freq)
            elif choice.lower() == 'config':
                choice = input('Digit the configurator filename     ')
                res = myconfig.read_pytlwall(choice)
                if res is not None:
                    wall = res
                    chamber = wall.chamber
                    beam = wall.beam
                    freq = wall.freq
            elif choice.lower() == 'calc':
                list_calc = shell.calc_interface()
                myconfig.save_calc(list_calc)
                myconfig.calc_wall()
            elif choice.lower() == 'sav':
                file_output = shell.sav_interface(list_calc)
                myconfig.file_output = file_output
                myconfig.print_wall()
            elif choice.lower() == 'plot':
                img_output = shell.plot_interface(list_calc)
                myconfig.img_output = img_output
                myconfig.plot_wall()
            elif choice.lower() == 'sav_conf':
                choice = input('Digit the configurator filename     ')
                myconfig.config.write(open(choice, 'w'))
            elif choice.upper() == 'X' or choice.lower() == 'exit':
                print("Goodbye")
            else:
                print("Wrong choice, try again")

    elif param == '-g':
        print("graphic interface under construction")

    else:
        shell.help_pytlwall()
