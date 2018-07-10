class Solution :
	def addOneRow(self, root, v, d) :
		if d == 1 :
			ret = TreeNode(v)
			ret.left = root
			return ret
		stack = [(root, 1)]
		while stack :
			node, depth = stack.pop()
			if depth != d-1 :
				if node.left : stack.append((node.left, depth+1))
				if node.right : stack.append((node.right, depth+1))
			else :
				left, right = node.left, node.right
				node.left, node.right = TreeNode(v), TreeNode(v)
				node.left.left, node.right.right = left, right
		return root