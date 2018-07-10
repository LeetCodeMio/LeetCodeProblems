from collections import Counter
class Solution :
	def intersect(self, nums1, nums2) :
		nums1,nums2 = map(Counter, [nums1,nums2])
		return [n for n in nums1 if n in nums2
			for _ in range(min(nums1[n], nums2[n]))]