import socket

HOST = 'tcp.ngrok.io'  # The server's hostname or IP address
PORT = 18830       # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    data = '^XA^CFA,60^FO150,35^FDASISTENTE^FS^CFA,40^FO50,110^FDNicolas Baudon^FS^CFA,30^FO50,170^FDProLine - CEO^FS^FO50,110^BY2,2,100^BQ,2,4^FH_^FDHM,ANicolas Baudon/Proline - CEO/Cel: 2612548472/nicobaudon01@gmail.com/DNI: 41155268^FS^XZ'
    bytestring = bytes(data, 'utf-8')
    s.sendall(bytestring)

print('Received', repr(bytestring))