class Solution :
	def minDiffInBST(self, root) :
		last, ret = None, None
		stack = [(root, True)]
		while stack :
			node, left = stack.pop()
			if left :
				stack.append((node, False))
				if node.left : stack.append((node.left, True))
			else :
				if node.right : stack.append((node.right, True))
				if ret is not None : ret = min(ret, node.val - last)
				elif last is not None : ret = node.val - last
				last = node.val
		return ret