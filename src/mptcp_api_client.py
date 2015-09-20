#!/usr/bin/python

import socket
import mptcp_api
import subprocess

subprocess.call('sysctl -w net.mptcp.mptcp_enabled=1', shell=True)
subprocess.call('sysctl -w net.mptcp.mptcp_debug=1', shell=True)
subprocess.call('sysctl -w net.mptcp.mptcp_path_manager=fullmesh', shell=True)

SERVER_ADDR="192.168.22.44"
SERVER_PORT=22222

num_subflows = 2

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mptcp_api.subflow_add(s, num_subflows)

try:
#	r = mptcp_api.get_connid(s)
	#print r
	s.connect((SERVER_ADDR, SERVER_PORT))
	while True:
		recv_now = s.recv(1024)
		if not recv_now:
			break
finally:
	s.close()
