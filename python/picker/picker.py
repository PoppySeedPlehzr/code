import sys, random, os

num_selections = 10000000

def picker(names): 
    names_lib = {} 
    names = sorted(names) 
    done = False
      
    for i in xrange(len(names)): 
        names_lib[i] = [0, names[i], 0] 
          
    while not done and len(names_lib.keys()) > 1:
        keep = True
        done = True
      
        # This is where the actual random selection happens.
        for i in xrange(num_selections): 
            names_lib[list(names_lib.keys())[random.randint(0, len(names_lib.keys())-1)]][0] += 1
          
        key, value = max(names_lib.items(), key= lambda x:x[1]) 
        print(str(value[1]) + " won with " + str(value[0]) + " votes from " + os.environ['COMPUTERNAME'])
          
        if(names_lib[key][2] == 0): 
            print("Would you like to keep this result? (y/n): ")
            if(input().rstrip('\n')[0].lower() == 'n'): 
                del names_lib[key] 
                keep = False
            else:
                print(names_lib[key][1] + " - already marked for keep")
                
        if keep:
            names_lib[key][2] += 1
        # Check to see if all names have gotten a 'yes' vote
        for i in names_lib.keys(): 
            if(names_lib[i][2] == 0): 
                done = False
            names_lib[i][0] = 0
              
    # Dump the results
    print("Name Selection Completed")
    if len(names_lib.keys()) == 1:
        print(names_lib[0][1] + "\t- Default selection.")
    else:
        print("Names marked for keep")
        for i in names_lib.keys(): 
            if len(names_lib[i][1]) > 7: 
                print(names_lib[i][1] + "\t- " + str(names_lib[i][2]))
            else: 
                print(names_lib[i][1] + "\t\t- " + str(names_lib[i][2]))
              
              
if __name__ == '__main__': 
    if(len(sys.argv) == 2): 
        random.seed() # Seed random using systime 
        f = open(sys.argv[1], 'r').readlines() 
        names = [] 
        for n in f: 
            names.append(n.rstrip('\n')) 
        picker(names) 
    else: 
        print("Usage: %s <File of Names>" % sys.argv[0])
        sys.exit()
