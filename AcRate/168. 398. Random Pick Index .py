from random import randint
class Solution :
	def __init__(self, nums) :
		self.indexs = {}
		for i,x in enumerate(nums) :
			self.indexs.setdefault(x, []).append(i)
	def pick(self, target) :
		indexs = self.indexs[target]
		return indexs[randint(0, len(indexs) - 1)]