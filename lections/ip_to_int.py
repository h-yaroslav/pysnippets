#!/usr/bin/python
import socket
import struct

print socket.inet_ntoa(struct.pack('>I',long(212665105)))
#'12.173.3.17'
print struct.unpack('>I', socket.inet_aton('127.0.0.1'))[0]
#2130706433