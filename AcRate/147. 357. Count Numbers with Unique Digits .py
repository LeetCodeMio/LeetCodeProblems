class Solution : # n=4 : 9*9*8*7+9*9*8+9*9+9+1
	def countNumbersWithUniqueDigits(self, n) :
		return [1,10,91,739,5275,32491,168571,712891,
			2345851,5611771,8877691][min(10, n)]