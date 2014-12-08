
import sys, os

def translator(fname):
    alph_map = {'y' : 'a',
                'n' : 'b',
                'f' : 'c',
                'i' : 'd',
                'c' : 'e',
                'w' : 'f',
                'l' : 'g',
                'b' : 'h',
                'k' : 'i',
                'u' : 'j',
                'o' : 'k',
                'm' : 'l',
                'x' : 'm',
                's' : 'n',
                'e' : 'o',
                'v' : 'p',
                'z' : 'q',
                'p' : 'r',
                'd' : 's',
                'r' : 't',
                'j' : 'u',
                'g' : 'v',
                't' : 'w',
                'h' : 'x',
                'a' : 'y',
                'q' : 'z',}
            
    lines     = []
    c_shift   = 2
    outf_name = os.path.join(os.getcwd(), "SpeakingInTongues.out")
    try:
        outf = open(outf_name, 'w')
        try:
            lines = open(fname, 'r').readlines()
        except FileNotFoundError as e:
            print("Unable to find file %s" % fname)
            sys.exit()
        for i in range(int(lines[0])):
            outf.write("Case #%s: " % str(i+1))
            for c in lines[i+1]:
                if c != '\n':
                    if c.isalpha():
                        c = alph_map[c]
                    outf.write("%s" % c)
            outf.write('\n')
        outf.close()
    except PermissionError as pe:
        print("Unable to open %s for writing.  Insufficient Permissions" % outf_name)
        sys.exit()
                

if __name__ == '__main__':
    if(len(sys.argv) != 2):
        print("Usage: %s <Input File>" % sys.argv[0])
        sys.exit()
    else:
        translator(sys.argv[1])
