# 逐位求解
# 对于每位bit 如果出现1的次数为1mod3 那么它就是singleNumber的bit
# 可以对31个bit分别计数 也可以用循环计数器统一计数
# 循环计数器 用编码 ab = 00 01 10 代表 0mod3 1mod3 2mod3
# 对输入 x = 1 进行状态转移 对输入 x = 0 保持状态
# b' = (b^x) & ~a
# a' = (a^x) & ~b'
class Solution : # t=O(n) m=O(1)
	def singleNumber(self, nums) :
		a,b = 0,0
		for x in nums :
			b = (b^x) & ~a
			a = (a^x) & ~b
		return b
