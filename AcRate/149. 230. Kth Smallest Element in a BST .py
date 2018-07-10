class Solution :
	def kthSmallest(self, root, k) :
		count = 0
		stack = [(root, True)]
		while True :
			node, flag = stack.pop()
			if flag :
				stack.append((node, False))
				if node.left : stack.append((node.left,True))
			else :
				if node.right : stack.append((node.right, True))
				count += 1
				if count == k : return node.val