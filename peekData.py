
class peekData:
	def __init__(self):
		self.data = []

	def __str__(self):
		return str(self.data)

	def __repr__(self):
		return repr(self.data)

	def clear(self):
		self.data = []

	def addPeeker(self, peekerName, memSize = 0):
		self.removePeeker(peekerName)
		new_elem = [ (peekerName, memSize), [] ]
		self.data.append(new_elem)

	def removePeeker(self, peekerName):
		for i in range(len(self.data)):
			if self.data[i][0][0] == peekerName:
				self.data.pop(i)
				return
	def addMessage(self, fromNode, toNode, msg):
		new_elem = (fromNode, toNode, msg)
		for elem in self.data:
			header = elem[0]
			msg_list = elem[1]
			maxMem = header[1]
			if (maxMem > 0) and (len(msg_list) >= maxMem):
				msg_list.pop(0)
			msg_list.append(new_elem)

	def getMessage(self, peekerName):
		for elem in self.data:
			header = elem[0]
			if peekerName == header[0]:
				msg_list = elem[1]
				if len(msg_list) > 0:
					return msg_list.pop(0)

	def dump(self):
		print("peekData Dump: {} elements".format(len(self.data)))
		for elem in self.data:
			print("\t{}".format(elem))
		

#############################################################################
# UNIT TESTING
#############################################################################

def test_assert(predicate):
	if not predicate:
		raise RuntimeError('# TEST ASSERTION FAILURE #')

def utest1():
	print("\nutest1 == BEGIN")
	p = peekData()
	print("After construction: dump='{}'".format(p))

	p.addPeeker('p1')
	print("After adding p1: dump='{}'".format(p))
	p.addPeeker('p2', 2)
	print("After adding p2: dump='{}'".format(p))

	p.addMessage('f1', 't1', 'm1')
	print("After adding m1: dump='{}'".format(p))

	p.addMessage('f2', 't2', 'm2')
	p.addMessage('f3', 't3', 'm3')
	p.addMessage('f4', 't4', 'm4')
	print("After adding 3 mode msgs: dump='{}'".format(p))

	test_assert(p.getMessage('p1') == ('f1', 't1', 'm1'))
	test_assert(p.getMessage('p1') == ('f2', 't2', 'm2'))
	test_assert(p.getMessage('p1') == ('f3', 't3', 'm3'))
	test_assert(p.getMessage('p1') == ('f4', 't4', 'm4'))
	test_assert(p.getMessage('p1') is None)
	test_assert(p.getMessage('p1') is None)

	test_assert(p.getMessage('p2') == ('f3', 't3', 'm3'))
	test_assert(p.getMessage('p2') == ('f4', 't4', 'm4'))
	test_assert(p.getMessage('p2') is None)
	test_assert(p.getMessage('p2') is None)


def utest2():
	print("\nutest2 == BEGIN")
	p = peekData()
	p.addPeeker('p1')
	p.addPeeker('p2', 2)
	p.addPeeker('p3', 3)
	p.addMessage('f1', 't1', 'm1')
	p.addMessage('f1', 't1', 'm2')
	p.addMessage('f1', 't1', 'm3')
	p.addMessage('f1', 't1', 'm4')
	print("Full container: dump='{}'".format(p))

	p.removePeeker('p2')
	print("After deleting p2: dump='{}'".format(p))
	p.removePeeker('p1')
	print("After deleting p1: dump='{}'".format(p))
	p.removePeeker('p3')
	print("After deleting p3: dump='{}'".format(p))


def unit_test():
	utest1()
	utest2()
	print("\n == SUCCESS ==")

if __name__ == '__main__':
	unit_test()
			

	
