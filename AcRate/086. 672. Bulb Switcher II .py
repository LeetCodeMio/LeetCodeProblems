# 枚举
class Solution :
	def flipLights(self, n, m) :
		if n == 0 : return 0
		if m == 0 : return 1
		if n == 1 : return 2
		if n == 2 : return 3 if m == 1 else 4
		if m == 1 : return 4
		if m == 2 : return 7
		return 8