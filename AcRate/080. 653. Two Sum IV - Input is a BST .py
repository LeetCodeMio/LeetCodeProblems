class Solution :
	def findTarget(self, root, k) :
		if not root : return False
		stack = [root]
		while stack :
			node = stack.pop()
			if node.left : stack.append(node.left)
			if node.right : stack.append(node.right)
			other = k - node.val
			if other == node.val : continue
			search = root
			while search :
				if search.val == other : return True
				elif search.val < other : search = search.right
				else : search = search.left
		return False