# O(n)动态规划
class Solution(object) :
	def countBits(self, num) :
		ans = [0]
		off = 1
		for i in range(1, num+1) :
			if off << 1 == i : off <<= 1
			# off是仅保留i的最高位1的int
			ans += [ans[i - off] + 1]
			# i的1比i去掉最高位1后的int多一个
		return ans