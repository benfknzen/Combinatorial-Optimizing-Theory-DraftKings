from PlayerClass import Player
# Attempting to make a class with map more modular and accessable--- 3.1.2019 BZ

# class Fighter(Player):
class Fighter(Player):
    def __init__(self, key):
        self.key = 99
        self.attributes = [None] * 4
        self.attributes[0] = 'valuekey'
        self.attributes[1] = 'valuecolor'
        self.attributes[2] = 'valuesize'
        self.attributes[3] = 'valueshape'

        self.map_dk_attribute_index = {}

        #   indexing by a numerical key and also string
        self.map_dk_attribute_index.__setitem__(0, 'key')
        self.map_dk_attribute_index.__setitem__(1, 'color')
        self.map_dk_attribute_index.__setitem__('color', 1)
        self.map_dk_attribute_index.__setitem__(2, 'size')
        self.map_dk_attribute_index.__setitem__(3, 'shape')
        self.map_dk_attribute_index.update(dict((v, k) for k, v in list(self.map_dk_attribute_index.items())))



    def draft_kings_initialization(self, position, name_and_id_number, name, id_number, roster_position, salary,
                                   game_info, team_abbrev, avg_points_per_game):
        return

    # bi-dictionary setting occurs during mapping
    # def __setitem__(self, key, val):
    #     dict.__setitem__(self, key, val)
    #     dict.__setitem__(self, val, key)

    def get_index_by_name(self, name):
        return self.attributes[name]

    def draft_kings_get_attribute_key_by_index(self, index):
        return self.map_draft_kings_attribute_index[index]

    def get_attribute_by_name(self, name):
        return self.attributes[name]

    def get_attribute_by_index(self, index):
        return self.attributes[index]

    def set_attribute_by_name(self, name, value):
        self.attributes[self.map_dk_attribute_index[name]] = value

    def set_attribute_by_index(self, index, value):
        self.attribute_index[index] = value


if __name__ == "__main__":

    fighter_object = Fighter(77)
    for i in fighter_object.map_dk_attribute_index:
        print(i)
        print(fighter_object.map_dk_attribute_index[i])
    print(fighter_object.map_dk_attribute_index)
    print(fighter_object.map_dk_attribute_index[1])
    print(fighter_object.map_dk_attribute_index['color'])
    fighter_object.set_attribute_by_name('color', "red")
    print(str(fighter_object.get_attribute_by_index(int(fighter_object.map_dk_attribute_index['color']))))
    # print(str(fighter_object.get_attribute_by_name('1')))


    # fighter_object.set_attribute_by_name("color", "blue")
    # fighter_object.set_attribute_by_index(fighter_object, 2, 100)
    # fighter_object.set_attribute_by_name(fighter_object, "texture", "smooth")
    #
    # print(fighter_object.get_attribute_by_name("color"))
    # # print(fighter_object.get_attribute_by_index(1))
    #
    # for x in range(len(fighter_object.attributes)):
    #     print(fighter_object.attributes[x])
    #
    # for x in fighter_object.attribute_index:
    #     print(x)
    # # for x in fighter_object.get_attribute_by_index(x):
    # #     (x
    # print(fighter_object.get_attribute_by_index(1))
    #
    # print(fighter_object.draft_kings_get_attribute_key_by_index(1))
