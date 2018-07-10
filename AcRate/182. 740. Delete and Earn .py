from collections import Counter
class Solution : # 正向动态规划
	def deleteAndEarn(self, nums) :
		nums = sorted((v,n) for v,n in Counter(nums).items())
		earn_2 = 0
		if not nums : return 0
		earn_1 = nums[0][0] * nums[0][1]
		if len(nums) == 1 : return earn_1
		for i in range(1, len(nums)) :
			v,n = nums[i]
			earn = earn_1 + v*n if v != nums[i-1][0] + 1 else max(earn_1, earn_2 + v*n)
			earn_1,earn_2 = earn,earn_1
		return earn