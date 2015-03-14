from idautils import *
from idc import *
import sys

"""
 Helper function to colorize all 'call' and 'xor' mnemonics, so long
 as the XOR mnemonic operands are different from eachother
   * Colors 'call' instructions green (0x208020)
   * Colors 'xor' instructions blue (0xc02020)

   SetColor(ea, what, color)
       ea - address of the item
       what - type of the item (one of CIC_* constants) (CIC_ITEM=1, CIC_FUNC=2, CIC_SEGM=3)
       color - new color code in RGB (hex 0xBBGGRR)
"""

ea = ScreenEA()

while ea < end:
    if GetMnem(ea) == "call":

        SetColor(ea, CIC_ITEM, 0x208020) # Green
    elif GetMnem(ea) == "xor" and GetOpnd(ea, 0) != GetOpnd(ea, 1):
        SetColor(ea, CIC_ITEM, 0xc02020)
    ea += 1
