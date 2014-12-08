
import sys
import random

def gen_ports(num_ports):
    random.seed()
    f     = open('port_list', 'w')
    ap    = set(range(1,65536))
    ports = random.sample(ap, int(num_ports))
    for i in ports:
        f.write(str(i)+"\n")
        f.flush()
    f.close()

if __name__ == '__main__':
    if(len(sys.argv) != 2):
        print("Usage:python %s <Number of Ports>" % sys.argv[0])
    else:
        gen_ports(sys.argv[1])
