class Solution :
	def myAtoi(self, s) :
		s = s.lstrip()
		if not (s and s[0] in '-+0123456789') : return 0
		for end in range(1, len(s)+1) :
			if end < len(s) and s[end].isdigit() : continue
			if not s[end-1].isdigit() : return 0
			return max(min(int(s[:end]), 2**31 - 1), -2**31)
