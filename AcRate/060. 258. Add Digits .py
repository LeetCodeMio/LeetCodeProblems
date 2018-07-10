# 请观察：
# 1 10 19 28
# 2 11 20 29
# 3 12 21 30
# 4 13 22 31
# 5 14 23 .
# 6 15 24 .
# 7 16 25 .
# 8 17 26
# 9 18 27
class Solution(object) :
	def addDigits(self, num) :
		if num == 0 : return 0
		num %= 9
		return num if num else 9