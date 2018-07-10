import numpy as np
class Solution :
	def constructRectangle(self, area) :
		W = int(np.sqrt(area))
		while area % W : W -= 1
		return [area // W, W]