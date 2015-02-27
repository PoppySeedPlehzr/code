# patch bytes
from idc import *

ea = 0x10025200
xor_key = 0x43
for x in range(0x53):
	v = Byte(ea+x)
	PatchByte(ea+x, (v^xor_key)&0xff)