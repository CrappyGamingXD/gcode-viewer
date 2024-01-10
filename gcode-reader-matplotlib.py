from parse import *
import matplotlib.pyplot as plt
import numpy as np
from extrude import extrude
from travel import travel

extrudes = []
travels = []

lastx = 0
lasty = 0
lastz = 0
laste = 0
lastfeed = 0
lasttemp = 0
lastfan = 0

def read_gcode(filename):
    gcode = open(filename, "r")

    for line in gcode:
        if parse("G1 {}", line) != None:
            G1(line)
        elif parse("G0 {}", line ) != None:
            G0(line)
        elif parse(";{}", line) != None:
            pass
        
        else: 
            print(line)


def G1(line):

    global lastfeed
    global lastx
    global lasty
    global lastz
    global laste
    
    if parse("G1 F{}", line) != None:
        if parse("G1 F{} X{} Y{} Z{} E{}", line) != None:

            parsed = parse("G1 F{} X{} Y{} Z{} E{}", line)

            global lastfeed
            global lastx
            global lasty
            global lastz
            global laste

            thisfeed = float(parsed[0])
            lastfeed = thisfeed

            thisx = float(parsed[1])
            thisy = float(parsed[2])
            thisz = float(parsed[3])
            thise = float(parsed[4])
            
            extrudes.append(extrude([lastx,thisx], [lasty, thisy], [lastz, thisz], thise - laste, thisfeed, lasttemp, lastfan))

            lastx = thisx
            lasty = thisy
            lastz = thisz
            laste = thise

        elif parse("G1 F{} X{} Y{} E{}", line) != None:
            
            parsed = parse("G1 F{} X{} Y{} E{}", line)

            thisfeed = float(parsed[0])
            lastfeed = thisfeed

            thisx = float(parsed[1])
            thisy = float(parsed[2])
            thise = float(parsed[3])
            
            extrudes.append(extrude([lastx,thisx], [lasty, thisy], [lastz, lastz], thise - laste, thisfeed, lasttemp, lastfan))

            lastx = thisx
            lasty = thisy
            laste = thise

        else: 
            print(line)

    elif parse('G1 {}', line) != None:
        if parse("G1 X{} Y{} Z{} F{} E{}", line) != None:

            parsed = parse("G1 X{} Y{} Z{} F{} E{} {}", line)

            thisfeed = float(parsed[3])
            lastfeed = thisfeed

            thisx = float(parsed[0])
            thisy = float(parsed[1])
            thisz = float(parsed[2])
            thise = float(parsed[4])
            
            extrudes.append(extrude([lastx,thisx], [lasty, thisy], [lastz, thisz], thise - laste, lastfeed, lasttemp, lastfan))

            lastx = thisx
            lasty = thisy
            lastz = thisz
            laste = thise

        elif parse("G1 X{} Y{} Z{} E{}", line) != None:

            parsed = parse("G1 X{} Y{} Z{} E{}", line)

            thisx = float(parsed[0])
            thisy = float(parsed[1])
            thisz = float(parsed[2])
            thise = float(parsed[3])
            
            extrudes.append(extrude([lastx,thisx], [lasty, thisy], [lastz, thisz], thise - laste, lastfeed, lasttemp, lastfan))

            lastx = thisx
            lasty = thisy
            lastz = thisz
            laste = thise

        elif parse("G1 X{} Y{} E{}", line) != None:
            
            parsed = parse("G1 X{} Y{} E{}", line)

            thisx = float(parsed[0])
            thisy = float(parsed[1])
            thise = float(parsed[2])
            
            extrudes.append(extrude([lastx,thisx], [lasty, thisy], [lastz, lastz], thise - laste, lastfeed, lasttemp, lastfan))

            lastx = thisx
            lasty = thisy
            laste = thise

        elif parse("G1 X{} Y{} Z{} F{} ;{}", line) != None:

            parsed = parse("G1 X{} Y{} Z{} F{} ;{}", line)

            thisx = float(parsed[0])
            thisy = float(parsed[1])
            thisz = float(parsed[2])
            thisfeed = float(parsed[3])
            
            extrudes.append(extrude([lastx,thisx], [lasty, thisy], [lastz, thisz], 0, thisfeed, lasttemp, lastfan))

            lastx = thisx
            lasty = thisy
            lastz = thisz
            lastfeed = thisfeed

        elif parse("G1 Z{} F{} {}", line) != None:

            parsed = parse("G1 Z{} F{} {}", line)

            thisz = parsed[0]
            thisfeed = parsed[1]

            extrudes.append(extrude([lastx, lastx], [lasty, lasty], [lastz, thisz], 0, thisfeed, lasttemp, lastfan))

            lastz = thisz
            lastfeed = thisfeed

        elif parse("G1 Z{} {}", line) != None:

            parsed = parse("G1 Z{} {}", line)

            thisz = parsed[0]

            extrudes.append(extrude([lastx, lastx], [lasty, lasty], [lastz, thisz], 0, lastfeed, lasttemp, lastfan))

            lastz = thisz


        else: 
            print(line)
    else: 
        print(line)
        

