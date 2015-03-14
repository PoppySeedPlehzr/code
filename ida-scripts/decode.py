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
        stroffs = Dword(ea)
        slength = Dword(ea+4)
        deckey  = Dword(ea+8)
        s = decrypt(stroffs, deckey, slength)
        MakeStr(ea, ea+slength)
        MakeStruct(ea, "string_struct")
        MakeComm(ea, s)
        print "[+] Decrypted String: {}".format(s)
        ea += 0xc

# Values relevant to a1d86bb21b2eda8a47c15888f9ef310b .\reader_sl.exe
# 0x0041A470 <-- Start of first block
# 0x0041A8B4 <-- End of first block
# 0x0041A8B8 <-- Start of second block
# 0x0041AADF <-- End of Second blcok
#decrypt_all(0x1000B1D0, 0x1000B2B3)
#decrypt_all(0x0041A8B8, 0x0041AADF)
#decrypt_all(0x1009d7d8, 0x1009d9dc)
#decrypt_all(0x1009d9e0, 0x1009dc14)
#decrypt_all(0x1009dc18, 0x1009eea7)
#decrypt_all(0x1009C130, 0x1009D6D7)
decrypt_all(0x100855B8, 0x100856A7)
