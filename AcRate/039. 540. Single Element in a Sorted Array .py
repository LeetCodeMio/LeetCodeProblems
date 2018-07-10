# 时间O(n) 空间O(0)
# 利用 异或 运算的 交换律 结合律 有
# a^b^d^c^b^a^c = a^a ^ b^b ^ c^c ^ d = 0^0^0^d = d
from functools import reduce
class Solution(object) :
	def singleNonDuplicate(self, nums) :
		return reduce(int.__xor__, nums)