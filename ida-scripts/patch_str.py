from idautils import *
from idc import *
import sys

def read_until(ea, b):
	out = ''
	count = 0
	while True:
		if Byte(ea) == b:
			break
		if count > 0x500:
			return '' # probably an error
		out+=chr(Byte(ea)&0xff)
		ea+=1
		count+=1
	return out
	
def find_hex_offsets(ea, mnem):
	offsets = {}
	for xref in XrefsTo(ea):
		addr = xref.frm
		paddr = PrevHead(addr)
		offset = 0
		count = 0
		while True:
			count+=1
			if count > 10:
				offset = 0
				break
			if GetMnem(paddr) == mnem:
				if "+" not in GetOpnd(paddr, 0) and "*" not in GetOpnd(paddr, 0):
					offset = GetOperandValue(paddr, 1)
					if offset == -1:
						offset = GetOperandValue(paddr, 0)
					if offset > 0x10000000:
						break
			paddr = PrevHead(paddr)
		if offset:
			offsets[paddr] = offset
	return offsets
			
def xor(data, key):
    l = len(key)

    buff = ""
    for i in range(0, len(data)):
        if data[i] != key[i % l]:
            buff += chr(ord(data[i]) ^ ord(key[i % l]))
        else:
            buff += data[i]
    return buff
	
key = "Last-Error Code"
key2 = "\x5c\x69\xc1\x11\x48\x17\x28\x19\x43\x11\xd8"
key3 = "Microsoft"
decode_funcs = (0x100029c0, 0x100060d0)
decode_funcs2 = (0x1000bf50, 0x1000C020)
decode_funcs3 = (0x10007C70,)

for decode_func in decode_funcs:
	
	offsets = find_hex_offsets(decode_func, "mov")	

	for addr, o  in offsets.iteritems():
		data = read_until(o, 0x00)
		string = xor(data, key)
		print "Making comment", hex(addr), string
		MakeComm(addr, string)

for decode_func in decode_funcs2:
	
	offsets = find_hex_offsets(decode_func, "push")	

	for addr, o  in offsets.iteritems():
		data = read_until(o, 0x00)
		string = xor(data, key2)
		print "Making comment", hex(addr), hex(o), string
		MakeComm(addr, string)	
		
for decode_func in decode_funcs3:
	
	offsets = find_hex_offsets(decode_func, "mov")	

	for addr, o  in offsets.iteritems():
		data = read_until(o, 0x00)
		string = xor(data, key3)
		print "Making comment", hex(addr), string
		MakeComm(addr, string)
print "----------------------------------"
