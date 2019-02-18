#!/bin/bash

cd ./Downloads
./ngrok tcp 8880 &
/usr/sbin/lpadmin -d Zebra_Technologies_ZTC_ZM400-200dpi_ZPL
cd ./socket_test/
python sockets.py


