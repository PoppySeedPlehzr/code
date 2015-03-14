from idautils import *
from idc import *
import sys, string




# This script iterates through an entire segment, and attempts to make all contiguous
# ASCII printable strings into String objects in IDA.
def make_strs(ea, ea_end):
    while ea < ea_end:
        b = Byte(ea)
        if b != 0x0:
            l = 0x0
            try:
                c = chr(b)
                if c in string.printable: start = ea
                while b != 0x0:
                    try:
                        c = chr(b)
                        if c in string.printable:
                            l += 0x1
                    except: pass
                    ea += 1
                    b = Byte(ea)
                #print "[+] Length of ASCII str: {}".format(l)
                #print "[+] Half Length of ASCII str: {}".format((ea-start)/2)
                if l >= (ea-start)-1:
                    MakeStr(start, ea) # Only make it a string if most of the data is ASCII printable
            except: pass
        ea += 1



# .rdata for cozy car
#make_strs(0x100853B0, 0x100AC000)

# .idata for cozy car
make_strs(0x10085000, 0x10085eB0)

# .data for cozy car
make_strs(0x100AC000, 0x100C8000)
