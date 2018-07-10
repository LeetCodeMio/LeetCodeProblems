class Solution :
	def diameterOfBinaryTree(self, root) :
		def search(node) :
			if not node : return 0,0
			ldia, llen = search(node.left)
			rdia, rlen = search(node.right)
			return max(ldia, rdia, llen+rlen), max(llen,rlen) + 1
		return search(root)[0]