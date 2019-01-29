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

from time import gmtime, strftime
import sys, os, time, platform

OS = platform.uname().system.lower()

data = {
    "0": "Debug",
    "1": "Log",
    "2": "Warning",
    "3": "Error",
    "4": "RESERVED",
    "5": "In-Game Message", #dont log
    "6": "In-Game Alert", #dont log
    "7": "RESERVED",
    "8": "User Response", #dont log
    "9": "Other", #dont log
    "10": "RESERVED"
}

def getTime():
    return strftime("%H:%M:%S", gmtime())

def logMsg(msg, game, lvl = 5):
    msg = str(msg)
    if(lvl < 4):
        sav(msg, lvl)
    if(lvl == 0):
        return
    elif(lvl == 1):
        #log/output
        sys.stdout.write(msg+'\n')
        return
    elif(lvl == 2):
        #warning
        sys.stdout.write('\x1b[1m\033[33m[WARNING] : '+msg+'\033[39m\x1b[21m\n')
        return
    elif(lvl == 3):
        #error
        sys.stdout.write('\x1b[1m\033[91m[ERROR] : '+msg+'\033[39m\x1b[21m\n')
        return
    elif(lvl == 9): 
        #Other
        sys.stdout.write(msg+'\n')

    return

def sav(msg, lvl):
    if not os.path.exists('data'):
        os.makedirs('data')
        os.makedirs('data/logs')
    elif not os.path.exists('data/logs'):
        os.makedirs('data/logs')
    f = open('data/logs/log.txt', 'a')
    f.write('['+getTime()+'] ['+data[str(lvl)]+'] '+msg.replace('\n',' ')+'\n')
    f.close()

class logger:
    def __init__(self, game):
        self.game = game
    
    def log(self,msg,lvl):
        logMsg(msg,self.game,lvl)