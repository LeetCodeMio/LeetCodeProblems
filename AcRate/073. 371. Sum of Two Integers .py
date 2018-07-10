# not allowed to use the operator + and -
class Solution :
	def getSum(self, a, b) :
		while b :
			c = a & b
			a = (a ^ b) & 0xffffffff
			b = (c << 1) & 0xffffffff
		if a & 0xe0000000 : return ~(a ^ 0xffffffff)
		return a