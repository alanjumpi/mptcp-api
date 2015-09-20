#!/usr/bin/python

import socket
import mptcp_api #MPTCP API python interface

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.setsockopt(socket.IPPROTO_TCP, MPTCP_ENABLED, 1)
#s.setsockopt(socket.IPPROTO_TCP, TCP_MULTIPATH_ENABLED, 1)
#s.setsockopt(socket.IPPROTO_TCP, TCP_MULTIPATH_DEBUG, 1)
	
#try:
#	connid = mptcp_api.get_connid(s)	
#finally:
#	s.close()

#print connid 

try:
        n = 2
	result = mptcp_api.subflow_add(s, n)	
finally:
	s.close()

print result


