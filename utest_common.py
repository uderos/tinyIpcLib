#!/usr/bin/env python
#import ipcCommon
from ipcCommon import ipcCommon
		
def test01():
	cmd_send 	= ipcCommon.get_cmd_send_message()
	cmd_get 	= ipcCommon.get_cmd_get_message()
	cmd_clear 	= ipcCommon.get_cmd_clear_server()
	cmd_stop 	= ipcCommon.get_cmd_stop_server()
	print("cmd_send : {}".format(cmd_send ))
	print("cmd_get  : {}".format(cmd_get  ))
	print("cmd_clear: {}".format(cmd_clear))
	print("cmd_stop : {}".format(cmd_stop ))

def test02():
	print("\n TEST 02")


def test03():
	print("\n TEST 03")

def main():
	test01()
	#test02()
	#test03()

if __name__ == '__main__':
	main()
