# 从后向前扫描 针对没找到答案的再从前往后扫描
class Solution :
	def nextGreaterElements(self, nums) :
		if not nums : return []
		ret = [-1] * len(nums)
		stack = []
		rest = []
		for i in reversed(range(len(nums))) :
			while stack and stack[-1] <= nums[i] : stack.pop()
			if stack : ret[i] = stack[-1]
			else : rest.append(i)
			stack.append(nums[i])
		rest.reverse()
		m = nums[rest[0]]
		for i in nums :
			if nums[rest[-1]] == m : return ret
			while nums[rest[-1]] < i :
				ret[rest.pop()] = i