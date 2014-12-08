# Reddit Daily Challenge 130 [easy] Roll the Dies
import random, sys

    def roll_the_dies(roll):
        n, m = [int(x) for x in roll.split('d')]
        for i in range(n):
            print(random.randrange(m)+1, end=" ")
        print()

    if __name__ == '__main__':
        random.seed()
        if(len(sys.argv) != 2):
            print("Usage: %s <NdM>" % sys.argv[0])
            sys.exit()
        else:
            roll_the_dies(sys.argv[1])
