# 时间O(n) 空间O(0)
class Solution :
	def findDisappearedNumbers(self, nums) :
		# 规定nums[i]只能是i+1或者0
		for i in range(len(nums)) :
			while nums[i] and nums[i] != i+1 :
				j = nums[i] - 1
				a, b = nums[i], nums[j]
				if a == b : b = 0
				nums[i], nums[j] = b, a
		return [i+1 for i in range(len(nums)) if not nums[i]]