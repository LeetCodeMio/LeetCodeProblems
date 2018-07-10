from collections import Counter
class Solution(object) :
	def customSortString(self, S, T) :
		T = Counter(T)
		ret = ''
		for i in S :
			if i in T :
				ret += i * T[i]
				del(T[i])
		for k, v in T.items() : ret += k * v
		return ret