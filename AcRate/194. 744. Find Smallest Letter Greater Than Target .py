from bisect import bisect
class Solution : # 二分查找
	def nextGreatestLetter(self, letters, target) :
		return letters[bisect(letters, target) % len(letters)]
