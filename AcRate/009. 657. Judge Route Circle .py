class Solution(object) :
	def judgeCircle(self, moves) :
		c = moves.count
		return c('U') == c('D') and c('L') == c('R')