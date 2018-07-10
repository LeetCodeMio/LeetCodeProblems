class NestedIterator :
	def __init__(self, nestedList) :
		self.stack = [iter(nestedList)]
		self.dfs()
	def dfs(self) :
		while self.stack :
			try : node = next(self.stack[-1])
			except : self.stack.pop(); continue
			if node.isInteger() :
				self.stack.append(node.getInteger()); return
			self.stack.append(iter(node.getList()))
	def next(self) :
		ret = self.stack.pop()
		self.dfs()
		return ret
	def hasNext(self) :
		return bool(self.stack)