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

def get_specific_asana( full_asanas, type, key ):
    return full_asanas[type][key][key]

def get_random_asana( full_asanas, type ):
    asanas = full_asanas[type]
    key = random.randrange(0, len(asanas), 1)
    return asanas[key][key]

#TODO: Add link move between standing and floor and floor and seated, etc
#TODO: Add rotation cannot go from internal to external, vice versa, either external to external or to neutral
#TODO: Find out how many moves are in a 60 min sequence, based on length of each move for 5 breaths and 1 breath for some
#TODO: Add warm up sequence
def build_sequence( full_asanas, vinyasa_flow, time ):
    list = []
    link = False
    moves = int( time / 1.5 )
    rising_moves = int( moves / 1.6 )
    asana_name = ""
    for x in range(0, moves):
        if x < rising_moves:
            if x % 3 == 0 and x != 0:
                if vinyasa_flow:
                    asana = get_specific_asana(full_asanas, 'linkers', 4)
                else:
                    asana = get_random_asana(full_asanas, 'linkers')
                link = True
            else:
                asana = get_random_asana(full_asanas, 'rising-action')
        elif x > rising_moves and x < rising_moves+3:
            asana = get_random_asana( full_asanas, 'climax')
        else:
            asana = get_random_asana(full_asanas, 'falling-action')

        asana_name = get_asana_english_name(asana) + ': ' + get_asana_sanskrit_name(asana)
        if link or asana_name not in list:
            list.append( asana_name )
            link = False
        else:
            x = x - 1
            
            
    return list

if __name__ == '__main__':
    __location__ = os.path.realpath( 
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    stream = open(os.path.join(__location__,'asanas.yml'), 'r')
    full_asanas = yaml.safe_load(stream)

    str_val = input("Options 30, 60, 90, 120, exit :- ")
    while str_val != 'exit':
        val = int(str_val)
        if val == 30 or val == 60 or val == 90 or val == 120:
            sequence = build_sequence(full_asanas, True, val)
            print( str_val + ' Minute sequence:')
            print( '\n'.join( sequence ) )
        else:
            print("Invalid time: 60,90,120 min classes are supported.")
        str_val = input("Options 60,90,exit :- ")

    """
    60 Minute sequence:
    Half Bound Lotus Standing Pose: Ardha Baddha Padmottanasana
    Mountain Pose: Tadasana
    Chaturanga to Upward-Facing Dog to Downward-Facing Dog: Vinyasa
    Sphinx Pose: Salamba Bhujangasana
    Headstand: Sirsasana
    Chaturanga to Upward-Facing Dog to Downward-Facing Dog: Vinyasa
    Scale Pose: Tolasana
    Cow Pose: Goasana
    Chaturanga to Upward-Facing Dog to Downward-Facing Dog: Vinyasa
    Wide Legged Standing Forward Bend Pose: Prasarita Paddotanasana
    Triangle Pose: Trikonasana
    Chaturanga to Upward-Facing Dog to Downward-Facing Dog: Vinyasa
    Standing Spinal Twist Pose: Katichakrasana
    Chaturanga to Upward-Facing Dog to Downward-Facing Dog: Vinyasa
    Standing Half Forward Bend Pose: Ardha Uttanasana
    Chaturanga to Upward-Facing Dog to Downward-Facing Dog: Vinyasa
    Warrior II Pose: Virabhadrasana II
    Dolphin Pose: Ardha Pincha Mayurasana
    Chaturanga to Upward-Facing Dog to Downward-Facing Dog: Vinyasa
    Warrior I Pose: Virabhadrasana I
    Chaturanga to Upward-Facing Dog to Downward-Facing Dog: Vinyasa
    Threading the Needle: Parsva Balasana
    Warrior II Pose: Virabhadrasana III
    Bridge Pose on Elbows: Dvapda Dhanurasana
    Upward Facing Forward Bend Pose: Urdhva Mukha Paschimottanasana
    Seated Forward Bend Pose: Paschimottanasana
    Plow Pose: Halasana
    Camel Pose: Ustrasana
    Revolved Head to Knee Pose: Parivritta Janu Sirsasana
    Child Pose: Balasana
    Fire Log Pose: Agni Stambhasana
    Royal Pigeon Pose: Raja Kapotasana
    Half Lotus Pose: Ardha Padmasana
    Crocodile Pose: Makarasana
    Upward Facing Two Foot Staff Pose: Dwi Pada Viparita Dandasana
    """
