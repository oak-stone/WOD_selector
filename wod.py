# A simple Python3 script to select a random wod from WODs wod_list
# The WOD list currently has only workouts, which do not require any equipment
# The WODs are taken from C r o s s F i t B o d y w e i g h t W o r k o u t R e s o u r c e Compiled and edited by Shane Skowron. Version 2.0, 09/02/09

import random
import linecache

file = 'wod_list.txt'

# Generate 1 random int
for x in range(1):
    #open the file
    with open(file, 'r') as wods:
        num_lines = sum(1 for line in wods)
    random_nr = (random.randint(0 ,(num_lines - 1)))
    wod = linecache.getline(file, random_nr)

print("Todays WOD is: \n\033[1;33;40m" + wod + "\033[0;37;40m")
