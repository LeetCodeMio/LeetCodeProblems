# S1[a][b] 表示局面为nums[a:b+1]且玩家1先行时 玩家1的最终score
# S2[a][b] 表示局面为nums[a:b+1]且玩家2先行时 玩家1的最终score
# S1[a][b] = max(nums[a] + S2[a+1][b], nums[b] + S2[a][b-1])
# S2[a][b] = min(S1[a+1][b], S1[a][b-1])
# S1[a][a] = nums[a], S2[a][a] = 0
class Solution : # 动态规划
	def PredictTheWinner(self, nums) :
		S1 = nums.copy()
		S2 = [0] * len(nums)
		for b in range(1, len(nums)) :
			for a in reversed(range(b)) :
				S1a = max(nums[a] + S2[a+1], nums[b] + S2[a])
				S2a = min(S1[a+1], S1[a])
				S1[a], S2[a] = S1a, S2a
		return S1[0] * 2 >= sum(nums)