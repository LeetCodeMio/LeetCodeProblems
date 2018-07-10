class Solution(object) :
	def hasAlternatingBits(self, n) :
		n = bin(n)[2:]
		for i in range(1, len(n)) :
			if n[i] == n[i-1] : return False
		return True