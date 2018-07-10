class Solution(object) :
	def pruneTree(self, root) :
		if root.left : root.left = self.pruneTree(root.left)
		if root.right : root.right = self.pruneTree(root.right)
		if root.left or root.right or root.val : return root
		return None