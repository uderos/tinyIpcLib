#!/usr/bin/env python
import ipcServer
from ipcCommon import ipcCommon

def test01():
	tcp_addr = ipcCommon.get_tcp_address()
	tcp_port = ipcCommon.get_tcp_port_number()
	server = ipcServer.ipcServer(tcp_addr, tcp_port)
	server.run()


def main():
	test01()

if __name__ == '__main__':
	main()

# End of file
