import socket
import printer.zebra as z

HOST = 'localhost'  # Standard loopback interface address (localhost)
PORT = 8880        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    data = b''
    with conn:
        print('Connected by', addr)
        while True:
            temp = conn.recv(4096)
            data += temp
            if not temp:
                break
            clean_data = z.parse_string(z.clean_string(data))
            print(clean_data)
            z.print_linux(clean_data)