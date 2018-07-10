# 索引排序
class Solution :
	def findRelativeRanks(self, nums) :
		nums = sorted((-x,i) for i,x in enumerate(nums))
		ret = [''] * len(nums)
		for rank,(_,i) in enumerate(nums) :
			ret[i] = str(rank+1)
		for medal,(_,i) in zip(('Gold','Silver','Bronze'), nums) :
			ret[i] = medal + ' Medal'
		return ret