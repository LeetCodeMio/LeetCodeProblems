class Solution :
	def firstUniqChar(self, s) :
		meet = []
		uniq = {}
		for i,x in enumerate(s) :
			if x in uniq :
				uniq[x] = False
			else :
				uniq[x] = True
				meet.append((i,x))
		for i,x in meet :
			if uniq[x] : return i
		return -1