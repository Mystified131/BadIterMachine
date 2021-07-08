#This code imports the necessary modules.

import random
import shutil
import os
from RandFunct import random_number
from RandFunct2 import random_number2

for subdir, dirs, files in os.walk("C:\\Users\\mysti\\BadIter"):
    for file in files:
        filepath = subdir + os.sep + file

        if (filepath.endswith(".wav")) or (filepath.endswith(".sfk")) :
            os. remove(filepath) 

#srchstr = 'C:\\Users\\mysti\\Media_Files\\Sounds\\Bin'

print("")

cbeats = input("Please enter a keyword/genre word for the beats: ")

print("")

cdrones = input("Please enter a keyword/genre word for the drones: ")

print("")

cpepper = input("Please enter a keyword/genre word for the pepper: ")

print("")

cbass = input("Please enter a keyword/genre word for the bass: ")

print("")

corg = input("Please enter a keyword/genre word for the organ: ")

print("")

csax = input("Please enter a keyword/genre word for the sax: ")

print("")

cgit = input("Please enter a keyword/genre word for the git: ")

print("")

srchstr = 'C:\\Users\\mysti\\Media_Files\\Sounds\\Acid_Loops'

contentbeats = []
contentdrones = []
contentpepper = []
contentbass = []
contentorg = []
contentsax = []
contentgit = []

for subdir, dirs, files in os.walk(srchstr):
    for file in files:
        filepath = subdir + os.sep + file

        sizlim = 5000000
        
        if  filepath.endswith(".wav") and ("Drum" in str(filepath))  or ("Beat" in str(filepath)) or ("drum" in str(filepath)) or ("beat" in str(filepath)) and (cbeats in str(filepath)): 
            if int(os.stat(filepath).st_size) < sizlim:
                contentbeats.append(filepath)

        if  filepath.endswith(".wav") and (cdrones in str(filepath)):
            if int(os.stat(filepath).st_size) < sizlim:  
                contentdrones.append(filepath)

        if  filepath.endswith(".wav") and (cbass in str(filepath)) :
            if int(os.stat(filepath).st_size) < sizlim:  
                contentbass.append(filepath)

        if  filepath.endswith(".wav") and (corg in str(filepath)) :
            if int(os.stat(filepath).st_size) < sizlim:  
             contentorg.append(filepath)

        if  filepath.endswith(".wav") and (csax in str(filepath)):
            if int(os.stat(filepath).st_size) < sizlim:  
                contentsax.append(filepath)

        if  filepath.endswith(".wav") and (cgit in str(filepath)) :
            if int(os.stat(filepath).st_size) < sizlim:  
                contentgit.append(filepath)

        if  filepath.endswith(".wav") and (cpepper in str(filepath)) :
            if int(os.stat(filepath).st_size) < sizlim:  
                contentpepper.append(filepath)

print("")

print("Gathering Root Sounds.")

x = len(contentbeats)

print("")
print("Beats")

for ctr in range(80):
    y = random_number(x)
    atrack = contentbeats[y]
    trackname = atrack[-20:-4]
    tracknam = ""
    for m in trackname:
        if m.isalnum():
            tracknam += m
    outstr = "C:\\Users\\mysti\\BadIter\\Beats\\Beat_" + str(ctr) + tracknam + ".wav"
    shutil.copy(contentbeats[y], outstr)

x = len(contentdrones)

print("")
print("Drone")

for ctr in range(60):
    y = random_number(x)
    atrack = contentdrones[y]
    trackname = atrack[-20:-4]
    tracknam = ""
    for m in trackname:
        if m.isalnum():
            tracknam += m
    outstr = "C:\\Users\\mysti\\BadIter\\Drone\\Drone_" + str(ctr) + tracknam + ".wav"
    shutil.copy(contentdrones[y], outstr)

x = len(contentpepper)

print("")
print("Pepper")

for ctr in range(60):
    y = random_number(x)
    atrack = contentpepper[y]
    trackname = atrack[-20:-4]
    tracknam = ""
    for m in trackname:
        if m.isalnum():
            tracknam += m
    outstr = "C:\\Users\\mysti\\BadIter\\Pepper\\Pepper_" + str(ctr) + tracknam + ".wav"
    shutil.copy(contentpepper[y], outstr)

x = len(contentbass)

print("")
print("Bass")

for ctr in range(50):
    y = random_number(x)
    atrack = contentbass[y]
    trackname = atrack[-20:-4]
    tracknam = ""
    for m in trackname:
        if m.isalnum():
            tracknam += m
    outstr = "C:\\Users\\mysti\\BadIter\\Bass\\Bass_" + str(ctr) + tracknam + ".wav"
    shutil.copy(contentbass[y], outstr)

x = len(contentorg)

print("")
print("Organ")

for ctr in range(50):
    y = random_number(x)
    atrack = contentorg[y]
    trackname = atrack[-20:-4]
    tracknam = ""
    for m in trackname:
        if m.isalnum():
            tracknam += m
    outstr = "C:\\Users\\mysti\\BadIter\\Organ\\Organ" + str(ctr) + tracknam + ".wav"
    shutil.copy(contentorg[y], outstr)

x = len(contentsax)

print("")
print("Saxophone")

for ctr in range(50):
    y = random_number(x)
    atrack = contentsax[y]
    trackname = atrack[-20:-4]
    tracknam = ""
    for m in trackname:
        if m.isalnum():
            tracknam += m
    outstr = "C:\\Users\\mysti\\BadIter\\Saxophone\\Saxophone_" + str(ctr) + tracknam + ".wav"
    shutil.copy(contentsax[y], outstr)

x = len(contentgit)

print("")
print("Guitar")

for ctr in range(50):
    y = random_number(x)
    atrack = contentgit[y]
    trackname = atrack[-20:-4]
    tracknam = ""
    for m in trackname:
        if m.isalnum():
            tracknam += m
    outstr = "C:\\Users\\mysti\\BadIter\\Guitar\\Guitar_" + str(ctr) + tracknam + ".wav"
    shutil.copy(contentgit[y], outstr)

print("")

print("The new files should be written to your home directory, and the inventory json added to the same directory.")

print("")

os.system("generinv -I C:\\Users\\mysti\\BadIter -o baditer")

instr = "C:\\Users\\mysti\\Coding\\BadIterMachine\\baditer.json"

ostr = "C:\\Users\\mysti"

shutil.copy(instr, ostr)

# generiter -L baditer.json -C composel.json

## THE GHOST OF THE SHADOW ##
