#!/usr/bin/env python
from sets import Set
from string import count

lines = [x.strip() for x in open("day5.in", 'r').readlines()]
#lines = [x.strip() for x in open("day5.in.sample", 'r').readlines()]



# Part 2
cnt = 0
for l in lines:
    if not [l[i] for i in range(len(l) - 2) if l[i] == l[i+2]]:
        continue
    # Fucking lol. The second stipulation.. is literally just python's string.count
    if not [ count(l, l[i:i+2]) for i in range(len(l)- 2) if count(l, l[i:i+2]) >= 2 ]:
        continue
    cnt += 1
print "[+] {} nice strings".format(cnt)


"""  Part 1
# Should contain at least three vowels
vowels = ['a','e','i','o','u']
# Does not contain any of the following strings, EVEN if they satisfy other reqs
does_not = ['ab', 'cd', 'pq', 'xy']

cnt = 0
for l in lines:
    if [x for x in does_not if x in l]:
        continue # Not nice, contains one of the strings
    if len([x for x in l if x in vowels]) < 3:
        continue # Not nice, does not contain more than three vowels.
    if not [l[i] for i in range(len(l)-1) if l[i+1] == l[i]]:
        continue
    cnt += 1

print "[+] {} nice strings".format(cnt)
"""


"""
--- Day 5: Doesn't He Have Intern-Elves For This? ---

Santa needs help figuring out which strings in his text file are naughty or nice.

A nice string is one with all of the following properties:

It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
For example:

ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double letter (...dd...), and none of the disallowed substrings.
aaa is nice because it has at least three vowels and a double letter, even though the letters used by different rules overlap.
jchzalrnumimnmhp is naughty because it has no double letter.
haegwjzuvuyypxyu is naughty because it contains the string xy.
dvszwmarrgswjxmb is naughty because it contains only one vowel.
How many strings are nice?

Your puzzle answer was 258.

The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---

Realizing the error of his ways, Santa has switched to a better model of determining whether a string is naughty or nice. None of the old rules apply, as they are all clearly ridiculous.

Now, a nice string is one with all of the following properties:

It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.
For example:

qjhvhtzxzqqjkmpb is nice because is has a pair that appears twice (qj) and a letter that repeats with exactly one letter between them (zxz).
xxyxx is nice because it has a pair that appears twice and a letter that repeats with one between, even though the letters used by each rule overlap.
uurcxstgmygtbstg is naughty because it has a pair (tg) but no repeat with a single letter between them.
ieodomkazucvgmuy is naughty because it has a repeating letter with one between (odo), but no pair that appears twice.
How many strings are nice under these new rules?

"""
