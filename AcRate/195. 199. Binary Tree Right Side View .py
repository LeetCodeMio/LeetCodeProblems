class Solution : # 广搜
	def rightSideView(self, root) :
		if not root : return []
		ret = []
		search = [root]
		while search :
			ret.append(search[-1].val)
			nsearch = []
			for node in search :
				if node.left : nsearch.append(node.left)
				if node.right : nsearch.append(node.right)
			search = nsearch
		return ret
