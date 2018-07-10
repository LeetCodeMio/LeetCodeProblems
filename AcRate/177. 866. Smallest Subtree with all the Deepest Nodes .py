class Solution :
	def subtreeWithAllDeepest(self, root) :
		def search(node, depth) :
			if not node : return depth, None
			ldepth, lnode = search(node.left, depth+1)
			rdepth, rnode = search(node.right, depth+1)
			if ldepth == rdepth : return ldepth, node
			return max((ldepth, lnode), (rdepth, rnode))
		return search(root, 0)[1]