import socket
import threading

#On linux SERVER might give 127.0.0.1, if thats the case, check /etc/hosts file and delete all non "localhost" entries with IP 127.0.0.1.
#If that's a problem, set SERVER to your servers IP.
SERVER = socket.gethostbyname(socket.gethostname())
#SERVER = 192.168.x.xxx
PORT = 5055
HEADER = 32
ENDMSG = "%DISC%"


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((SERVER, PORT))

def clientMgr(connection, address):
    connected = True

    while connected:
        msgLength = connection.recv(HEADER).decode('utf-8')
        if msgLength:
            msgLength = int(msgLength)
            msg = connection.recv(msgLength).decode('utf-8')

            if msg == ENDMSG:
                connected = False
                print(f"Connection to {address[0]}:{address[1]} terminated")
            else:
                print(f"-----\nFrom: {address[0]}:{address[1]}\nMsg: {msg}\n-----")
                #Do what you want with the received data here...
                with open("Logfile.txt", "a") as logappend:
                    logappend.write(msg + "\n")
                #Send a response to Client.
                connection.send("Received".encode('utf-8'))

    connection.close()

def main():
    server.listen()
    print(f"--Server-{SERVER} starting, listening on port {PORT}--")
    while True:
        connection, address = server.accept()
        thread = threading.Thread(target=clientMgr, args=(connection, address))
        thread.start()
        print(f"Total Clients: {threading.activeCount() -1}")

main()
