# 绝对值不等式
# 求数轴上一点到nums中所有点连线之和最短
# 这一点就是中位数
class Solution :
	def minMoves2(self, nums) :
		mean = sorted(nums)[len(nums) // 2]
		return sum(abs(i - mean) for i in nums)