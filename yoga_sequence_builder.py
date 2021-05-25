import yaml
import os
import random

class YogaSequenceBuilder:
    def __init__(self):
        __location__ = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__)))
        stream = open(os.path.join(__location__,'asanas.yml'), 'r')
        self.full_asanas = yaml.safe_load(stream)

    def print_asana_dictionary(self, asanas):
        for type,poses in asanas.items():
            for pose in poses:
                for key,name in pose.items():
                    print()
                    print(type)
                    print('Key: ' + str(key))
                    print('Rotation: ' + name['rotation'])
                    print('English: ' + name['english'])
                    print('Sanskrit: ' + name['sanskrit'])
                    print('Orientation: ' + name['orientation'])

    def print_asana_attributes(self, asana):
        print(self.get_asana_english_name(asana))
        print(self.get_asana_sanskrit_name(asana))
        print(self.get_asana_rotation(asana))
        print(self.get_asana_orientation(asana))

    def get_asana_rotation(self, asana):
        return asana['rotation']

    def get_asana_english_name(self, asana):
        return asana['english']

    def get_asana_sanskrit_name(self, asana):
        return asana['sanskrit']

    def get_asana_orientation(self, asana):
        return asana['orientation']

    def get_specific_asana(self, full_asanas, type, key):
        return full_asanas[type][key][key]

    def get_random_asana(self, full_asanas, type):
        asanas = full_asanas[type]
        key = random.randrange(0, len(asanas), 1)
        return asanas[key][key]

    #TODO: Add link move between standing and floor and floor and seated, etc
    #TODO: Add rotation cannot go from internal to external, vice versa, either external to external or to neutral
    #TODO: Find out how many moves are in a 60 min sequence, based on length of each move for 5 breaths and 1 breath for some
    #TODO: Add warm up sequence
    def build_sequence(self, full_asanas, vinyasa_flow, time):
        list = []
        link = False
        moves = int(time / 1.5)
        rising_moves = int(moves / 1.6)
        for x in range(0, moves):
            if x < rising_moves:
                if x % 3 == 0 and x != 0:
                    if vinyasa_flow:
                        asana = self.get_specific_asana(full_asanas, 'linkers', 4)
                    else:
                        asana = self.get_random_asana(full_asanas, 'linkers')
                    link = True
                else:
                    asana = self.get_random_asana(full_asanas, 'rising-action')
            elif x > rising_moves and x < rising_moves+3:
                asana = self.get_random_asana(full_asanas, 'climax')
            else:
                asana = self.get_random_asana(full_asanas, 'falling-action')

            asana_names = (self.get_asana_sanskrit_name(asana), self.get_asana_english_name(asana))
            if link or asana_names not in list:
                list.append(asana_names)
                link = False
            else:
                x = x - 1
                
                
        return list

    def get_sequence_as_string(self, sequence):
        return '\n'.join(sequence)

    def get_sequence(self, time):
        return self.build_sequence(self.full_asanas, True, int(time))
