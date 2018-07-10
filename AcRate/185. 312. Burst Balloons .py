class Solution : # 分治 动态规划
	def maxCoins(self, nums) :
		nums = [1] + nums + [1]
		coins = [[0 for i in nums] for j in nums]
		# coins[a][b] = 子区间(a,b)的最大得分
		for b in range(2, len(nums)) :
			for a in reversed(range(b-1)) :
				coins[a][b] = max(coins[a][c] + coins[c][b]
					+ nums[a] * nums[c] * nums[b]
					for c in range(a+1, b))
		return coins[0][len(nums) - 1]