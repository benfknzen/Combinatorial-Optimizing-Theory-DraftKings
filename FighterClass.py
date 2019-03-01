# Google doc: https://docs.google.com/document/d/1T2konG3rGbnJsHpv_LCwMBu_KvBv2bqaaab_bBlw02g/edit
# Authors: Benjamin Zeng, Jordan Shih
# Class
#
# Class subset of Player

from PlayerClass import Player


class Fighter(Player):

    # defines default input parameters for new Fighter object
    def __init__(self, key):
        self.key = key
        self.first_name = ""
        self.last_name = ""
        self.win = ""
        self.win_by_knockout = ""
        self.win_by_submission = ""
        self.win_by_decision = ""
        self.loss = ""
        self.loss_by_knockout = ""
        self.loss_by_submission = ""
        self.loss_by_decision = ""
        self.no_contest = ""

        # Draft Kings normalized spreadsheet import/export
        self.draft_kings_mma_attributes = [None]*9

        self.name_and_id_number = ""
        self.position = ""
        self.name = ""
        self.id_number = ""
        self.roster_position = ""
        self.salary = ""
        self.game_info = ""
        self.team_abbrev = None
        self.avg_points_per_game = None

    # Draft Kings fully defined spreadsheet
    def draft_kings_initialization(self, position, name_and_id_number, name, id_number, roster_position, salary,
                                   game_info, team_abbrev, avg_points_per_game):
        self.draft_kings_mma_attributes[0], self.position = position
        self.name_and_id_number = name_and_id_number
        self.name = name
        self.id_number = id_number
        self.roster_position = roster_position
        self.salary = salary
        self.game_info = game_info
        self.team_abbrev = team_abbrev
        self.avg_points_per_game = avg_points_per_game

    def get_all_draft_kings_data(self):
        return str(self.name_and_id_number) + " " + \
               str(self.position) + " " + \
               str(self.name) + " " + \
               str(self.id_number) + " " + \
               str(self.roster_position) + " " + \
               str(self.salary) + " " + \
               str(self.game_info) + " " + \
               str(self.team_abbrev) + " " + \
               str(self.avg_points_per_game)

    # Fully defines the Fighter object
    def full_initialization(self, key, first_name, last_name):

        self.key = key
        self.first_name = first_name
        self.last_name = last_name
        self.super_player()
        # To  be added: rest of the parameters to initialize fully

    # Fully displays the Fighter object
    def get_all_fighter_data(self):
            return str(self.key) + " " + self.first_name + " " + self.last_name + " " + self.win + " " \
                   + self.win_by_knockout + " " + self.win_by_submission + " " + self.win_by_decision \
                   + self.loss + " " + self.loss_by_knockout + " " + self.loss_by_submission + " " \
                   + self.loss_by_decision + " " + self.no_contest

    # Defines and initializes all of the superclass of this object.
    # After initialized all functions of PlayerClass can be used.
    def super_player(self):
        Player.__init__(self, self.key, self.first_name, self.last_name)





    # def all-the-other-relevant-data(self):
# fill in relevant data that can be scrapped into fighter_data.csv (all data that we gather about our fighters should be not null)
