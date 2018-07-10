class Solution :
	def convertToBase7(self, num) :
		ret = ''
		absnum = abs(num)
		while absnum :
			ret += str(absnum % 7)
			absnum //= 7
		if not ret : ret = '0' # corner case
		return ('-' if num < 0 else '') + ret[::-1]