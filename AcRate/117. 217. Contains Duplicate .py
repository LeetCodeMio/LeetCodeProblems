class Solution :
	def containsDuplicate(self, nums) :
		vis = set()
		for i in nums :
			if i in vis : return True
			vis.add(i)
		return False