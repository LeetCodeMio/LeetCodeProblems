class Solution :
	def twoSum(self, nums, target) :
		b, e = 0, len(nums) - 1
		while nums[b] + nums[e] != target :
			if target - nums[b] < nums[e] : e -= 1
			else : b += 1
		return b + 1, e + 1