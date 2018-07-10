# nums一定是若干独立的闭环
# 找出nums里最长的闭环
class Solution :
	def arrayNesting(self, nums) :
		ans = 0
		vis = [False] * len(nums)
		for i in range(len(nums)) :
			if vis[i] : continue
			vis[i] = True
			count = 1
			j = i
			while nums[j] != i :
				j = nums[j]
				vis[j] = True
				count += 1
			ans = max(ans, count)
		return ans