# patch bytes
from idc import *

ea = 0x100A6E38

for x in range(0xa):
	v = Byte(ea+x)
	PatchByte(ea+x, (v ^ x) ^ 0xd6) 