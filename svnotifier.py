#! /usr/bin/python
# -*- coding: UTF-8 -*-
"""
svnotifier.py: Client to receive notifications of changes to the svn repository

links:
http://wiki.python.org/moin/UdpCommunication
http://www.doughellmann.com/PyMOTW/socket/multicast.html
"""
__version__ = "0.2"
__author__ = "João Pinto Neto (joaopintoneto@gmail.com)"
__copyright__ = "(C) 2011. GNU GPL 3."

import sys
import os
import socket
import struct
from time import sleep
import pynotify
import locale

class MainWindow(object):
    def __init__(self):
        multicast_group = '224.3.29.71'
        server_address = ('', 10000)

        # Create the socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # Bind to the server address
        self.sock.bind(server_address)

        # Tell the operating system to add the socket to the multicast group
        # on all interfaces.
        group = socket.inet_aton(multicast_group)
        mreq = struct.pack('4sL', group, socket.INADDR_ANY)
        self.sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

    def notificar(self, title, msg):
        encoding = (locale.getdefaultlocale())[1]

        if pynotify.init('mcnotify'):
            n = pynotify.Notification(unicode(title, encoding, 'ignore'), unicode(msg, encoding, 'ignore'), 'server')
            n.show()


    def verificarStatus(self):
        data, address = self.sock.recvfrom(1024)
        self.notificar('SVNotifier', data)


if __name__ == '__main__':
    m = MainWindow()

    while True:
        try:
            m.verificarStatus()
        except:
            print "\nGood Bye!"
            break

