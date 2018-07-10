class BSTIterator() :
	def __init__(self, root) :
		self.stack = [(root, False)] if root else []
	def hasNext(self) : return bool(self.stack)
	def next(self) :
		while self.stack :
			node, vis = self.stack.pop()
			if vis :
				if node.right :
					self.stack.append((node.right, False))
				return node.val
			self.stack.append((node, True))
			if node.left :
				self.stack.append((node.left, False))