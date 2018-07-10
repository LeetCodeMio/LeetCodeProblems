from collections import Counter as ct
class Solution(object) :
	def shortestCompletingWord(self, licensePlate, words) :
		ans = None
		license = ct(i.lower() for i in licensePlate if i.isalpha())
		for i in words :
			tmp = ct(i)
			if all(k in tmp and tmp[k] >= v for k,v in license.items()) :
				ans = ans if ans and len(i) >= len(ans) else i
		return ans