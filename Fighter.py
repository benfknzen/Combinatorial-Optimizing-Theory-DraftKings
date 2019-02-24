# Google doc: https://docs.google.com/document/d/1T2konG3rGbnJsHpv_LCwMBu_KvBv2bqaaab_bBlw02g/edit
# Authors: Benjamin Zeng, Jordan Shih
# Class
#
# Class subset of Player

import Player


class Fighter(Player):

    def __init__(self, key, first_name, last_name, win, win_by_knockout, win_by_submission, win_by_decision, loss,
                 loss_by_knockout, loss_by_submission, loss_by_decision, no_contest):

        Player.__init__(self, key, first_name, last_name)

        self.win = win
        self.win_by_knockout = win_by_knockout
        self.win_by_submission = win_by_submission
        self.win_by_decision = win_by_decision
        self.loss = loss
        self.loss_by_knockout = loss_by_knockout
        self.loss_by_submission = loss_by_submission
        self.loss_by_decision = loss_by_decision
        self.no_contest = no_contest

    def get_all_fighter_data(self):
            return self.key + " " + self.first_name + " " + self.last_name + " " + self.win + " " + self.win_by_knockout + " " + self.win_by_submission
            + " " + self.win_by_decision + self.loss + " " + self.loss_by_knockout + " " \
            + loss_by_submission + " " + loss_by_decision + no_contest

    def get_win(self):
        return self.win

    def get_win_by_knockout(self):
        return self.win_by_knockout

    # def all-the-other-relevant-data(self):
# fill in relevant data that can be scrapped into fighter_data.csv (all data that we gather about our fighters should be not null)
