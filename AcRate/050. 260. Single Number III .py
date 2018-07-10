# 时间O(n) 空间O(1)
# 利用 异或 运算的 交换律 结合律 有
# a^b^d^c^b^a^c^e = a^a ^ b^b ^ c^c ^ d ^ e = 0^0^0^d^e = d^e = t
# 由于d!=e 所以t的bit中一定存在1 不妨设t的第i个bit为1
# 那么d和e的第i个bit位一个为1一个为0
# 不妨设d的为1 e的为0
# 第二遍扫描时 将第i位bit为1/0的异或在一起便得到了d/e
#
# 一个快速保留最低bit位1的trick：
# 由补码规则 ~x = -x - 1
# 有 -x = ~x + 1
# 即 -???1000 = ?'?'?'0111 + 1 = ?'?'?'1000
# 于是 x&(-x) = 0001000
from functools import reduce
class Solution(object) :
	def singleNumber(self, nums) :
		t = reduce(int.__xor__, nums)
		t &= -t
		d, e = 0, 0
		for i in nums :
			if i & t : d ^= i
			else : e ^= i
		return [d, e]