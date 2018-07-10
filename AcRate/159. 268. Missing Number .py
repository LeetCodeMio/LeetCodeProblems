class Solution : # t=O(n) m=O(1)
	def missingNumber(self, nums) :
		n = len(nums)
		return (n+1)*n//2 - sum(nums)