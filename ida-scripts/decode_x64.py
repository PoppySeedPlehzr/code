from idautils import *
from idc import *
import sys

def decrypt(addr, key, l):
    ea = addr
    s  = ''
    for i in range(l):
        w = Byte(ea)
        c = (i ^ w ^ key)&0xff
        PatchByte(ea, c)
        ea += 1
        s += chr(c)
    return s


def decrypt_all(start, end):
    print "--------------------"
    ea = start
    while ea < end:
        stroffs = Qword(ea)
        slength = Qword(ea+0x8)
        deckey  = Qword(ea+0x10)
        s = decrypt(stroffs, deckey, slength)
        MakeStr(ea, ea+slength)
        MakeStruct(ea, "string_struct")
        MakeComm(ea, s)
        print "[+] Decrypted String: {}".format(s)
        ea += 0x18

# Values relevant to a1d86bb21b2eda8a47c15888f9ef310b .\reader_sl.exe
# 0x0041A470 <-- Start of first block
# 0x0041A8B4 <-- End of first block
# 0x0041A8B8 <-- Start of second block
# 0x0041AADF <-- End of Second blcok
decrypt_all(0x00000018000C6D0, 0x00000018000C897)
#decrypt_all(0x0041A8B8, 0x0041AADF)
