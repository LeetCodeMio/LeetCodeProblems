class Solution :
	def titleToNumber(self, s) :
		ret = 0
		for i in s :
			ret *= 26
			ret += 1 + ord(i) - ord('A')
		return ret