class Solution :
	def maxProfit(self, p) :
		return sum(p[i] - p[i-1] for i in range(1, len(p)) if p[i] > p[i-1])