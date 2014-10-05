#
#
# In tabletop role-playing games like Dungeons & Dragons, people use a system 
# called dice notation to represent a combination of dice to be rolled to 
# generate a random number. Dice rolls are of the form AdB (+/-) C, and 
# are calculated like this:
# Generate A random numbers from 1 to B and add them together.
# Add or subtract the modifier, C.
# If A is omitted, its value is 1; if (+/-)C is omitted, step 2 is skipped. 
# That is, "d8" is equivalent to "1d8+0".
# Write a function that takes a string like "10d6-2" or "d20+7" and generates 
# a random number uing this syntax.
# Here's a hint on how to parse the strings, if you get stuck:
# Split the string over 'd' first; if the left part is empty, A = 1,
# otherwise, read it as an integer and assign it to A. Then determine
# whether or not the second part contains a '+' or '-', etc
#
#



def diceRoller(roll):
    print roll.split('d');
    
    
    
    
    
    
if __name__ == '__main__":
    if(len(sys.argv) == 2):
        diceRoller(sys.argv[1])
    else:
        print "Incorrect number of arguments.  Please pass AdB+=C"

