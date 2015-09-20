#!/usr/bin/python

import socket
import subprocess

server_port = 22222

#machine
subprocess.call('sysctl -w net.mptcp.mptcp_enabled=1', shell=True)
subprocess.call('sysctl -w net.mptcp.mptcp_debug=1', shell=True)
subprocess.call('sysctl -w net.mptcp.mptcp_path_manager=fullmesh', shell=True)
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
 
amount_bytes = 32 * 1024 * 1024
 
try:
    s.bind(('', server_port))
    s.listen(1)
    (cs, caddr) = s.accept()
    print 'Client connected!'
    try:
      chunk = bytearray(['x'] * 1024)
      sent_bytes = 0
      while sent_bytes < amount_bytes:
        sent_now = cs.send(chunk)
        if not sent_now:
          break
        sent_bytes = sent_bytes + sent_now
 
    finally:
      cs.close()
finally:
    s.close()

