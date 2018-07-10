import numpy as np
class Solution(object) :
	def constructMaximumBinaryTree(self, nums) :
		con = self.constructMaximumBinaryTree
		arg = np.argmax(nums)
		ret = TreeNode(nums[arg])
		if arg != 0 : ret.left = con(nums[:arg])
		if arg+1 != len(nums) : ret.right = con(nums[arg+1:])
		return ret