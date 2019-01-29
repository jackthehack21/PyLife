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

import time, sys, game.ver
from game import Handler as gameClass
from game.utils.colorama import initialise as color
from traceback import format_exception

travis = False

if(len(sys.argv) >= 2 and sys.argv[1] == "--travis-mode"):
    travis = True

color.init()
game = gameClass.handler(travis)

del travis

if(game.travis):
    game.logger.log("Travis mode enabled !",2)



#### Start Main: ####

time.sleep(2)

game.logger.log("Game loading...", 1)

#Spawn main

#####################

##### End Game: #####

#Kill main thread when all finished.

######################