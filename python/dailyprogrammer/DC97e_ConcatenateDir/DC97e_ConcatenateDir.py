# Write a program that concatenates all text files (*.txt) in a directory, 
# numbering file names in alphabetical order. Print a header containing some basic 
# information above each file.
#
# For example, if you have a directory like this:
#
# ~/example/abc.txt
# ~/example/def.txt
# ~/example/fgh.txt
#
# And call your program like this:
# nooodl:~$ ./challenge97easy example
# The output would look something like this:
# === abc.txt (200 bytes)
# (contents of abc.txt)
#
# === def.txt (300 bytes)
# (contents of def.txt)
#
# === ghi.txt (400 bytes)
# (contents of ghi.txt)
# For extra credit, add a command line option '-r' to your program that makes it 
# recurse into subdirectories alphabetically, too, printing larger headers for #each subdirectory.



import sys, os, re

def rec():
    files = os.walk('.')
    #print files(0)
#    newfile = open('ConcatedFile.txt','w')
#    for fname in files: 
#        if(fname.endswith('.txt')):
#            f = open(fname, 'r')
#            d = f.read()
#            newfile.write('=== ' + fname + ' ' + str(len(d)) + ' Bytes\n')
#            newfile.write(d)
#            newfile.write('\n\n')
#    newfile.close()

def non_rec():
    files = os.listdir('.')
    newfile = open('ConcatedFile.txt','w')
    for fname in files:
        if(fname.endswith('.txt')):
            f = open(fname, 'r')
            d = f.read()
            newfile.write('=== ' + fname + ' ' + str(len(d)) + ' Bytes\n')
            newfile.write(d)
            newfile.write('\n\n')
    newfile.close()

if __name__ == '__main__':
    if(len(sys.argv) > 1):
        if(sys.argv[1] == '-r'):
            rec()
        else:
            print "Invalid option.  use '-r' for recursive concatenation.  Otherwise"
            print "do not specify a flag."
    else:
        non_rec()





