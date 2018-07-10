import numpy as np
class Solution :
	def maxCount(self, m, n, ops) :
		if not ops : return m * n
		return int(np.multiply(*np.min(ops, 0)))