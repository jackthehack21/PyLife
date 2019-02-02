from os.path import abspath, join, dirname
import random

def full_path(name):
    return "data/assets/names/"+name

files = {
    'male': full_path('namesMaleFirst.data'),
    'female': full_path('namesFemaleFirst.data'),
    'last': full_path('namesLast.data'),
}


def get_name(filename):
    selected = random.random() * 90
    with open(filename) as name_file:
        for line in name_file:
            name, _, cummulative, _ = line.split()
            if float(cummulative) > selected:
                return name
    return ""  # Return empty string if file is empty

#######################
## Public Functions: ##
#######################

def get_first_name(game, gender=None):
    if gender is None:
        game.logger.log("[Generator] : Gender must be provided for first name.",2)
        #raise ValueError("[Generator] : Gender must be provided for first name.")
    if gender not in ('male', 'female'):
        game.logger.log("[Generator] : Only 'male' and 'female' are supported as gender",2)
        #raise ValueError("[Generator] : Only 'male' and 'female' are supported as gender")
    return get_name(files['first:%s' % gender]).capitalize()


def get_last_name(game):
    return get_name(files['last']).capitalize()


def getFullName(game, gender=None):
    return "{0} {1}".format(get_first_name(game, gender), get_last_name(game))