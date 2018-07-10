class Solution : # 贪心
	def findMinArrowShots(self, points) :
		ret = 0
		end = float('-inf')
		for a,b in sorted(points) :
			ret, end = (ret+1, b) if a > end else (ret, min(end, b))
		return ret