import socket
import threading

#On linux SERVER might give 127.0.0.1, if thats the case, check /etc/hosts file and delete all non "localhost" entries with IP 127.0.0.1.
#If that's a problem, set SERVER to your servers IP.
SERVER = socket.gethostbyname(socket.gethostname())
#SERVER = 192.168.x.xxx
PORT = 5055
SIZE = 32

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((SERVER, PORT))

def clientMgr(connection, address):
    data = connection.decode('utf-8')

    print(f"-----\nFrom: {address[0]}:{address[1]}\nMsg: {data}\n-----")
    #Do what you want with the received data here...
    with open("Logfile.txt", "a") as logappend:
        logappend.write(data + "\n")


def main():
    #server.listen()
    print(f"--Server-{SERVER} starting, listening on port {PORT}--")
    while True:
        connection, address = server.recvfrom(SIZE)
        thread = threading.Thread(target=clientMgr, args=(connection, address))
        thread.start()
        print(f"Total Threads: {threading.activeCount()}")

main()
