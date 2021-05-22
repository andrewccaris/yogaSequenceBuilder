import yaml
import os

def print_dictionary( asanas ):
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

def get_asana_rotation( asanas, type, key ):
    return asanas[type][key][key]['rotation']

def get_asana_english_name( asanas, type, key ):
    return asanas[type][key][key]['english']

def get_asana_sanskrit_name( asanas, type, key ):
    return asanas[type][key][key]['sanskrit']

def get_asana_orientation( asanas, type, key ):
    return asanas[type][key][key]['orientation']

if __name__ == '__main__':
    __location__ = os.path.realpath( 
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    stream = open(os.path.join(__location__,'asanas.yml'), 'r')
    full_asanas = yaml.safe_load(stream)
    # linker = {key:value for key,value in full_asanas.items() if key in 'linkers'}
    # rising = {key:value for key,value in full_asanas.items() if key in 'rising-action'}
    # climax = {key:value for key,value in full_asanas.items() if key in 'climax'}
    # falling = {key:value for key,value in full_asanas.items() if key in 'falling-action'}
    
    print(get_asana_english_name(full_asanas,'linkers',1))
    print(get_asana_english_name(full_asanas,'rising-action',10))
    print(get_asana_english_name(full_asanas,'climax',2))
    print(get_asana_english_name(full_asanas,'falling-action',12))
    # print_dictionary(full_asanas['linkers'])
    # print_dictionary(full_asanas['rising-action'])
    # print_dictionary(full_asanas['climax'])
    # print_dictionary(full_asanas['falling-action'])
