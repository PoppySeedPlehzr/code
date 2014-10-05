import sys, re

if(len(sys.argv) > 1):
    print sys.argv[1] + ' | ' + ' '.join(re.findall('\d+',str(range(5))))
    print "---" + "--"*(int(sys.argv[2])+1)
    for i in range(int(sys.argv[2])+1):
        print str(i) + ' |',
        for j in range(int(sys.argv[2])+1):
            if(i == 0):
                print j,
            else:
                if(sys.argv[1] == "+"):
                    print i + j,
                elif(sys.argv[1] == "-"):
                    print i - j,
                elif(sys.argv[1] == "*"):
                    print i * j,
                elif(sys.argv[1] == "/"):
                    if(j == 0):
                        print "NA",
                    else:
                        print i / j,
        print '\n',
else:
    print "No command line arguments recieved"