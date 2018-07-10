class Solution(object) :
	def findMaxConsecutiveOnes(self, nums) :
		ans = 0
		lenth = 0
		for i in range(len(nums)) :
			if nums[i] : lenth += 1
			else :
				ans = max(ans, lenth)
				lenth = 0
		return max(ans, lenth)