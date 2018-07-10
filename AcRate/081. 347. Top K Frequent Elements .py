from collections import Counter
class Solution :
	def topKFrequent(self, nums, k) :
		return [k for k,v in Counter(nums).most_common(k)]