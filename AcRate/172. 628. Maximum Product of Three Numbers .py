from heapq import nsmallest, nlargest
from itertools import combinations
class Solution : # 经过观察 一定是从最大3个和最小3个中选3个相乘
	def maximumProduct(self, nums) :
		if len(nums) >= 6 :
			nums = nsmallest(3, nums) + nlargest(3, nums)
		return max(a*b*c for a,b,c in combinations(nums, 3))