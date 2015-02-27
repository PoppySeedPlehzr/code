from idautils import *
from idc import *
import sys


#decode = 0x10009550
#decode = 0x10009f30
#decode = 0x10001550

# Reads bytes from an offset for a size
def read_bytes(ea, count):
    out = ''
    for i in range(count):
        out+=chr(Byte(i))
    return out
    
# Reads data from an offset until a 2 byte delimeter
def read_until(ea, word):
    out = ''
    while True:
        if Word(ea) == word:
            break
        out+=chr(Word(ea)&0xff)
        out+=chr((Word(ea)&0xff00) >> 0x8)
        ea+=2
    return out
            
def decode_str(ea, length, xor_key):
	s=''
	for x in range(length):
		v = Byte(ea+x)
		PatchByte(ea+x, (v ^ x) ^ xor_key) 
		s+=chr((v ^ x) ^ xor_key)
	print hex(ea), s
			
def get_string(offset, index):
	return GetString(Dword(offset+(index*0xc)))
			
# Finds the xor/hex offsets (push 0x1887)
def find_hex_offsets(ea):
    offsets = {}
    for xref in XrefsTo(ea):
        addr = xref.frm
        paddr = PrevHead(addr)
        index = 0
        count = 0
        while True:
            count+=1
            if count > 10:
                index = 0
                break
            if GetMnem(paddr) == 'mov':
				if GetOpType(paddr, 1) == 5:
					index = GetOpnd(paddr, 1)
					if index.endswith('h'):
						int(index[:-1], 16)
						break
            paddr = PrevHead(paddr)
        if index:
            #offsets[int(index[:-1], 16)] = paddr
			offsets[paddr] = int(index[:-1], 16)
            #print "("+hex(paddr)+",", hex(int(index[:-1], 16))+"),"
    return offsets

#get_string(0x100A4CB0, 0x105)
s_offset = 0x100A4038
decode_func_ea = 0x10071e30
offsets = find_hex_offsets(decode_func_ea)


for addr, o in offsets.iteritems():
	s = get_string(s_offset, o)
	#print hex(o), hex(addr), s
	MakeComm(addr, s)
    #x = find_offset_from_xor_data(o, xor_dwords_offset_loc)
    #string = config_data[x]
    #print "Making comment", hex(addr), string
    #MakeComm(addr, string)

    
print "----------------------------------"