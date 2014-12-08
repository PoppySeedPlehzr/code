#cd '.\Google Drive\Code\python\CDAL_weekly_ctf1'
#python client.py 10.100.1.103 42242

import socket
import sys
import os
import string
from time import localtime, strftime, sleep

# Generic function to write a time and a message
# to my log file.
def write_log(lfile, msg):
    message = strftime("%Y-%m-%d %H:%M:%S", localtime()) + " - " + msg + "\n"
    #print("%s" % message)  # Comment out for production run!
    lfile.write("%s" % message)
    lfile.flush()
    
# Primary functionality of the client.  This
# function talks to the server.
def talk(s, p):
    log_file = open('client.log', 'a')
    write_log(log_file, "Client starting")
    
    sleep_time = 5
    username   = b'Muffins'
    password   = b'Password1'
    flag       = b''
    size       = 4096
    client     = None
    
    while True:
        try:
            write_log(log_file, "Sleeping for " + str(sleep_time) + " seconds.")
            sleep(sleep_time)
            try:
                client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client.connect((s, int(p)))
            except socket.error as se:
                if client:
                    client.close()
                write_log(log_file, "ERROR: Socket Creation Failed - ErrorNumber #" + \
                    str(se.errno) + " - " + str(os.strerror(se.errno)))
                sys.exit()
            write_log(log_file, "Successfully connected to " + s + ":" + p)    
            
            # Get the initial server message.
            data = str(client.recv(size))[2:-1]
            if not data.startswith("Username"):
                write_log(log_file, "Server returned unexpected login negatiation sequence.")
                write_log(log_file, "\t*** Expected 'Username' but got '" + data + "'")
                write_log(log_file, "Closing connection to " + s + ":" + p)
                client.close()
                log_file.close()
                sys.exit()
            
            # Verify our username.
            r = client.send(username)
            data = str(client.recv(size))[2:-1]
            if not data.startswith("Password"):
                write_log(log_file, "Login failed.  Server Responded - '" + data + "'")
                write_log(log_file, "Closing connection to " + s + ":" + p)
                client.close()
                log_file.close()
                sys.exit()

            # Verify our password.
            r = client.send(password)    
            data = str(client.recv(size))[2:-1]
            if data.startswith("Correct"): # Success!
                write_log(log_file, "Successful login.  Server Responded - '" + data + "'")
                data = str(client.recv(size))[2:-1] # Site to submit the information
                write_log(log_file, "(cont)\t'" + data + "'")
            else: # FAIL!
                write_log(log_file, "Login failed.  Server Responded - '" + data + "'")

            # Cleanup and close.
            write_log(log_file, "Closing connection to " + s + ":" + p)
            client.close()
        except:
            write_log(log_file, "Shutting down client")
            break
        
    log_file.close()
    
if __name__ == '__main__':
    if(len(sys.argv) != 3):
        print("Usage: ./python %s <Server IP> <Server Port>" % sys.argv[0])
        sys.exit()
    else:
        talk(sys.argv[1], sys.argv[2])