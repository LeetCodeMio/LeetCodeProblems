# [1,10**6]中的数的set bits不会超过20个
class Solution(object) :
	def countPrimeSetBits(self, L, R) :
		p = {2,3,5,7,11,13,17,19}
		return sum(bin(i).count('1') in p for i in range(L,R+1))