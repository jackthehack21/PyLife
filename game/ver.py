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

import sys

def http():
    return '001_dev' #_rel/_dev

def ver():
    return '0.0.1'

def build():
    return '0004'

def codeName():
    return 'ALPHA'

def release():
    return False

def bundled():
    if (getattr(sys, 'frozen', False) and (sys.argv[0] == sys.executable)):
        return True
    return False