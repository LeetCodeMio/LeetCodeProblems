# 递推
class Solution :
	def countBinarySubstrings(self, s) :
		ret = 0
		last = s[0]
		diff = 0
		same = 1
		for i in s[1:] :
			if i == last :
				same += 1
				ret += same <= diff
			else :
				last = i
				diff = same
				same = 1
				ret += 1
		return ret