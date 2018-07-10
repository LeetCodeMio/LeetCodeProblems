class Solution :
	def maxProfit(self, p, fee) :
		T0, T1 = 0, -p[0] # T0/T1 当天 不持有/持有 股票的最大收益
		for i in p[1:] : T0, T1 = max(T0, T1+i-fee), max(T1, T0-i)
		return T0