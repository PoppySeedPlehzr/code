
import sys, os
from math import floor, ceil

def dancin(fname):
    outf_name = os.path.join(os.getcwd(), "DancingWithGooglers.out")
    try:
        out_file = open(outf_name, 'w')
        try:
            lines = open(fname, 'r').readlines()
        except FileNotFoundError as e:
            print("Unable to find file %s" % fname)
            sys.exit()
         
        #         
        # Main Code Goes Here.
        #
        
        num_cases = int(lines[0])
        for i in range(num_cases):
            #print("Analyzing Case#%d: " % int(i+1))
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
                #print("\tGoogler #%d had an overall score of %d" % (i+1, score))
                if(score >= p):
                    judge1 = p
                    while judge1 <= 10:
                        #print("\t\tJudge #1: %d" % judge1)
                        score_remainder = score - judge1
                        if(score_remainder <= 20):
                            if(score_remainder % 2): # remaining score was odd
                                judge2 = floor(score_remainder/2)
                                judge3 = ceil(score_remainder/2)
                            else: # remaining score was even
                                judge2 = score_remainder/2
                                judge3 = score_remainder/2
                            #print("\t\tJudge #3: %d" % judge2)
                            #print("\t\tJudge #2: %d" % judge3)
                            num1 = abs(judge1 - judge2)
                            num2 = abs(judge1 - judge3)
                            num3 = abs(judge2 - judge3)
                            if num1 < 2 and num2 < 2 and num3 < 2: # Found a solution
                                #print("\t\t\tFound a solution!")
                                #print("\t\t\tJudge #1: %d" % judge1)
                                #print("\t\t\tJudge #2: %d" % judge2)
                                #print("\t\t\tJudge #3: %d" % judge3)
                                total += 1
                                if i in surprises:
                                    surprises.remove(i)
                                break
                            elif num1 <= 2 and num2 <= 2 and num3 <= 2: # Found a surprise.
                                #print("\t\t\tSurprise Found!")
                                #print("\t\t\tJudge #1: %d" % judge1)
                                #print("\t\t\tJudge #2: %d" % judge2)
                                #print("\t\t\tJudge #3: %d" % judge3)
                                #print("\t\t\tAdding to surprise set!")
                                surprises.add(i)
                        judge1 += 1
            # Check the total number of surprises... and add it on to the total.
            #print("\tSurprise Set: ",surprises)
            #additional_s = len(surprises) if len(surprises) <= S else S
            #print("\tAdding %d additional surprises" % additional_s)
            #total += additional_s
            total += len(surprises) if len(surprises) <= S else S
            # Write the results to the file.
            #print("Total was %d Googlers that scored higher than p" % total)
            out_file.write('%s\n' % str(total))
        #
        # Main Code Ends Here.
        #
        
        out_file.close()
    except PermissionError as pe:
        print("Unable to open %s for writing.  Insufficient Permissions" % outf_name)
        sys.exit()
                

if __name__ == '__main__':
    if(len(sys.argv) != 2):
        print("Usage: %s <Input File>" % sys.argv[0])
        sys.exit()
    else:
        dancin(sys.argv[1])
