class Solution :
	def reverseStr(self, s, k) :
		return ''.join(s[i : i+k][::-1] + s[i+k : i+k*2]
			for i in range(0, len(s), k*2))