class Solution :
	def rotatedDigits(self, N) :
		ret = 0
		for i in range(1, N+1) :
			if any(j in str(i) for j in '347') : continue
			if all(j not in str(i) for j in '2569') : continue
			ret += 1
		return ret