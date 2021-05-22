import yaml
import os

if __name__ == '__main__':
    __location__ = os.path.realpath( 
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    stream = open(os.path.join(__location__,'asanas.yml'), 'r')
    asanas_dictionary = yaml.safe_load(stream)
    for asana,poses in asanas_dictionary.items():
        for pose in poses:
            for key,name in pose.items():
                print()
                print(asana)
                print('Key: ' + key)
                print('Rotation: ' + name['rotation'])
                print('English: ' + name['english'])
                print('Sanskrit: ' + name['sanskrit'])
                print('Orientation: ' + name['orientation'])
