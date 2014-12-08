#cd '.\Google Drive\Code\python\CDAL_weekly_ctf1'
#python server.py 10.100.2.72 42242

import socket
import os
import sys
import string
from time import localtime, strftime

# Generic function to write a time and a message
# to my log file.
def write_log(lfile, msg):
    message = strftime("%Y-%m-%d %H:%M:%S", localtime()) + " - " + msg + "\n"
    print("%s" % message)
    lfile.write("%s" % message)
    lfile.flush()
    
# Helper function to 'gracefully' close a socket. 
def close_connection(sock):
    try:
        sock.shutdown(socket.SHUT_RDWR)
        sock.close()
    except:
        pass

# Primary functionality of the server.  This
# function listens for and accepts socket connections
def listen(addr, port):
    
    log_file = open('server.log', 'a')
    write_log(log_file, "Server starting on " + addr + ":" + port)
    
    size   = 4096           # Max File Size
    serv   = None           # Server socket
    client = None           # Client socket
    uname  = "Muffins"      # Correct Username
    pword  = "Password1"    # Correct Password
    msg1   = b'Username: '  # Byte Strings
    msg2   = b'Password: '  # Byte Strings
    msg3   = b'Invalid Username.  Exiting.\n'
    msg4   = b'Invalid Password.  Exiting.\n'
    msg5   = b'Correct!  The flag is  between the brackets {1234567890_Muffins_Password1}'
    msg6   = bytes("Submit the flag at http://"+addr+"/index.php")
            
    try:
        serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serv.bind((addr, int(port)))
        serv.listen(10)
    except socket.error as se:
        if serv:
            serv.close()
        write_log(log_file, "ERROR: Socket Creation Failed - ErrorNumber " + \
            str(se.errno) + " - " + str(os.strerror(se.errno)))
        sys.exit()
        
    while True:
        print("Waiting for connections.  Ctrl+C to shutdown server.")
        try:
            # Log the incoming connection
            (client, address) = serv.accept()
            write_log(log_file, "Recieved connection from " + address[0] + ":" + str(address[1]))

            # Get the username from the client
            s = client.send(msg1)
            #data = str(client.recv(size))[2:-1].rstrip('\\r\\n')  # Needed for Windows
            data = str(client.recv(size))
            if data != uname:
                s = client.send(msg3)
                write_log(log_file, "Incorrect login attempt from " + address[0] + ":" + str(address[1]))
                write_log(log_file, "\t*** Attempted Username: " + data)
                write_log(log_file, "Closing connection from " + address[0] + ":" + str(address[1]))
                close_connection(client)
                continue
                
            # Get the password from the client    
            s = client.send(msg2)
            #data = str(client.recv(size))[2:-1].rstrip('\\r\\n')  # Needed for Windows
            data = str(client.recv(size))
            if data != pword:
                s = client.send(msg4)
                write_log(log_file, "Incorrect login attempt from " + address[0] + ":" + str(address[1]))
                write_log(log_file, "\t*** Attempted Password: " + data)
                write_log(log_file, "Closing connection from " + address[0] + ":" + str(address[1]))
                close_connection(client)
                continue
                
            # User name and password were correct, dump the data file.
            s = client.send(msg5)
            s = client.send(msg6)
            write_log(log_file, "Successful login from " +  address[0] + ":" + str(address[1]))
            write_log(log_file, "Closing connection from " + address[0] + ":" + str(address[1]))            
            close_connection(client)
        except:
            write_log(log_file, "Server shutting down")
            close_connection(serv)
            close_connection(client)
            sys.exit()

    log_file.close()


# Entry point, for sanity
if __name__ == '__main__':
    if(len(sys.argv) != 3):
        print("Usage: ./python %s <Listen IP> <Listen Port>" % sys.argv[0])
        sys.exit()
    else:
        listen(sys.argv[1], sys.argv[2])
        
        
        
        
        
        
        

