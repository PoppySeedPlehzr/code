from idautils import *
from idc import *
import sys

"""
// Get string type
//      ea - linear address
// Returns one of ASCSTR_... constants

long GetStringType(long ea);


#define ASCSTR_C        0       // C-style ASCII string
#define ASCSTR_PASCAL   1       // Pascal-style ASCII string (length byte)
#define ASCSTR_LEN2     2       // Pascal-style, length is 2 bytes
#define ASCSTR_UNICODE  3       // Unicode string
#define ASCSTR_LEN4     4       // Pascal-style, length is 4 bytes
#define ASCSTR_ULEN2    5       // Pascal-style Unicode, length is 2 bytes
#define ASCSTR_ULEN4    6       // Pascal-style Unicode, length is 4 bytes
#define ASCSTR_LAST     6       // Last string type
"""



def change_stack_vars(ea, end, s, encstructbase):
    regs   = set(["eax","ebx","ecx","edx","esp","edi","esi"])
    base   = encstructbase # This is the base of the encrypted strings.
    stack  = GetFrame(s) # Base of the subroutine.
    decstrval = ''

    while ea < end:
        mnem = GetMnem(ea)
        if mnem == "lea":
            opnd = GetOpnd(ea, 1)
            if len(opnd.split("+")) and "ebp" in opnd.split("+")[0] and decstrval != '':
                stkvarname = opnd.split("+")[1][:-1]
                #print "[+] Attempting to get Stack Variable {0} from stack base 0x{1:08x}:0x{2:08x}".format(stkvarname, stack, GetMemberOffset(stack, stkvarname))
                #print "[+] Changing stack variable {0} to {1}".format(stkvarname, decstrval)
                SetMemberName(stack, GetMemberOffset(stack, stkvarname), decstrval)
                decstrval = ''
        elif mnem == "mov":
            offs = 0x0 # Offset into the encrypted structure table we need to look
            opnd = GetOpnd(ea, 1)
            if opnd not in regs:
                if opnd[-1] == 'h': offs = int(opnd[:-1], 16)
                else: offs = int(opnd, 16)
            else:
                ea += 1
                continue
            strloc = Dword(base+offs*0xc)
            decstrval = GetString(strloc, -1, GetStringType(strloc))
            #print "[+] Got decrypted string at 0x{0:08x}: {1}".format(strloc, decstrval)
        ea += 1

#print "[+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+]"
change_stack_vars(0x100519C0, 0x10052013, 0x10051910, 0x1009DE40)











"""
from idautils import *
from idc import *
import sys

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

"""
