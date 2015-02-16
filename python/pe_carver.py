

import argparse, pefile




def carve_pe():
	pass







if __name__ == "__main__":
	carve_pe()







"""
import pefile
pe =  pefile.PE(‘/path/to/pefile.exe’, fast_load=True)
A later call to the full_load() method would parse the missing information.

It's also possible to just parse raw PE data:

pe = pefile.PE(data=str_object_with_pe_file_data)
Reading and writing standard header members
Once the PE file is successfully parsed, the data is readily available as attributes of the PE instance.

pe.OPTIONAL_HEADER.AddressOfEntryPoint
pe.OPTIONAL_HEADER.ImageBase
pe.FILE_HEADER.NumberOfSections
All of these values support assignment

pe.OPTIONAL_HEADER.AddressOfEntryPoint = 0xdeadbeef
and a subsequent call to

pe.write(filename='file_to_write.exe')



for section in pe.sections:
  print (section.Name, hex(section.VirtualAddress),
    hex(section.Misc_VirtualSize), section.SizeOfRawData )
"""



