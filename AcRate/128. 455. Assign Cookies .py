# 贪心
class Solution :
	def findContentChildren(self, g, s) :
		g.sort()
		s.sort()
		ret = 0
		gi, si = 0, 0
		while gi < len(g) and si < len(s) :
			if g[gi] <= s[si] :
				ret += 1
				gi += 1
			si += 1
		return ret