def G0(line):

    global lastfeed
    global lastx
    global lasty
    global lastz
    global laste
    
    if parse("G0 F{}", line) != None:
        if parse("G0 F{} X{} Y{} Z{}", line) != None:

            parsed = parse("G0 F{} X{} Y{} Z{}", line)

            global lastfeed
            global lastx
            global lasty
            global lastz
            global laste

            thisfeed = float(parsed[0])
            lastfeed = thisfeed

            thisx = float(parsed[1])
            thisy = float(parsed[2])
            thisz = float(parsed[3])
            
            travels.append(travel([lastx,thisx], [lasty, thisy], [lastz, thisz], thisfeed))

            lastx = thisx
            lasty = thisy
            lastz = thisz

        elif parse("G0 F{} X{} Y{}", line) != None:
            
            parsed = parse("G0 F{} X{} Y{}", line)

            thisfeed = float(parsed[0])
            lastfeed = thisfeed

            thisx = float(parsed[1])
            thisy = float(parsed[2])
            
            travels.append(travel([lastx,thisx], [lasty, thisy], lastz, thisfeed))

            lastx = thisx
            lasty = thisy

        else: 
            print(line)

    elif parse('G0 {}', line) != None:
        if parse("G0 X{} Y{} Z{} F{}", line) != None:

            parsed = parse("G0 X{} Y{} Z{} F{}", line)

            thisfeed = float(parsed[3])
            lastfeed = thisfeed

            thisx = float(parsed[0])
            thisy = float(parsed[1])
            thisz = float(parsed[2])
            
            travels.append(travel([lastx,thisx], [lasty, thisy], [lastz, thisz], lastfeed))

            lastx = thisx
            lasty = thisy
            lastz = thisz

        elif parse("G0 X{} Y{} Z{}", line) != None:

            parsed = parse("G0 X{} Y{} Z{}", line)

            thisx = float(parsed[0])
            thisy = float(parsed[1])
            thisz = float(parsed[2])
            
            travels.append(travel([lastx,thisx], [lasty, thisy], [lastz, thisz], lastfeed))

            lastx = thisx
            lasty = thisy
            lastz = thisz

        elif parse("G0 X{} Y{}", line) != None:
            
            parsed = parse("G0 X{} Y{}", line)

            thisx = float(parsed[0])
            thisy = float(parsed[1])
            
            travels.append(travel([lastx,thisx], [lasty, thisy], [lastz, lastz], lastfeed))

            lastx = thisx
            lasty = thisy

        else: 
            print(line)
    else: 
        print(line)



ax = plt.figure().add_subplot(projection='3d')

read_gcode("CE3PRO_bed_level_test.gcode")

for extrude in extrudes:
    ax.plot(extrude.x, extrude.y, extrude.z, '-b', label='extrudes')

plt.xlim(0,220)
plt.ylim(0,220)
ax.set_zlim(0,100)

plt.show()

#todo: matplotlib is too slow! maybe try other libraries?