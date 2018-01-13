#!/usr/bin/env python
import ipcCacClient
import ipcClient
import ipcServer
import msgContainer
from ipcCommon import ipcCommon

def msg_to_string(msg):
	if msg is None:
		return '(none)'
	return msg
		
def test01():
	print("\n TEST 01")
	tcp_addr = ipcCommon.get_tcp_address()
	tcp_port = ipcCommon.get_tcp_port_number()
	client1 = ipcClient.ipcClient('Client1', tcp_addr, tcp_port)
	client1.sendMessage('Client2', 'msg1')
	client2 = ipcClient.ipcClient('Client2', tcp_addr, tcp_port)
	msg = None
	msg = client2.getMessage('Client1')
	print("msg='{}'".format(msg_to_string(msg)))
	msg = None

	client1.sendMessage('Client2', 'msg2')
	client1.sendMessage('Client2', 'msg3')
	msg = None
	msg = client2.getMessage('Client1')
	print("msg='{}'".format(msg))
	msg = None
	msg = client2.getMessage('Client1')
	print("msg='{}'".format(msg))
	msg = None
	msg = client2.getMessage('Client1')
	print("msg='{}'".format(msg))

	client1.clearServer()

def test02():
	print("\n TEST 02")
	client1 = ipcCacClient.ipcCacClient('Client1')
	client2 = ipcCacClient.ipcCacClient('Client2')

	client1.sendValueList('Client2', [1, 0, 0, 1])
	client1.sendValueList('Client2', [0, 0, 1, 1])

	bl1 = client2.getValueList('Client1')
	print("BitList1 = {}".format(bl1))

	bl2 = client2.getValueList('Client1')
	print("BitList2 = {}".format(bl2))
	client1.clearServer()


def test03():
	print("\n TEST 03")
	client1 = ipcCacClient.ipcCacClient('Client1')
	client2 = ipcCacClient.ipcCacClient('Client2')
	client1.sendAck('Client2')
	client2.getAck('Client1')
	client1.clearServer()

def test04():
	print("\n TEST 04")
	client1 = ipcCacClient.ipcCacClient('Client1')
	client2 = ipcCacClient.ipcCacClient('Client2')

	client1.clearServer()
	vlist_out = [ 1, 3, 5, 7 ]
	client1.sendValueList('Client2', vlist_out)
	vlist_in = client2.getValueList('Client1')
	if not vlist_out == vlist_in:
		print("# MISMATCH #: '{}' '{}'".format(vlist_out, vlist_in))
	client1.clearServer()

def test05():
	print("\n TEST 05")
	client1 = ipcCacClient.ipcCacClient('Client1')
	client2 = ipcCacClient.ipcCacClient('Client2')
	client1.clearServer()

	client1.sendValueList('Client2', [1, 0, 0, 1])
	client1.sendValueList('Client2', [0, 0, 1, 1])

	bl1 = client2.getValueList('Client1')
	print("BitList1 = {}".format(bl1))

	bl2 = client2.getValueList('Client1')
	print("BitList2 = {}".format(bl2))
	client1.clearServer()


def test_last():
	client1 = ipcCacClient.ipcCacClient('Client1')
	client1.closeChannel()

def main():
	test01()
	test02()
	test03()
	test04()
	test05()
	test_last()

if __name__ == '__main__':
	main()
