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
	
def read_length(ea, length):
	out = ''
	for i in range(length):
		out+=chr(Byte(ea)&0xff)
		ea+=1
	return out

def xor(data, key):
	return ''.join([chr(ord(c) ^ key ^ i) for i, c in enumerate(data)])
	
ea = 0x1003B030
print hex(ea)
print hex(Dword(ea))
counter = 0
while (ea < 0x1003B688):
	offset = Dword(ea)
	length = Dword(ea+4)
	xor_key = Dword(ea+8)
	
	data = read_length(offset, length)
	#print [hex(ord(c)) for c in data]
	#print hex(xor_key)
	#sys.exit()
	MakeComm(ea, hex(counter) + "-> " + xor(data, xor_key))
	#print xor(data, xor_key)
	ea+=0xc
	counter+=1
#key = "Last-Error Code"
#decode_func = 0x402a93
#key = "Microsoft"
#decode_func = 0x4018d0

	
#offsets = find_hex_offsets(decode_func, "push")	

#for addr, o  in offsets.iteritems():
	#data = read_until(o, 0x00)
	#string = xor(data, key)
	#print "Making comment", hex(addr), string
	#MakeComm(addr, string)
#print "----------------------------------"
