class Solution : # 动态规划
	def maxProfit(self, p) :
		if not p : return 0
		f,g = -p[0], 0 # 第i=0天 持有/不持有 股票的最大收益
		for i in p[1:] :
			f,g = max(-i, f), max(f+i, g)
		return g