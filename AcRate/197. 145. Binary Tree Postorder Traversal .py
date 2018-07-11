class Solution :
	def postorderTraversal(self, root) :
		if not root : return []
		ret = []
		stack = [(root, False)]
		while stack :
			node, vis = stack.pop()
			if not vis :
				stack.append((node, True))
				if node.right : stack.append((node.right, False))
				if node.left : stack.append((node.left, False))
			else : ret.append(node.val)
		return ret
