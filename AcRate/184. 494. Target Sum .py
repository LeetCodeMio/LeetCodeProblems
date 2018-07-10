from collections import defaultdict
class Solution : # 有限态空间游走
	def findTargetSumWays(self, nums, S) :
		if not nums : return 0
		ret = defaultdict(int)
		ret[nums[0]] += 1
		ret[-nums[0]] += 1
		for i in nums[1:] :
			tmp = defaultdict(int)
			for k,v in ret.items() : tmp[k+i] += v
			for k,v in ret.items() : tmp[k-i] += v
			ret = tmp
		return ret[S]