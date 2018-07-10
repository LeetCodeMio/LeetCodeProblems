# 枚举
from itertools import combinations as cb
class Solution(object) :
	def largestTriangleArea(self, points) :
		def area(i) :
			[x1,y1], [x2,y2], [x3,y3] = i
			return abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) / 2
		return max(area(i) for i in cb(points, 3))