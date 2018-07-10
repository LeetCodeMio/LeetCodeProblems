class Solution :
	def isSameTree(self, rootA, rootB) :
		stackA, stackB = [rootA], [rootB]
		while stackA or stackB :
			if not(stackA and stackB) : return False
			nodeA, nodeB = stackA.pop(), stackB.pop()
			if nodeA or nodeB :
				if not(nodeA and nodeB) : return False
				if nodeA.val != nodeB.val : return False
				stackA.extend([nodeA.left, nodeA.right])
				stackB.extend([nodeB.left, nodeB.right])
		return True