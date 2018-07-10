class Solution(object) :
	def numberOfLines(self, widths, S) :
		c = 0
		l = 1
		for i in S :
			dc = widths[ord(i) - ord('a')]
			if c + dc <= 100 : c += dc
			else :
				l += 1
				c = dc
		return [l, c]