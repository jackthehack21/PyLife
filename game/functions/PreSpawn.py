#  /$$$$$$$            /$$       /$$  /$$$$$$         
# | $$__  $$          | $$      |__/ /$$__  $$        
# | $$  \ $$ /$$   /$$| $$       /$$| $$  \__//$$$$$$ 
# | $$$$$$$/| $$  | $$| $$      | $$| $$$$   /$$__  $$
# | $$____/ | $$  | $$| $$      | $$| $$_/  | $$$$$$$$
# | $$      | $$  | $$| $$      | $$| $$    | $$_____/
# | $$      |  $$$$$$$| $$$$$$$$| $$| $$    |  $$$$$$$
# |__/       \____  $$|________/|__/|__/     \_______/
#            /$$  | $$                                
#           |  $$$$$$/                                
#            \______/                                 
#
# @author Jackthehack21 <gangnam253@gmail.com | Jackthehaxk21#8860>
#
# A small life simulator game run someone elses lives and see what happens !...
# Copyright (C) 2019 Jackthehack21
#
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  
#
# See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with this program.  
# If not, see https://www.gnu.org/licenses/

import time, ssl

def run(game):
    plat = game.os.system.lower()
    game.logger.log("Game running on "+plat+", v"+game.os.release+", "+game.os.machine,0)
    if(plat == "windows"):
        handleWindows(game)
    elif(plat == "linux"):
        handleLinux(game)
    elif(plat == "darwin"):
        handleMacOSX(game)
    else:
        handleUnkown(game)

    game.logger.log("PreSpawn setup complete.",0)


def handleLinux(game):
    game.logger.log("Handling Linux PreSpawn setup.",0)
    return

def handleWindows(game):
    game.logger.log("Handling Windows PreSpawn setup.",0)
    enableColour(game)
    return

def handleMacOSX(game):
    game.logger.log("Handling MacOSX PreSpawn setup.",0)

    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        # Legacy Python that doesn't verify HTTPS certificates by default
        pass
    else:
        # Handle target environment that doesn't support HTTPS verification
        ssl._create_default_https_context = _create_unverified_https_context
    #This is to fix ssl warnings when using MacOSX to get/post data to our server.

    return

def handleUnkown(game):
    game.logger.log("Unable to identify your OS (Operating System), please contact me and let me know what your using !\np.s game will attempt to run now.",2)
    game.logger.log("Handling -unkown- system PreSpawn setup.",0)
    enableColour(game)
    return

def enableColour(game):
    game.logger.log("Force enabling colour.",0)
    from game.utils.colorama import initialise as color
    color.init()
    del color