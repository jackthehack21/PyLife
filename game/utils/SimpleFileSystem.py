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

import os

class sfs:

    def __init__(self, game):
        self.game = game

    def makeDir(self, d):
        return os.mkdir(d)

    def changeDir(self, d):
        return os.chdir(d)

    def removeDir(self, d):
        return os.rmdir(d)

    def getCWD(self):
        return os.getcwd()

    def createFile(self, f, data=None):
        if(self.fileExists(f)):
            self.game.logger.log("[SFS] : Attempted to create file "+f+" however it already exists.",3)
            #raise IOError("[SFS] : Attempted to create file "+f+" however it already exists.")
        
    def fileExists(self, f):
        if(os.path.exists(f) and os.path.isfile(f)):
            return True
        return False

    def dirExists(self, d):
        if(os.path.exists(d) and (not os.path.isfile(d))):
            return True
        return False