'''
@authors: Tatiana Rijoff,
          Carlo Zannini
@date:    01/03/2013
@copyright CERN
'''


class WallImpedanceList(object):
    def __init__(self, list_apertype, list_pipe_len_m, list_radius_m,
                 list_betax, list_betay, apertype_cfg_dict):
        self.list_apertype = list_apertype
        self.list_pipe_len_m = list_pipe_len_m
        self.list_radius_m = list_radius_m
        self.list_betax = list_betax
        self.list_betay = list_betay
        self.list_tlwall = []
        self.chamber_model = {}

        read_cfg = pytlwall.CfgIo()
        for apertype in self.apertype_cfg_dict.keys():
            cfg_file = apertype_cfg_dict[apertype]
            self.chamber_model[apertype] = read_cfg.read_chamber(cfg_file)
        beam = read_cfg.read_beam(cfg_file)
        freq = read_cfg.read_freq(cfg_file)

        for index in range(len(self.list_apertype)):
            chamber = self.chamber_model[self.list_apertype[index]]
            chamber.pipe_len_m = self.list_pipe_len_m[index]
            chamber.pipe_rad_m = self.list_pipe_radius_m[index]
            self.list_tlwall.append(chamber, beam, freq)
