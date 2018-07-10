class Solution :
	def maxChunksToSorted(self, arr) :
		m = arr[0]
		ret = 0
		for i,x in enumerate(arr) :
			m = max(m, x)
			ret += i == m
		return ret