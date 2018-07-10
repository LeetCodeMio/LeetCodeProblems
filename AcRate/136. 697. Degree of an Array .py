class Solution :
	def findShortestSubArray(self, nums) :
		count = {}
		for i,x in enumerate(nums) :
			if x not in count :
				count[x] = [-1, i, i]
			else :
				count[x][0] -= 1
				count[x][2] = i
		return min((n, b - a) for n,a,b in count.values())[1] + 1