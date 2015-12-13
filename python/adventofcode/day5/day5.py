#!/usr/bin/env python
from sets import Set

#lines = open("day5.in", 'r').readlines()
lines = open("day5.in.sample", 'r').readlines()

# Should contain at least three vowels
vowels = Set(['a','e','i','o','u'])
# Does not contain any of the following strings, EVEN if they satisfy other reqs
does_not = Set(['ab', 'cd', 'pq', 'xy'])


cnt = 0
for l in lines:
    if [x for x in does_not if x in l]:
        print "[-] Line {} was naughty because of not allowed strings".format(l)
        continue # Not nice, contains one of the strings
    if len(vowels.intersection(Set(l))) < 3:
        print "[-] Line {} was naughty because not greater than or equal to 3 vowels".format(l)
        continue # Not nice, does not contain more than three vowels.
    chars = list(l)
    if not [chars[i] for i in range(len(chars)-1) if chars[i+1] == chars[i]]:
        print "[-] Line {} was naughty because no repeated strings".format(l)
        continue
    cnt += 1

print "[+] {} nice strings".format(cnt)



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



"""
