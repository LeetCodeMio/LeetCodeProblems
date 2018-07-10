class Solution :
	def romanToInt(self, s) :
		dic = {'M':1000, 'CM':900, 'D':500, 'CD':400,
			'C':100, 'XC':90, 'L':50, 'XL':40,
			'X':10, 'IX':9, 'V':5, 'IV':4, 'I':1}
		ret = 0
		i = 0
		while i < len(s) :
			if i+2 <= len(s) and s[i:i+2] in dic :
				ret += dic[s[i:i+2]]
				i += 2
			else :
				ret += dic[s[i]]
				i += 1
		return ret