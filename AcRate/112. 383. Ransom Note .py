from collections import Counter as C
class Solution :
	def canConstruct(self, a, b) :
		a, b = C(a), C(b)
		return all(i in b and ni <= b[i] for i,ni in a.items())