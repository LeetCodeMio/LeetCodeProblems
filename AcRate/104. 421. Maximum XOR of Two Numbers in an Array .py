# 题目描述欠佳 要求时间O(n) int的长度算作O(32)的常数复杂度
# 从最高位到最低位逐位求出ans
# mmp 早说把sizeof(int)视为常数啊 浪费劳资时间
class Solution :
	def findMaximumXOR(self, nums) :
		ans = 0
		for i in reversed(range(31)) :
			ans <<= 1
			top = {num >> i for num in nums}
			ans += any(j^(ans+1) in top for j in top)
		return ans