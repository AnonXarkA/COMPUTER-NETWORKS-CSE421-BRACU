import socket

format = "utf-8"
data = 16
port = 5050

disconnected_msg = "off"

hostname = socket.gethostname()

host_addr = socket.gethostbyname(hostname)

server_socket_addr = (host_addr, port)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(server_socket_addr)


server.listen()
print("Server is listening!")


 
while True:
    conn, addr = server.accept()
    print("Connected to:", addr)
    connected = True

    while connected:
        initial_msg = conn.recv(data).decode(format)
        print("Length", initial_msg)

        if initial_msg:
            msg_length = int(initial_msg)
            msg = conn.recv(msg_length).decode(format)
            if msg == disconnected_msg:
                conn.send("Bye . ".encode(format))

                print("Terminate conncetion with", addr)

                connected = False
            else:
                print(msg)
                conn.send("Msg recieve".encode(format))    

    conn.close()           