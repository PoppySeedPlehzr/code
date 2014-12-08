import sys, re, string

def analytics(fname):
    lines   = []
    first   = {}
    check_f = True
    c_cnts  = {}  # Individual character counts
    w_cnts  = {}  # Individual word counts
    syms    = 0   # Total Symbol counts
    words   = 0   # Total word count
    letters = 0   # Total letter count
    ascii_l = set(string.ascii_lowercase)
    
    try:
        lines = open(fname, 'r').readlines()
    except FileNotFoundError as e:
        print("%s was not found.  Exiting." % fname)
        sys.exit
    for line in lines:
        ws = [re.sub(r'[\W_]+', '', x) for x in line.split()]
        if(len(ws) == 0):
            check_f = True
        syms += len(re.findall(r'[\W_]', ''.join(x for x in line.split())))
        for w in ws:
            w = w.lower()
            words += 1
            w_cnts[w] = 1 if w not in w_cnts.keys() else w_cnts[w] + 1
            if check_f:
                first[w] = 1 if w not in first.keys() else first[w] + 1
                check_f = False
            for c in w:
                letters += 1
                c_cnts[c] = 1 if c not in c_cnts.keys() else c_cnts[c] + 1
    
    w_list = sorted(w_cnts.items(), key=lambda x:x[1], reverse=True) # Reverse sort the dict of words
    c_list = sorted(c_cnts.items(), key=lambda x:x[1], reverse=True) # Reverse sort the dict of characters
    
    print("%d words" % words)
    print("%d letters" % letters)
    print("%d symbols" % syms)
    print("Top three most common words: \"%s\", \"%s\", \"%s\"" % (w_list[0][0],w_list[1][0],w_list[2][0]))
    print("Top three most common letters: '%s', '%s', '%s'" % (c_list[0][0],c_list[1][0],c_list[2][0]))
    print("%s is the most common first word of all paragraphs" % sorted(first.items(), key=lambda x:x[1], reverse=True)[0][0])
    print("Words were only used once:", [x[0] for x in w_list if x[1] == 1])
    print("Letters were not used in this document: ", {x for x in ascii_l if x not in c_cnts.keys()})

if __name__ == '__main__':
    if(len(sys.argv) != 2):
        print("Usage: %s <Text File Path>" % sys.argv[0])
        sys.exit()
    else:
        analytics(sys.argv[1])
    