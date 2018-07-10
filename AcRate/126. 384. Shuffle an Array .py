from random import shuffle
class Solution :
	def __init__(self, nums) :
		self.nums = nums
	def reset(self) :
		return self.nums
	def shuffle(self) :
		ret = self.nums.copy()
		shuffle(ret)
		return ret