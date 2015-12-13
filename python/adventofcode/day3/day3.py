#!/usr/bin/env python

# To solve this problem, let's just imagine santa flying through Euclidian space,
# and mark his coords accordingly. We'll keep track of where he's been in a set,
# and then answering the question of how many unique houses he's visited should be super simply.

from sets import Set


data = open("day3.in", 'r').read()
#data = open("day3.in.sample", 'r').read()
#houses_delivered = Set([(0,0)]) # Part 1
santa_delivered = Set([(0,0)]) # Part 2
robos_delivered = Set([(0,0)]) # Part 2
#coord = (0,0) # Part 1
coord = (0,0)
for i in range(0, len(data), 2):
    if data[i] == "^":
        coord = (coord[0] + 1, coord[1])
    elif data[i] == ">":
        coord = (coord[0], coord[1] + 1)
    elif data[i] == "v":
        coord = (coord[0] - 1, coord[1])
    elif data[i] == "<":
        coord = (coord[0], coord[1] - 1)
    else:
        print "[-] Encountered unknown character: {}".format(data[i])
    santa_delivered.add(coord)
print "[+] Santa visited {} houses".format(len(santa_delivered))

coord = (0,0)
for i in range(1, len(data), 2):
    if data[i] == "^":
        coord = (coord[0] + 1, coord[1])
    elif data[i] == ">":
        coord = (coord[0], coord[1] + 1)
    elif data[i] == "v":
        coord = (coord[0] - 1, coord[1])
    elif data[i] == "<":
        coord = (coord[0], coord[1] - 1)
    else:
        print "[-] Encountered unknown character: {}".format(data[i])
    robos_delivered.add(coord)
print "[+] Robo Santa visited {} houses".format(len(robos_delivered))
print "[+] Total number of houses delivered to: {}" \
    .format(len(santa_delivered.symmetric_difference(robos_delivered))+
    len(santa_delivered.intersection(robos_delivered)))

""" Part 1
for c in data:
    if c == "^":
        coord = (coord[0] + 1, coord[1])
    elif c == ">":
        coord = (coord[0], coord[1] + 1)
    elif c == "v":
        coord = (coord[0] - 1, coord[1])
    elif c == "<":
        coord = (coord[0], coord[1] - 1)
    else:
        print "[-] Encountered unknown character: {}".format(c)
    houses_delivered.add(coord)
print "[+] Santa visited {} houses".format(len(houses_delivered))
"""






"""
--- Day 3: Perfectly Spherical Houses in a Vacuum ---

Santa is delivering presents to an infinite two-dimensional grid of houses.

He begins by delivering a present to the house at his starting location, and then an elf at the North Pole calls him via radio and tells him where to move next. Moves are always exactly one house to the north (^), south (v), east (>), or west (<). After each move, he delivers another present to the house at his new location.

However, the elf back at the north pole has had a little too much eggnog, and so his directions are a little off, and Santa ends up visiting some houses more than once. How many houses receive at least one present?

For example:

> delivers presents to 2 houses: one at the starting location, and one to the east.
^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.
Your puzzle answer was 2572.

The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---

The next year, to speed up the process, Santa creates a robot version of himself, Robo-Santa, to deliver presents with him.

Santa and Robo-Santa start at the same location (delivering two presents to the same starting house), then take turns moving based on instructions from the elf, who is eggnoggedly reading from the same script as the previous year.

This year, how many houses receive at least one present?

For example:

^v delivers presents to 3 houses, because Santa goes north, and then Robo-Santa goes south.
^>v< now delivers presents to 3 houses, and Santa and Robo-Santa end up back where they started.
^v^v^v^v^v now delivers presents to 11 houses, with Santa going one direction and Robo-Santa going the other.
Although it hasn't changed, you can still get your puzzle input.

Answer:
 [Submit]

You can also [Share] this puzzle.

"""
