class Solution :
	def printTree(self, root) :
		m = 1
		stack = [(root, 1)]
		while stack :
			node, depth = stack.pop()
			m = max(m, depth)
			if node.left : stack.append((node.left, depth+1))
			if node.right : stack.append((node.right, depth+1))
		n = 2**m - 1
		ret = [['' for i in range(n)] for j in range(m)]
		stack = [(root, 0, n // 2, n // 2)]
		while stack :
			node, depth, pos, space = stack.pop()
			ret[depth][pos] = str(node.val)
			space //= 2
			if node.left : stack.append(
				(node.left, depth+1, pos-1-space, space))
			if node.right : stack.append(
				(node.right, depth+1, pos+1+space, space))
		return ret