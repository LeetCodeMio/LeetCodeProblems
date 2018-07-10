from collections import Counter
class Solution :
	def longestPalindrome(self, s) :
		c = Counter(s).values()
		return sum(i//2*2 for i in c) + any(i%2 for i in c)