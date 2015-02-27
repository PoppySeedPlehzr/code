from idautils import *
from idc import *

def PatchInJump(jumpFrom, jumpTo):
	if jumpTo - jumpFrom > 255:
		PatchByte(jumpFrom, 0xE9)
		PatchDword(jumpFrom+1, jumpTo-(jumpFrom+5)) #e9XXXXXXXX 
	else:
		PatchByte(jumpFrom, 0xEB)
		PatchByte(jumpFrom+1, jumpTo-(jumpFrom+2)) #ebxx
		
def FindJunkCodeAddrs(frm, to):
	first = frm
	fc = 0
	lc = 0
	last = to
	while True:
		first = PrevHead(first)
		if GetMnem(first) == 'push':
			fc += 1
			continue
		else:
			first = NextHead(first)
			break
	while True:
		last = NextHead(last)
		if GetMnem(last) == 'pop':
			lc += 1
			continue
		else:
			break
	if fc == lc:
		return first, last

for head in Heads():
	if GetMnem(head) == 'pushf':
		next_head = NextHead(head)
		while True:
			if GetMnem(next_head) == 'popf':
				break
			elif GetMnem(next_head) == 'retn':
				next_head == 0
				break
			next_head = NextHead(next_head)
		if next_head:
			try:
				f, l = FindJunkCodeAddrs(head, next_head)
				PatchInJump(f, l)
				print "Patching: %s - %s" % (hex(f), hex(l))
			except:
				print "ERROR: %s - %s" % (hex(head), hex(next_head))