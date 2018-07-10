class Solution :
	def sumOfLeftLeaves(self, root) :
		if not root : return 0
		ret = 0
		stack = [root]
		while stack :
			node = stack.pop()
			if node.left :
				if not (node.left.left or node.left.right):
					ret += node.left.val
				stack.append(node.left)
			if node.right : stack.append(node.right)
		return ret