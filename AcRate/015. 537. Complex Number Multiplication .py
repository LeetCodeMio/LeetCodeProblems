class Solution(object) :
	def complexNumberMultiply(self, a, b) :
		def com(x) :
			x = x.replace('+-', '-')
			x = x.replace('i', 'j')
			return complex(x)
		ans = com(a) * com(b)
		return str(int(ans.real)) + '+' + str(int(ans.imag)) + 'i'