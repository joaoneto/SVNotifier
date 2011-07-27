#!/usr/bin/env python
"""
svnotifier.py: Client to receive notifications of changes to the svn repository

links:
http://wiki.python.org/moin/UdpCommunication
http://www.doughellmann.com/PyMOTW/socket/multicast.html
"""
__version__ = "0.1"
__author__ = "João Pinto Neto (joaopintoneto@gmail.com)"
__copyright__ = "(C) 2011. GNU GPL 3."

import socket, struct, sys

multicast_group = '224.3.29.71'
server_address = ('', 10000)

# Create the socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind to the server address
sock.bind(server_address)

# Tell the operating system to add the socket to the multicast group
# on all interfaces.
group = socket.inet_aton(multicast_group)
mreq = struct.pack('4sL', group, socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

# Receive/respond loop
while True:
    data, address = sock.recvfrom(1024)
    print >>sys.stderr, data

