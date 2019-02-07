import socket
import selectors
import types
import printer.zebra as z
import subprocess
import os
import argparse


def accept_wrapper(sock):
    conn, addr = sock.accept()  # accept connection
    print('accepted connection from', addr)
    conn.setblocking(False)  # dont block
    data = types.SimpleNamespace(addr=addr, inb=b'', outb=b'')
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    sel.register(conn, events, data=data)


def service_connection(key, mask):
    sock = key.fileobj
    data = key.data
    if mask & selectors.EVENT_READ:
        recv_data = sock.recv(4096)  # Should be ready to read
        if recv_data:
            data.outb += recv_data
        else:
            #datos = b'^XA^CFA,45^FO50,25^FDEmiliano Larrea^FS^CFA,30^FO50,80^FDProLine - CEO^FS^FO50,120^FD2644804290^FS^FO50,160^FDemiliano18796@gmail.com^FS^FO50,110^BY2,2,95^BQ,2,4^FH_^FDHM,AEmiliano Larrea/ProLine - CEO/2644804290/emiliano18796@gmail.com^FS^XZ'
            # print_linux(datos)
            if mask & selectors.EVENT_WRITE:
                if data.outb:
                    print('echoing', repr(data.outb), 'to', data.addr)
                    # sent = sock.send(data.outb)  # Should be ready to write
                    clean_data = ((data.outb))
                    z.print_linux(clean_data)
                    f = open('./tmp/output.dat', 'wb')
                    f.write(clean_data)
                    f.close()
                    #data.outb = data.outb[sent:]
            print('closing connection to', data.addr)
            sel.unregister(sock)
            sock.close()


if __name__ == "__main__":
    from sys import platform

    if platform == "linux" or platform == "linux2":
        IS_LINUX = True
    else:
        IS_LINUX = False

    HOST = 'localhost'
  # Define HOST IP
    PORT = 8880        # Define port

    sel = selectors.DefaultSelector()  # selector object provides IO Multiplexing
    selectorcito = selectors.DefaultSelector()
    lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create socket
    lsock.bind((HOST, PORT))  # bind it to address
    lsock.listen()  # Enable server to accept connections
    print('listening on', (HOST, PORT))
    lsock.setblocking(False)  # set system calls to nonblocking
    # Register a socket object, monitoring it for I/O events
    sel.register(lsock, selectors.EVENT_READ, data=None)

    while True:  # run forever
        # wait until registered socket becomes ready, it blocks until it is ready for IO
        # returns key,event tuple one for each socket
        events = sel.select(timeout=None)
        '''
            key: SelectorKey namedtuple
                key.fileobj is the socket object
                key.data 
            mask is an event mask of the operations that are ready.
        '''
        for key, mask in events:
            if key.data is None:  # we know that the socket is ready
                accept_wrapper(key.fileobj)  # accept data
            else:
                service_connection(key, mask)
