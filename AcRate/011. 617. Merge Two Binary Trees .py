class Solution(object) :
	def mergeTrees(self, t1, t2) :
		if t1 and t2 :
			ret = TreeNode(t1.val + t2.val)
			ret.left = self.mergeTrees(t1.left, t2.left)
			ret.right = self.mergeTrees(t1.right, t2.right)
			return ret
		return t1 or t2