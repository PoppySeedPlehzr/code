#!/usr/bin/env python

#lines = open("day6.sample.in", 'r').readlines()
lines = open("day6.in", 'r').readlines()
lights = [[0 for x in range(1000)] for i in range(1000)]

# Read in all of the lights data
for l in lines:
    # If the lights are on, turn them off, if off turn them on
    if 'toggle' in l:
        x1, y1 = int(l.split()[1].split(',')[0]), int(l.split()[1].split(',')[1])
        x2, y2 = int(l.split()[3].split(',')[0]), int(l.split()[3].split(',')[1])
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                lights[x][y] += 2

    # Turn on all lights in the range to the 'on' position
    elif 'on' in l:
        x1, y1 = int(l.split()[2].split(',')[0]), int(l.split()[2].split(',')[1])
        x2, y2 = int(l.split()[4].split(',')[0]), int(l.split()[4].split(',')[1])
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                lights[x][y] += 1

    # Turn off all lights in the specified range
    elif 'off' in l:
        x1, y1 = int(l.split()[2].split(',')[0]), int(l.split()[2].split(',')[1])
        x2, y2 = int(l.split()[4].split(',')[0]), int(l.split()[4].split(',')[1])
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                lights[x][y] -= 1
                if lights[x][y] < 0: lights[x][y] = 0
    else:
        pass



# Count all the turned on lights
cnt = 0
for x in range(1000):
    for y in range(1000):
        cnt += lights[x][y]
#print "[+] {} lights are turned on".format(cnt)
print "[+] Total Brightness - {} ".format(cnt)


# Bonus: Display the lights :)








"""
--- Day 6: Probably a Fire Hazard ---

Because your neighbors keep defeating you in the holiday house decorating contest year after year, you've decided to deploy one million lights in a 1000x1000 grid.

Furthermore, because you've been especially nice this year, Santa has mailed you instructions on how to display the ideal lighting configuration.

Lights in your grid are numbered from 0 to 999 in each direction; the lights at each corner are at 0,0, 0,999, 999,999, and 999,0. The instructions include whether to turn on, turn off, or toggle various inclusive ranges given as coordinate pairs. Each coordinate pair represents opposite corners of a rectangle, inclusive; a coordinate pair like 0,0 through 2,2 therefore refers to 9 lights in a 3x3 square. The lights all start turned off.

To defeat your neighbors this year, all you have to do is set up your lights by doing the instructions Santa sent you in order.

For example:

turn on 0,0 through 999,999 would turn on (or leave on) every light.
toggle 0,0 through 999,0 would toggle the first line of 1000 lights, turning off the ones that were on, and turning on the ones that were off.
turn off 499,499 through 500,500 would turn off (or leave off) the middle four lights.
After following the instructions, how many lights are lit?
"""
