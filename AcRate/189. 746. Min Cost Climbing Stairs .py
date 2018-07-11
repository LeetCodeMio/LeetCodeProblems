class Solution(object) : # 动态规划
	def minCostClimbingStairs(self, cost) :
		cost += [0]
		f_1,f_2 = cost[1], cost[0]
		for i in range(2, len(cost)) :
			f = cost[i] + min(f_1, f_2)
			f_1,f_2 = f,f_1
		return f