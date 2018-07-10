import numpy as np
class Solution(object) :
	def maxIncreaseKeepingSkyline(self, grid) :
		maxI = np.max(grid, 1) # 行天际线
		maxJ = np.max(grid, 0) # 列天际线
		ran = range(len(grid))
		# 题目要求返回int
		# 不做类型转换返回的是numpy.int64
		return int(sum([min(maxI[i], maxJ[j]) - grid[i][j]
			for i in ran for j in ran]))