# Google doc: https://docs.google.com/document/d/1T2konG3rGbnJsHpv_LCwMBu_KvBv2bqaaab_bBlw02g/edit
# Authors: Benjamin Zeng
# Class
#
# Combinatorially adds more dimensions to our picks. To be used in conjunction with more definitive classes.
# Contains generic identification and attributes that all subclasses should contain


class Player:

    def __init__(self, key, first_name, last_name):
        self.key = key
        self.first_name = first_name
        self.last_name = last_name

    def get_all_player_data(self):
        return self.first_name + " " + self.last_name
