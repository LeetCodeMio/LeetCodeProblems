# 逐位计算结果 第l位的结果为nums中第l位为0的数量乘1的数量
class Solution :
	def totalHammingDistance(self, nums) :
		f = lambda ones : ones * (len(nums) - ones)
		return sum(f(sum((i>>l)&1 for i in nums)) for l in range(30))