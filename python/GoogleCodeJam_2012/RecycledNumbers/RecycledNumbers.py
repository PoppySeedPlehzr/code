from math import factorial

def recycle_check():
    in_file  = open('RecycledNumbers_small.in', 'r')
    out_file = open('RecycledNumbers_small.out', 'w')

    lines     = in_file.readlines()
    num_cases = int(lines[0])
    
    for i in range(num_cases):
        out_file.write("Case #%d: " % int(i+1))
        line  = lines[i+1].split()
        low   = int(line[0])
        high  = int(line[1])
        total = 0
        
        for i in range(low, high+1):
            n   = 0
            num = str(i)
            old = set()
            for j in range(1, len(num)):
                num = num[1:] + num[0]
                if i < int(num) <= high and num not in old:
                    old.add(num)
                    n += 1
            total += n
            
        out_file.write('%d\n' % total)
        out_file.flush()
    out_file.close()

if __name__ == '__main__':
    recycle_check()