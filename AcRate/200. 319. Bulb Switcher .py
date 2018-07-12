from math import sqrt,ceil
class Solution : # 归纳法
	def bulbSwitch(self, n) :
		return ceil(sqrt(n+1)) - 1
