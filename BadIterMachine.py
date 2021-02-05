#This code imports the necessary modules.

import random
import shutil
import os

#srchstr = 'C:\\Users\\mysti\\Media_Files\\Sounds\\Bin'

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
        
        if  filepath.endswith(".wav") and ("Drum" in str(filepath))  or ("Beat" in str(filepath)) or ("drum" in str(filepath)) or ("beat" in str(filepath)): 
            if int(os.stat(filepath).st_size) < sizlim:
                contentbeats.append(filepath)

        if  filepath.endswith(".wav") and ("Pad" in str(filepath)) or ("pad" in str(filepath)):
            if int(os.stat(filepath).st_size) < sizlim:  
                contentdrones.append(filepath)

        if  filepath.endswith(".wav") and ("Bass" in str(filepath)) or ("bass" in str(filepath)):
            if int(os.stat(filepath).st_size) < sizlim:  
                contentbass.append(filepath)

        if  filepath.endswith(".wav") and ("One Shot" in str(filepath)) or ("one shot" in str(filepath)):
            if int(os.stat(filepath).st_size) < sizlim:  
             contentorg.append(filepath)

        if  filepath.endswith(".wav") and ("FX" in str(filepath)) or ("fx" in str(filepath)) :
            if int(os.stat(filepath).st_size) < sizlim:  
                contentsax.append(filepath)

        if  filepath.endswith(".wav") and ("Drone" in str(filepath)) or ("drone" in str(filepath)) :
            if int(os.stat(filepath).st_size) < sizlim:  
                contentgit.append(filepath)

        if  filepath.endswith(".wav") and (("Twinkle" in str(filepath)) or ("twinkle" in str(filepath)) and ("Amplitude" not in str(filepath))) :
            if int(os.stat(filepath).st_size) < sizlim:  
                contentpepper.append(filepath)

print("")

print("Gathering Root Sounds.")

x = len(contentbeats)

print("")
print("Beats")

for ctr in range(80):
    y = random.randrange(x)
    atrack = contentbeats[y]
    trackname = atrack[-20:-4]
    tracknam = ""
    for m in trackname:
        if m.isalnum():
            tracknam += m
    outstr = 'C:\\Users\\mysti\\Coding\\BadIterMachine\\BadIter\\Beats\\Beat_' + str(ctr) + tracknam + ".wav"
    shutil.copy(contentbeats[y], outstr)

x = len(contentdrones)

print("")
print("Drone")

for ctr in range(60):
    y = random.randrange(x)
    atrack = contentdrones[y]
    trackname = atrack[-20:-4]
    tracknam = ""
    for m in trackname:
        if m.isalnum():
            tracknam += m
    outstr = 'C:\\Users\\mysti\\Coding\\BadIterMachine\\BadIter\\Drone\\Drone_' + str(ctr) + tracknam + ".wav"
    shutil.copy(contentdrones[y], outstr)

x = len(contentpepper)

print("")
print("Pepper")

for ctr in range(60):
    y = random.randrange(x)
    atrack = contentpepper[y]
    trackname = atrack[-20:-4]
    tracknam = ""
    for m in trackname:
        if m.isalnum():
            tracknam += m
    outstr = 'C:\\Users\\mysti\\Coding\\BadIterMachine\\BadIter\\Pepper\\Pepper_' + str(ctr) + tracknam + ".wav"
    shutil.copy(contentpepper[y], outstr)

x = len(contentbass)

print("")
print("Bass")

for ctr in range(50):
    y = random.randrange(x)
    atrack = contentbass[y]
    trackname = atrack[-20:-4]
    tracknam = ""
    for m in trackname:
        if m.isalnum():
            tracknam += m
    outstr = 'C:\\Users\\mysti\\Coding\\BadIterMachine\\BadIter\\Bass\\Bass_' + str(ctr) + tracknam + ".wav"
    shutil.copy(contentbass[y], outstr)

x = len(contentorg)

print("")
print("Organ")

for ctr in range(50):
    y = random.randrange(x)
    atrack = contentorg[y]
    trackname = atrack[-20:-4]
    tracknam = ""
    for m in trackname:
        if m.isalnum():
            tracknam += m
    outstr = 'C:\\Users\\mysti\\Coding\\BadIterMachine\\BadIter\\Organ\\Organ' + str(ctr) + tracknam + ".wav"
    shutil.copy(contentorg[y], outstr)

x = len(contentsax)

print("")
print("Saxophone")

for ctr in range(50):
    y = random.randrange(x)
    atrack = contentsax[y]
    trackname = atrack[-20:-4]
    tracknam = ""
    for m in trackname:
        if m.isalnum():
            tracknam += m
    outstr = 'C:\\Users\\mysti\\Coding\\BadIterMachine\\BadIter\\Saxophone\\Saxophone_' + str(ctr) + tracknam + ".wav"
    shutil.copy(contentsax[y], outstr)

x = len(contentgit)

print("")
print("Guitar")

for ctr in range(50):
    y = random.randrange(x)
    atrack = contentgit[y]
    trackname = atrack[-20:-4]
    tracknam = ""
    for m in trackname:
        if m.isalnum():
            tracknam += m
    outstr = 'C:\\Users\\mysti\\Coding\\BadIterMachine\\BadIter\\Guitar\\Guitar_' + str(ctr) + tracknam + ".wav"
    shutil.copy(contentgit[y], outstr)

print("")

print("Check the folder containing these files for the 'BadIter' selections. You can copy these to your home folder for use with the GenerIter.")

print("")

## THE GHOST OF THE SHADOW ##
