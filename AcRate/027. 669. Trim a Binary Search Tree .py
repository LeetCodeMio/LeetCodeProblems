class Solution(object) :
	def trimBST(self, root, L, R) :
		trim = lambda n : self.trimBST(n, L, R)
		if root.val < L :
			return trim(root.right) if root.right else None
		if root.val > R :
			return trim(root.left) if root.left else None
		if root.left : root.left = trim(root.left)
		if root.right : root.right = trim(root.right)
		return root