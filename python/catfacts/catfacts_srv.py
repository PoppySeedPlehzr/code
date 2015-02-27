import socket, sys, random

HOST  = "" # Listen on all available interfaces :3
PORT  = 1337
fout  = open("catfacts.log", "a")
facts = open("catfacts.txt", 'r').readlines()


def handler():
    global HOST, PORT, fout, facts
    greeting = "Welcome to Cat Facts!\n"
    s = socket.socket()

    s.bind((HOST,PORT))
    s.listen(1) # The arg is the backlog of queued connections :P

    while True:
        catfact    = greeting + facts[random.randrange(len(facts))]
        conn, addr = s.accept()
        fout.write("[+] Got connection from {}\n".format(addr))
        fout.write("[+] Sending catfact: {}\n".format(catfact))
        s.send





if __name__ == "__main__":
    #if len(sys.argv) !=
    random.seed()
    handler()
