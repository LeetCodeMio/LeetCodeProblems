class Solution :
	def preorderTraversal(self, root) :
		stack = [root]
		ret = []
		while stack :
			node = stack.pop()
			if node :
				ret.append(node.val)
				stack.append(node.right)
				stack.append(node.left)
		return ret