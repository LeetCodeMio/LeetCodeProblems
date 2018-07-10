# 时间O(n) 空间O(1) 禁用除法
class Solution :
	def productExceptSelf(self, nums) :
		ret = [1] * len(nums)
		for i in range(1, len(nums)) :
			ret[i] = ret[i-1] * nums[i-1]
		tmp = 1
		for i in range(1, len(nums)).__reversed__() :
			tmp *= nums[i]
			ret[i-1] *= tmp
		return ret