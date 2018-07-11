from collections import deque
class Solution :
	def levelOrder(self, root) :
		if not root : return []
		ret = []
		search = [root]
		while search :
			ret.append([])
			nsearch = []
			for node in search :
				ret[-1].append(node.val)
				if node.left : nsearch.append(node.left)
				if node.right : nsearch.append(node.right)
			search = nsearch
		return ret