import yaml
import os
import random

def print_asana_dictionary( asanas ):
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

def print_asana_attributes( asana ):
    print(get_asana_english_name(asana))
    print(get_asana_sanskrit_name(asana))
    print(get_asana_rotation(asana))
    print(get_asana_orientation(asana))

def get_asana_rotation( asana ):
    return asana['rotation']

def get_asana_english_name( asana ):
    return asana['english']

def get_asana_sanskrit_name( asana ):
    return asana['sanskrit']

def get_asana_orientation( asana ):
    return asana['orientation']

def get_random_asana( full_asanas, type ):
    asanas = full_asanas[type]
    key = random.randrange(0, len(asanas), 1)
    return asanas[key][key]

#TODO: Add link move between standing and floor and floor and seated, etc
#TODO: Don't allow duplicates
#TODO: Find out how many moves are in a 60 min sequence, based on length of each move for 5 breaths and 1 breath for some
def build_60min_sequence( full_asanas ):
    link = 0
    for x in range(0,40):
        if x < 25:
            if link == 3:
                asana = get_random_asana(full_asanas, 'linkers')
                print(get_asana_english_name(asana))
                link = 0
            else:
                asana = get_random_asana(full_asanas, 'rising-action')
                print(get_asana_english_name(asana))
                link += 1
        elif x > 25 and x < 28:
            asana = get_random_asana( full_asanas, 'climax')
            print( get_asana_english_name(asana))
        else:
            asana = get_random_asana(full_asanas, 'falling-action')
            print(get_asana_english_name(asana))

if __name__ == '__main__':
    __location__ = os.path.realpath( 
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    stream = open(os.path.join(__location__,'asanas.yml'), 'r')
    full_asanas = yaml.safe_load(stream)
    # linker = {key:value for key,value in full_asanas.items() if key in 'linkers'}
    # rising = {key:value for key,value in full_asanas.items() if key in 'rising-action'}
    # climax = {key:value for key,value in full_asanas.items() if key in 'climax'}
    # falling = {key:value for key,value in full_asanas.items() if key in 'falling-action'}
    
    build_60min_sequence(full_asanas)

    # print_dictionary(full_asanas['linkers'])
    # print_dictionary(full_asanas['rising-action'])
    # print_dictionary(full_asanas['climax'])
    # print_dictionary(full_asanas['falling-action'])
