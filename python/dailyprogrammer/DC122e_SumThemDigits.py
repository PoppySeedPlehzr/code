# As a crude form of hashing function, Lars wants to sum the digits of a number. 
# Then he wants to sum the digits of the result, and repeat until he have only 
# one digit left. He learnt that this is called the digital root of a number, 
# but the Wikipedia article is just confusing him.
#
# Can you help him implement this problem in your favourite programming language?
# It is possible to treat the number as a string and work with each character at 
# a time. This is pretty slow on big numbers, though, so Lars wants you to at 
# least try solving it with only integer calculations 
# (the modulo operator may prove to be useful!).

# Input Description
# A positive integer, possibly 0.

# Output Description
# An integer between 0 and 9, the digital root of the input number.

from sys import argv

def SumThemDigits(num):
    if(num in range(10)):
        # print("Digital root is %d" % num)
        return num
    new_num = 0
    exp     = len(str(num))
    while(exp > 0):
        # new_num += int(num/(10**(exp-1)))
	new_num += num % 10
        # num     %= 10**(exp-1)
	num     /= 10
        exp     -= 1
    return SumThemDigits(new_num)

if __name__ == '__main__':
    if(len(argv) == 2):
        print(SumThemDigits(int(argv[1])))
    else:
        print("Usage: %s number" % argv[0])
