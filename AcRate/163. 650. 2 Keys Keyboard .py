class Solution : # 归纳法 return n的质因数之和
	def minSteps(self, n) :
		ret = 0
		while n != 1:
			for i in range(2, n+1) :
				if n%i == 0 :
					n //= i
					ret += i
					break
		return ret