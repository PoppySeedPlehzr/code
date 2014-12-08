import sys, os
from math import floor, ceil
out_file = open(os.path.join(os.getcwd(), "DancingWithGooglers_large.out"), 'w')
lines = open("DancingWithGooglers_large.in", 'r').readlines()
num_cases = int(lines[0])
for i in range(num_cases):
    out_file.write("Case #%s: " % str(i+1))
    line       = lines[i+1].split()
    num_scores = int(line[0])  # Number of numbers for this case.
    S          = int(line[1])  # Number of 'Surprises'
    surprises  = set()         # Set for keeping track of which scores had a surprise.
    p          = int(line[2])  # Threshold score
    scores     = line[3:]
    total      = 0
    for i in range(len(scores)):
        score  = int(scores[i])
        if(score >= p):
            judge1 = p
            while judge1 <= 10:
                score_remainder = score - judge1
                if(score_remainder <= 20):
                    if(score_remainder % 2): # remaining score was odd
                        judge2 = floor(score_remainder/2)
                        judge3 = ceil(score_remainder/2)
                    else: # remaining score was even
                        judge2 = score_remainder/2
                        judge3 = score_remainder/2
                    num1 = abs(judge1 - judge2)
                    num2 = abs(judge1 - judge3)
                    num3 = abs(judge2 - judge3)
                    if num1 < 2 and num2 < 2 and num3 < 2: # Found a solution
                        total += 1
                        if i in surprises:
                            surprises.remove(i)
                        break
                    elif num1 <= 2 and num2 <= 2 and num3 <= 2: # Found a surprise.
                        surprises.add(i)
                judge1 += 1 # End of While
    total += len(surprises) if len(surprises) <= S else S
    out_file.write('%s\n' % str(total))
out_file.close()