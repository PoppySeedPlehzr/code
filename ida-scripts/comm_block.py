from idautils import *
from idc import *
import sys

"""
Code to add comments of strings decrypted
"""

ea   = 0x100519C0
end  = 0x10052013
base = 0x1009DE40
regs = set(["eax","ebx","ecx","edx","esp","edi","esi"])

while ea < end:
    op = GetMnem(ea)
    if op == "mov":
        print "[+] Found mov instruction"
        try:
            opnd = GetOpnd(ea, 1)
            if opnd not in regs:
                print "[+] Found non-register operand: {}".format(opnd)
                if opnd[-1] == 'h': offs = int(opnd[:-1], 16)
                else: offs = int(opnd, 16)
            else:
                print "[-] Operand was non-hex value."
                ea += 1
                continue
            print "[+] Got offset: {}".format(offs)
            comm = GetCommentEx(base+(offs*12), 0)
            print "[+] Got comment {} from base {}".format(comm, (base+offs*12))
            print "[+] Searching for correlating Call"
            while GetMnem(ea) != "call": ea += 1
            MakeComm(ea, comm)
        except Exception as e:
            print "[-] mov instruction did not have hex operand"
            print "[-] {}".format(e)
            ea += 1
            continue
    ea += 1
