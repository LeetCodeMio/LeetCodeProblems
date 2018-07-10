# min(a,b) = (a+b - |a-b|)/2
# sum(min(a,b)) = (sum_all - sum|a-b|)/2
# find_max(sum(min(a,b))) <=> find_min(sum|a-b|)
# |a-b| = 数轴上a,b两点连线长度
# sum|a-b| = 在数轴上将nums中的点配对相连的总线长
# 在find_min条件下 不可能有两条连线交叠 否则存在更短连法
# 在'不可能有两条连线交叠'条件下 只可能是近邻配对
class Solution(object) :
	def arrayPairSum(self, nums) :
		nums.sort()
		return sum([nums[i*2] for i in range(len(nums)//2)])