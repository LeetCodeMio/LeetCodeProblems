class Solution(object):
	def selfDividingNumbers(self, left, right) :
		ret = []
		for i in range(left, right+1) :
			if '0' in str(i) : continue
			if any([i % int(j) for j in str(i)]) : continue
			ret += [i]
		return ret