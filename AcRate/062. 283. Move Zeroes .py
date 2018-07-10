# 在原数组上施加最少的操作
class Solution :
	def moveZeroes(self, nums) :
		count = 0
		for i in range(len(nums)) :
			if nums[i] : nums[i - count] = nums[i]
			else : count += 1
		for i in range(-1, -count-1, -1) : nums[i] = 0