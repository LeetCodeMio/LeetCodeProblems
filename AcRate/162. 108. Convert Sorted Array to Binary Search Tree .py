class Solution :
	def sortedArrayToBST(self, nums) :
		def build(nums) :
			if not nums : return None
			c = len(nums) // 2
			ret = TreeNode(nums[c])
			ret.left = build(nums[:c])
			ret.right = build(nums[c+1:])
			return ret
		return build(nums)