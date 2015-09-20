#!/usr/bin/python

import socket
import netifaces
from netifaces import AF_INET

TCP_MULTIPATH_CONNID = 10006
TCP_MULTIPATH_ADD = 10003

def get_connid(s):
	set_conn = False
	try:
		address = netifaces.ifaddresses('eth0')[AF_INET][0]['addr']
		print address
		s.bind((address, 0))
		set_conn = True
	except:
		pass
	if not set_conn:
		raise Exception('Socket not bind') 		
	conn_id = s.getsockopt(socket.IPPROTO_TCP, TCP_MULTIPATH_CONNID) 
	return conn_id

def subflow_add(s,n):
	set_conn = False
	try:
		address = netifaces.ifaddresses('eth0')[AF_INET][0]['addr']
		s.bind((address, 0))
		set_conn = True
	except:
		pass
	if not set_conn:
		raise Exception('Socket not bind') 		
	s.setsockopt(socket.IPPROTO_TCP, TCP_MULTIPATH_ADD, n)
