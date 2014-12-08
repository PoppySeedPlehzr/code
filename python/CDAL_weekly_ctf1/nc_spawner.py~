import sys
import time
import random
from subprocess import PIPE, Popen

# Function for getting the PIDs of all nc sessions.
#def get_nc_pids():
def kill_ncs():
    pids = []
    proc = Popen("netstat -lpnut", stdout=PIPE, shell=True)
    lines = proc.stdout.readlines()[2:]
    proc.kill()
    for l in lines:
        line = l.split()
        pid_info = line[-1].split('/')
        if(pid_info[1] == 'nc'):
            #pids.append(int(pid_info[0]))
            p = Popen("kill -9 " + str(pid_info[0]), stdout=PIPE, shell=True)
            p.wait()

# Function to kill all nc and shell script sessions
#def killer(procs):
def kill_daemons(procs):
    #print("Killer Called.  Dumping Pids")
    #print(pids)
    # Terminate all of the shell scripts spawning the NC sessions
    for p in procs:
        #print("Killing shell script %d" % p)
        try:
            p.kill()
            #Popen("kill -9 " + str(p), stdout=PIPE, shell=True)
        except SubprocessError as se:
            print("ERROR: %s" % se)

    # Terminate all of the NC sessions
    #nc_pids = get_nc_pids()
    #for p in nc_pids:
    #    #print("Killing nc session %d" % p)
    #    try:
    #        Popen("kill -9 " + str(p), stdout=PIPE, shell=True)
    #    except SubprocessError as se:
    #        print("ERROR: %s" % se)
    
    # Verify that all of the NC sessions are dead.
    #nc_pids = get_nc_pids()
    #if len(nc_pids) > 0:
    #    print("ERROR: Not all NC Sessions were destroyed.  Dumping PIDs")
    #    for p in nc_pids:
    #        print("NC Session with pid %d was not killed." % p)
    #else:
    #    print("All nc sessions ended.")

# Function to spawn a netcat session on each port given in args.
#def spawner(port_list):
def spawner(fname):
    random.seed()
    #pids      = {}  # Mapping of PIDs with the NC port number.
    procs     = []
    egg       = "/bin/sh"
    msgs      = ["Hi, Billy Mays here with the AwesomeAuger!",\
                "Hi, Billy Mays here for Mighty Putty!",\
                "Hi, Billy Mays here for Mighty Mendit!",\
                "Hi, Billy Mays here with Zorbeez!",\
                "Hi, Billy Mays here for Mighty Shine",\
                "Hi, Billy Mays here for Kaboom!",\
                "Hi, Billy Mays here with the Steam Buddy!",\
                "Hi, Billy Mays here with Simoniz Fix It!",\
                "Hi, Billy Mays here for the Handy Switch!",\
                "Hi, Billy Mays here for the Grater Plater",\
                "Hi, Billy Mays here for What Odor?",\
                "Hi, Billy Mays here for the GatorBlades!",\
                "Hi, Billy Mays here for the Hercules Hooks!",\
                "Hi, Billy Mays here for the dualsaw!",\
                "Hi, Billy Mays here for the Tool Band-it",\
                "Hi, Billy Mays here to share with you, the most important product I have ever endorsed!",\
                "Hi, Billy Mays here for the Vidalia Chopit!",\
                "Hi, Billy Mays here with the Vidalia Slice Wizard!",\
                "Hi, Billy Mays here for the original Quick Chop!",\
                "Hi, Billy Mays here with the Ding King!",\
                "Hi, Billy Mays here for Oxy Clean",\
                "Hi, Billy Mays here for the Jupiter Jack!",\
                "Hi, Billy Mays here for the Big City Slider Station!",\
                "Hi, Billy Mays here for the Home Smart Easy Butler",\
                "Hi, Billy Mays here for Engrave-It!",\
                "Hi, Billy Mays here for Green Now!",\
                "Hi, Billy Mays here for Flies-away!",\
                "Hi, Billy Mays here for Simoniz Liquid Diamonds!",\
                "Hi, Billy Mays here for the Gopher!"]

    lim = Popen("ulimit -Sn", stdout=PIPE, shell=True).stdout.read().strip()
    port_list = [x.strip() for x in open(fname, 'r').readlines() if len(x) > 1]
    
    if(len(port_list) < int(lim)):
        for p in port_list:
            if int(p) != 42242 and int(p) != 80:
                msg = msgs[random.randrange(len(msgs))]
                try:
                    proc = Popen("while true; do echo $(echo "+msg+" | nc -l -p "+p+" &) >> nc_spawner.log; done", stdout=PIPE, shell=True)
                except OSError as oe:  # This should hopefully never get hit due to initial check, but leaving in...
                    print("ERROR: %s" % oe)
                    print("Exiting - Killing all daemons and netcat sessions.")
                    for pr in procs:
                        pr.kill()
                    proc.kill()
                    kill_ncs()
                    print("Unable to open %d NC daemons.  Please increase alloted open file count." % len(port_list))
                    sys.exit()
                except SubprocessError as se:
                    print("ERROR: %s" % se)
                procs.append(proc)
                #pids[proc.pid] = p
                
        # Dump the sessions spawned. Used for debugging
        #for p in pids.keys():
        #    print("NC daemon spawned with pid %d listening on port %s" % (p, pids[p]))
        
        resp = raw_input("All sessions spawned.  Type 'exit' to quit.\n")    
        while resp != 'exit':
            print("Unknown Command: %s\nType 'exit' to quit." % resp)
            time.sleep(1)
            resp = raw_input()
        # Call the function to end all nc sessions.
        #killer(procs)
        print("Shutting down all daemons and netcat sessions")
        time.sleep(10)
        kill_daemons(procs)
        time.sleep(10)
        kill_ncs()
    else:
        print("Open File limits insufficient to open %d netcat sessions.")
        print("Increase the openfiles ulimits and run again.")
        sys.exit()
        
    

if __name__ == '__main__':
    if(len(sys.argv) != 2):
        #if(len(sys.argv) == 1):
        print("Usage: python %s <Newline Delimed Ports File>" % sys.argv[0])
        sys.exit()
    else:
        spawner(sys.argv[1])
        #spawner(sys.argv[1:])
        
        
