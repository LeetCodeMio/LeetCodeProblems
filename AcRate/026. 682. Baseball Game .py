class Solution(object) :
	def calPoints(self, ops) :
		valid = []
		ret = 0
		for i in ops :
			if i == 'C' :
				ret -= valid.pop()
				continue
			elif i == 'D' : s = valid[-1] * 2
			elif i == '+' : s = sum(valid[-2:])
			else : s = int(i)
			valid += [s]
			ret += s
		return ret