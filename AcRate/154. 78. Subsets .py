from itertools import combinations as cb
class Solution :
	def subsets(self, nums) :
		return [list(i) for l in range(len(nums) + 1) for i in cb(nums, l)]