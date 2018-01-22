#!/usr/bin/env python

import socket
import time
from ipcCommon import ipcCommon
import msgContainer
import peekData


class ipcServer:
	def __init__(self, tcp_addr, tcp_port):
		self.tcp_addr = tcp_addr
		self.tcp_port = tcp_port
		self.server_socket = None
		self.msg_container = msgContainer.msgContainer()
		self.peek_data = peekData.peekData()
		self.server_running_flag = True
		self.client_running_flag = True


	def run(self):
		print("ipcServer is starting")
		try:
			self.__initialize()
			while self.server_running_flag:
				session_socket, client_addr = self.server_socket.accept()
				self.__handle_client_session(session_socket, client_addr)
		finally:
			self.__cleanup_at_exit()
		print("ipcServer terminates")


	def __handle_client_session(self, session_socket, client_addr):
		print("ipcServer: new connection from {}".format(client_addr))
		self.client_running_flag = True
		with session_socket:
			while self.client_running_flag:
				data_in = ipcCommon.recv_data(session_socket)
				if data_in:
					self.__process_incoming_message(data_in, session_socket)		
				else:
					print("ipcServer: client connection closed")
					self.client_running_flag = False


	def __initialize(self):
		self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.server_socket.bind((self.tcp_addr, self.tcp_port))
		self.server_socket.listen(10)


	def __process_incoming_message(self, data, session_socket):
		msg = data.decode()
		print("ipcServer: <== '{}'".format(msg))
		fields = msg.split("|")
		cmd = fields[0]
		if cmd == ipcCommon.get_cmd_send_message():
			self.__process_msg_push_request(fields, session_socket)

		elif cmd == ipcCommon.get_cmd_get_message():
			self.__process_msg_pull_request(fields, session_socket)

		elif cmd == ipcCommon.get_cmd_add_peeker():
			self.__process_add_peeker_request(fields, session_socket)

		elif cmd == ipcCommon.get_cmd_remove_peeker():
			self.__process_remove_peeker_request(fields, session_socket)

		elif cmd == ipcCommon.get_cmd_peek_message():
			self.__process_msg_peek_request(fields, session_socket)

		elif cmd == ipcCommon.get_cmd_clear_server():
			self.msg_container.clear()
			self.peek_data.clear()

		elif cmd == ipcCommon.get_cmd_stop_server():
			self.server_running_flag = False
		else:
			print("ipcServer: Unable to process '{}'".format(msg))


	def __process_msg_push_request(self, fields, session_socket):
		if not len(fields) == 4:
			print("Invalid msg push request: '{}'".format(fields))
			return
		from_node = fields[1]
		to_node = fields[2]
		msg = fields[3]
		self.msg_container.addMessage(from_node, to_node, msg)


	def __process_msg_pull_request(self, fields, session_socket):
		if not len(fields) == 3:
			print("Invalid msg pull request: '{}'".format(fields))
			return
		from_node = fields[1]
		to_node = fields[2]
		msg = self.msg_container.getMessage(from_node, to_node)
		if msg is None:
			msg = ""
		print("ipcServer: ==> '{}'".format(msg))
		ipcCommon.send_string(session_socket, msg)

	def __process_msg_peek_request(self, fields, session_socket):
		if not len(fields) == 2:
			print("Invalid msg peek request: '{}'".format(fields))
			return
		peeker_name = fields[1]
		msg = self.peek_data.getMessage(peeker_name)
		if msg is None:
			msg = ""
		print("ipcServer: ==> '{}'".format(msg))
		ipcCommon.send_string(session_socket, msg)


	def __process_add_peeker_request(self, fields, session_socket):
		if not len(fields) == 2:
			print("Invalid add peeker request: '{}'".format(fields))
			return
		peeker_name = fields[1]
		self.peek_data.addPeeker(peeker_name)


	def __process_remove_peeker_request(self, fields, session_socket):
		if not len(fields) == 2:
			print("Invalid remove peeker request: '{}'".format(fields))
			return
		peeker_name = fields[1]
		self.peek_data.removePeeker(peeker_name)


	def __cleanup_at_exit(self):
		if not self.server_socket is None:
			self.server_socket.shutdown(socket.SHUT_RDWR)
			self.server_socket.close()


def main():
	tcp_addr = ipcCommon.get_tcp_address()
	tcp_port = ipcCommon.get_tcp_port_number()
	ipc_server = ipcServer(tcp_addr, tcp_port)
	ipc_server.run()
	

if __name__ == '__main__':
	main()
			
