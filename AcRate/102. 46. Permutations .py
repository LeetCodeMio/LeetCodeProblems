from itertools import permutations as pm
class Solution :
	def permute(self, nums) :
		return list(pm(nums))